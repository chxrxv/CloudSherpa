"""Run the golden set through the current pipeline and score it.

    python -m evals.run --tag det-baseline --no-llm    # deterministic baseline, NO network
    python -m evals.run --tag smoke5 --subset 5        # free-tier Gemini, stratified 5
    python -m evals.run --tag baseline                 # all 50 scenarios (free tier)
    python -m evals.run --tag baseline --resume        # continue after a quota stop
    python -m evals.run --tag ci --smoke --mock        # 5 scenarios, mocked LLM + judge

Writes evals/runs/<tag>/{results.jsonl, meta.json, summary.json}.

Free-tier guarantees: only an AI Studio API key and free-tier Flash models are allowed
(FREE_TIER_ONLY); every request goes through a per-model RPM throttle and a persisted daily
request budget; 429s back off exponentially. When the daily budget or server quota runs out,
the run stops cleanly, keeps what it finished, and `--resume` continues later without
repeating answered scenarios or cached judge calls. Nothing is ever estimated or fabricated.
"""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from core.config import REPO_ROOT, FreeTierViolation, Settings, get_settings
from core.llm import (
    FakeLLM,
    GeminiClient,
    LLMCallError,
    LLMClient,
    OpenAICompatClient,
    QuotaExhaustedError,
)
from evals.judge import Judge, LLMJudge, MockJudge
from evals.judge_cache import JudgeCache
from evals.metrics import score_deterministic
from evals.netguard import no_network
from evals.schema import GOLDEN_PATH, Scenario, load_scenarios
from evals.summary import summarize
from evals.systems import RagSystem, RunRecord, System

RUNS_DIR = REPO_ROOT / "evals" / "runs"
SMOKE_IDS = ["arch-03", "mh-05", "oos-01", "inj-04", "pii-02"]
MAX_CONSECUTIVE_ERRORS = 3
EXIT_ABORTED = 3
# meta keys that must match for --resume to be allowed (otherwise results would mix setups)
RESUME_KEYS = (
    "mode",
    "system",
    "prompt_version",
    "judge",
    "golden_sha256",
    "config",
    "scenario_ids",
)


def stratified_subset(scenarios: list[Scenario], n: int) -> list[Scenario]:
    """Deterministic round-robin across categories so small subsets still cover everything."""
    by_cat: dict[str, list[Scenario]] = defaultdict(list)
    for s in scenarios:
        by_cat[s.category].append(s)
    picked: list[Scenario] = []
    while len(picked) < min(n, len(scenarios)):
        for cat in sorted(by_cat):
            if by_cat[cat] and len(picked) < n:
                picked.append(by_cat[cat].pop(0))
    return sorted(picked, key=lambda s: scenarios.index(s))


def mock_responder(prompt: str) -> str:
    """Fake generator: restates the first sentence of source S1 and cites it."""
    m = re.search(r"\[S1\][^\n]*\n(.+?)(?:\n\n\[S2\]|\n\n---)", prompt, flags=re.S)
    if not m:
        return "INSUFFICIENT_CONTEXT"
    first = " ".join(m.group(1).split())
    sentence = re.split(r"(?<=[.!?])\s", first, maxsplit=1)[0][:300]
    return f"{sentence} [S1]"


def git_info() -> dict[str, object]:
    def _git(*args: str) -> str:
        try:
            return subprocess.run(
                ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
            ).stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            return ""

    return {
        "commit": _git("rev-parse", "HEAD") or None,
        "dirty": bool(_git("status", "--porcelain")),
    }


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def _judge_pending(rec: RunRecord) -> bool:
    return bool(rec.judge.get("pending"))


def read_results(path: Path) -> dict[str, RunRecord]:
    """results.jsonl is an append-only log; the last record per scenario wins."""
    if not path.exists():
        return {}
    out: dict[str, RunRecord] = {}
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                r = RunRecord.model_validate_json(line)
                out[r.scenario_id] = r
    return out


def load_previous(out_dir: Path) -> dict[str, RunRecord]:
    """Reusable records from an earlier (possibly interrupted) run: everything but errors."""
    return {k: r for k, r in read_results(out_dir / "results.jsonl").items() if not r.error}


def run_eval(
    scenarios: list[Scenario],
    system: System,
    judge: Judge | None,
    out_dir: Path,
    meta: dict[str, Any],
    previous: dict[str, RunRecord] | None = None,
) -> dict[str, Any]:
    """Core loop (no CLI concerns) so tests can drive it with fakes.

    `previous` holds records to reuse (resume). A record whose judging was interrupted is
    re-judged without re-running the system.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    previous = previous or {}
    results_path = out_dir / "results.jsonl"
    processed: dict[str, RunRecord] = {}
    consecutive_errors = 0
    aborted: str | None = None
    reused = rejudged = 0

    # Append-only while running (a hard kill loses at most the in-flight scenario); compacted
    # at the end. A fresh run truncates; a resumed run appends to the existing log.
    with results_path.open("a" if previous else "w", encoding="utf-8") as f:

        def emit(rec: RunRecord) -> None:
            processed[rec.scenario_id] = rec
            f.write(rec.model_dump_json() + "\n")
            f.flush()

        for i, sc in enumerate(scenarios, start=1):
            prev = previous.get(sc.id)
            if prev is not None and not _judge_pending(prev):
                processed[sc.id] = prev  # already complete: no calls at all
                reused += 1
                continue
            try:
                if prev is not None:
                    rec = prev  # answer already generated; only judging is missing
                    rejudged += 1
                else:
                    try:
                        rec = system.run(sc)
                        consecutive_errors = 0
                    except QuotaExhaustedError:
                        raise
                    except LLMCallError as exc:
                        rec = RunRecord(
                            scenario_id=sc.id, category=sc.category, error=str(exc)[:500]
                        )
                        consecutive_errors += 1
                rec.metrics = score_deterministic(rec, sc)
                rec.judge = {}
                if judge is not None and not rec.error:
                    try:
                        rec.judge = judge.judge(rec, sc)
                    except QuotaExhaustedError as exc:
                        # Keep the generated answer; --resume will only re-judge it.
                        rec.judge = {"pending": str(exc)[:300]}
                        emit(rec)
                        raise
            except QuotaExhaustedError as exc:
                aborted = f"quota: {exc}"
                print(f"[{i:>2}/{len(scenarios)}] {sc.id:<8} STOPPED  {aborted}", file=sys.stderr)
                break
            emit(rec)
            status = "ERROR" if rec.error else ("refused" if rec.refused else "answered")
            if not rec.generated:
                status = "gate-ok"
            print(
                f"[{i:>2}/{len(scenarios)}] {sc.id:<8} {status:<8} {rec.latency_ms:>7.0f} ms "
                f"req={rec.llm_requests}",
                flush=True,
            )
            if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                aborted = (
                    f"aborted after {consecutive_errors} consecutive LLM errors "
                    f"(last: {rec.error}); remaining scenarios were not run"
                )
                print(aborted, file=sys.stderr)
                break

    # Compact: this run's records plus any earlier records it did not reach, in plan order.
    final = {**previous, **processed}
    records = [final[s.id] for s in scenarios if s.id in final]
    tmp = results_path.with_suffix(".jsonl.tmp")
    tmp.write_text("".join(r.model_dump_json() + "\n" for r in records), encoding="utf-8")
    tmp.replace(results_path)

    done = [r for r in records if not _judge_pending(r)]
    meta = {
        **meta,
        "completed": len(done),
        "planned": len(scenarios),
        "reused_from_previous": reused,
        "rejudged": rejudged,
        "aborted": aborted,
        "finished_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")
    summary = summarize(done, {s.id: s for s in scenarios})
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return {"meta": meta, "summary": summary}


def make_judge(settings: Settings, mock: bool) -> tuple[Judge, LLMClient | None]:
    if mock:
        return MockJudge(), None
    cache = JudgeCache(settings.judge_cache_dir)
    if settings.judge_backend == "openai_compat":
        if settings.judge_model.startswith("gemini-"):
            raise SystemExit(
                "JUDGE_BACKEND=openai_compat needs JUDGE_MODEL set to the local model name "
                "(e.g. JUDGE_MODEL=qwen2.5:7b-instruct for Ollama)."
            )
        client: LLMClient = OpenAICompatClient(settings.judge_base_url, settings.judge_api_key)
        return LLMJudge(client, settings.judge_model, "openai_compat", cache), client
    if settings.judge_model == settings.flash_model:
        raise SystemExit("JUDGE_MODEL must differ from the model under test (FLASH_MODEL).")
    settings.check_free_tier(settings.judge_model)
    gclient = GeminiClient(settings)
    return LLMJudge(gclient, settings.judge_model, "gemini", cache), gclient


def judge_meta(settings: Settings, judge: Judge | None) -> dict[str, object]:
    if judge is None:
        return {"backend": "none", "model": None}
    info: dict[str, object] = {"backend": judge.backend, "model": judge.model}
    if judge.backend == "openai_compat":
        info["base_url"] = settings.judge_base_url
    return info


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--tag", required=True, help="run name; output in evals/runs/<tag>/")
    ap.add_argument("--subset", type=int, help="stratified subset of N scenarios")
    ap.add_argument("--smoke", action="store_true", help=f"only {SMOKE_IDS}")
    ap.add_argument("--ids", help="comma-separated scenario ids")
    ap.add_argument("--categories", help="comma-separated categories")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--mock", action="store_true", help="fake LLM + judge (no credentials)")
    mode.add_argument(
        "--no-llm",
        action="store_true",
        help="deterministic baseline: retrieval + gate only, network blocked",
    )
    ap.add_argument("--no-judge", action="store_true", help="deterministic metrics only")
    ap.add_argument("--resume", action="store_true", help="continue an interrupted run")
    ap.add_argument("--prompt-version", default="v1")
    ap.add_argument("--golden", default=str(GOLDEN_PATH))
    ap.add_argument("--force", action="store_true", help="overwrite an existing run tag")
    args = ap.parse_args(argv)

    settings = get_settings()
    scenarios = load_scenarios(Path(args.golden))
    if args.smoke:
        scenarios = [s for s in scenarios if s.id in SMOKE_IDS]
    if args.ids:
        wanted = set(args.ids.split(","))
        scenarios = [s for s in scenarios if s.id in wanted]
    if args.categories:
        cats = set(args.categories.split(","))
        scenarios = [s for s in scenarios if s.category in cats]
    if args.subset:
        scenarios = stratified_subset(scenarios, args.subset)
    if not scenarios:
        print("no scenarios selected", file=sys.stderr)
        return 2

    out_dir = RUNS_DIR / args.tag
    if out_dir.exists() and not (args.force or args.resume):
        print(
            f"{out_dir} exists; pass --resume to continue it or --force to overwrite",
            file=sys.stderr,
        )
        return 2
    if args.resume and not (out_dir / "meta.json").exists():
        print(f"nothing to resume at {out_dir}", file=sys.stderr)
        return 2

    run_mode = "mock" if args.mock else ("no_llm" if args.no_llm else "live")
    if run_mode == "live":
        try:
            settings.check_free_tier(settings.flash_model)
        except FreeTierViolation as exc:
            print(f"Refusing to run: {exc}", file=sys.stderr)
            return 2
        if not settings.has_llm_credentials:
            print(
                "Cannot run: no GEMINI_API_KEY in .env (use an AI Studio key on a project "
                "without billing). Use --no-llm for the network-free deterministic baseline or "
                "--mock for a plumbing-only run. No results were written.",
                file=sys.stderr,
            )
            return 2

    guard = no_network() if run_mode == "no_llm" else contextlib.nullcontext()
    with guard:
        from rag.retriever import HybridRetriever

        llm: LLMClient | None
        judge: Judge | None = None
        judge_client: LLMClient | None = None
        if run_mode == "mock":
            llm = FakeLLM(mock_responder)
            judge = None if args.no_judge else MockJudge()
        elif run_mode == "no_llm":
            llm = None
        else:
            llm = GeminiClient(settings)
            if not args.no_judge:
                judge, judge_client = make_judge(settings, mock=False)

        system = RagSystem(
            settings, HybridRetriever.from_settings(settings), llm, args.prompt_version
        )
        meta: dict[str, Any] = {
            "tag": args.tag,
            "started_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
            "mode": run_mode,
            "mock": run_mode == "mock",
            "network_guard": run_mode == "no_llm",
            "system": system.name,
            "prompt_version": args.prompt_version,
            "judge": judge_meta(settings, judge),
            "billing": "free tier ($0): AI Studio API key, FREE_TIER_ONLY enforced"
            if run_mode == "live"
            else "none (no LLM calls)",
            "rate_limits": {
                "rpm_per_model": settings.llm_rpm,
                "daily_request_budget_per_model": settings.llm_daily_request_budget,
                "max_retries": settings.llm_max_retries,
            },
            "golden_file": Path(args.golden).name,
            "golden_sha256": file_sha256(Path(args.golden)),
            "scenario_ids": [s.id for s in scenarios],
            "git": git_info(),
            "config": settings.snapshot(),
            "python": sys.version.split()[0],
        }

        previous: dict[str, RunRecord] = {}
        if args.resume:
            old = json.loads((out_dir / "meta.json").read_text(encoding="utf-8"))
            diffs = [k for k in RESUME_KEYS if old.get(k) != meta.get(k)]
            if diffs:
                print(
                    f"Refusing to resume {args.tag}: {diffs} changed since the run started "
                    "(results would mix setups). Use a new --tag.",
                    file=sys.stderr,
                )
                return 2
            previous = load_previous(out_dir)
            meta["resumed_from"] = old.get("started_at")
            print(f"resuming: {len(previous)} completed/partial records found")

        print(
            f"running {len(scenarios)} scenarios -> {out_dir} (mode={run_mode}, "
            f"judge={meta['judge']})"
        )
        result = run_eval(scenarios, system, judge, out_dir, meta, previous)

    # Record what the server told us about quotas (the only source of real free-tier limits).
    observed = []
    for c in (llm, judge_client):
        if isinstance(c, GeminiClient):
            observed += c.observed_quota
    if observed or isinstance(llm, GeminiClient):
        m = result["meta"]
        m["observed_quota_violations"] = observed
        if isinstance(llm, GeminiClient):
            gov = llm.governor
            m["requests_today_pacific"] = {
                "day": gov.pacific_day(),
                **{
                    mdl: gov.used_today(mdl) for mdl in {settings.flash_model, settings.judge_model}
                },
            }
            m["throttle_wait_s"] = round(gov.waited_s, 1)
        (out_dir / "meta.json").write_text(json.dumps(m, indent=2, default=str), encoding="utf-8")

    print(json.dumps(result["summary"]["overall"], indent=2))
    if result["meta"]["aborted"]:
        print(
            f"\nRun stopped early: {result['meta']['aborted']}\n"
            f"Completed {result['meta']['completed']}/{result['meta']['planned']}. "
            f"Continue later with: python -m evals.run --tag {args.tag} --resume",
            file=sys.stderr,
        )
        return EXIT_ABORTED
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
