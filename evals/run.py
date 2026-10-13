"""Run the golden set through the current pipeline and score it.

    python -m evals.run --tag baseline                 # full golden set (costs API credits)
    python -m evals.run --tag quick --subset 10        # stratified 10-scenario subset
    python -m evals.run --tag ci --smoke --mock        # 5 scenarios, mocked LLM + judge (free)

Writes evals/runs/<tag>/{results.jsonl, meta.json, summary.json}. Without LLM credentials a
real run refuses to start; it never fabricates outputs. With --mock, outputs come from a
deterministic fake model and the run is marked `mock: true` — it tests plumbing, not quality.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

from core.config import REPO_ROOT, Settings, get_settings
from core.llm import FakeLLM, LLMCallError, LLMClient
from core.pricing import PriceTable, load_price_table
from evals.judge import Judge, LLMJudge, MockJudge
from evals.metrics import score_deterministic
from evals.schema import GOLDEN_PATH, Scenario, load_scenarios
from evals.summary import summarize
from evals.systems import RagSystem, RunRecord, System

RUNS_DIR = REPO_ROOT / "evals" / "runs"
SMOKE_IDS = ["arch-03", "mh-05", "oos-01", "inj-04", "pii-02"]
MAX_CONSECUTIVE_ERRORS = 3


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


def run_eval(
    scenarios: list[Scenario],
    system: System,
    judge: Judge | None,
    out_dir: Path,
    meta: dict[str, object],
) -> dict[str, object]:
    """Core loop (no CLI concerns) so tests can drive it with fakes."""
    out_dir.mkdir(parents=True, exist_ok=True)
    results_path = out_dir / "results.jsonl"
    records: list[RunRecord] = []
    consecutive_errors = 0
    aborted: str | None = None

    with results_path.open("w", encoding="utf-8") as f:
        for i, sc in enumerate(scenarios, start=1):
            try:
                rec = system.run(sc)
                consecutive_errors = 0
            except LLMCallError as exc:
                rec = RunRecord(scenario_id=sc.id, category=sc.category, error=str(exc)[:500])
                consecutive_errors += 1
            rec.metrics = score_deterministic(rec, sc)
            if judge is not None and not rec.error:
                rec.judge = judge.judge(rec, sc)
            records.append(rec)
            f.write(rec.model_dump_json() + "\n")
            f.flush()
            status = "ERROR" if rec.error else ("refused" if rec.refused else "answered")
            print(
                f"[{i:>2}/{len(scenarios)}] {sc.id:<8} {status:<8} {rec.latency_ms:>7.0f} ms",
                flush=True,
            )
            if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                aborted = (
                    f"aborted after {consecutive_errors} consecutive LLM errors "
                    f"(last: {rec.error}); remaining scenarios were not run"
                )
                print(aborted, file=sys.stderr)
                break

    meta = {**meta, "completed": len(records), "planned": len(scenarios), "aborted": aborted}
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")
    summary = summarize(records, {s.id: s for s in scenarios})
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return {"meta": meta, "summary": summary}


def build_meta(
    args: argparse.Namespace, settings: Settings, scenarios: list[Scenario], judge_model: str
) -> dict[str, object]:
    prices = load_price_table(settings.price_table)
    return {
        "tag": args.tag,
        "started_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "mock": args.mock,
        "system": "rag-v1",
        "prompt_version": args.prompt_version,
        "judge_model": judge_model,
        "golden_file": str(Path(args.golden).relative_to(REPO_ROOT))
        if Path(args.golden).is_relative_to(REPO_ROOT)
        else str(args.golden),
        "golden_sha256": file_sha256(Path(args.golden)),
        "scenario_ids": [s.id for s in scenarios],
        "git": git_info(),
        "config": settings.snapshot(),
        "price_table": {"source": prices.source, "retrieved": prices.retrieved},
        "python": sys.version.split()[0],
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--tag", required=True, help="run name; output in evals/runs/<tag>/")
    ap.add_argument("--subset", type=int, help="stratified subset of N scenarios")
    ap.add_argument("--smoke", action="store_true", help=f"only {SMOKE_IDS}")
    ap.add_argument("--ids", help="comma-separated scenario ids")
    ap.add_argument("--categories", help="comma-separated categories")
    ap.add_argument("--mock", action="store_true", help="fake LLM + judge (no credentials)")
    ap.add_argument("--no-judge", action="store_true", help="deterministic metrics only")
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
    if out_dir.exists() and not args.force:
        print(f"{out_dir} exists; pass --force to overwrite", file=sys.stderr)
        return 2

    if not args.mock and not settings.has_llm_credentials:
        print(
            "Cannot run: no LLM credentials. Set GEMINI_API_KEY (or GOOGLE_GENAI_USE_VERTEXAI=true "
            "+ GOOGLE_CLOUD_PROJECT) in .env, or pass --mock for a plumbing-only run. "
            "No results were written.",
            file=sys.stderr,
        )
        return 2

    from rag.retriever import HybridRetriever

    prices = load_price_table(settings.price_table)
    llm: LLMClient
    judge: Judge | None
    if args.mock:
        llm = FakeLLM(mock_responder)
        # Fake token counts must not be turned into dollar figures.
        prices = PriceTable(source="mock", retrieved="n/a", models={})
        judge = None if args.no_judge else MockJudge()
    else:
        from core.llm import GeminiClient

        llm = GeminiClient(settings)
        judge = None if args.no_judge else LLMJudge(llm, settings.judge_model, prices)
    if judge is not None and not args.mock and settings.judge_model == settings.flash_model:
        print("JUDGE_MODEL must differ from the model under test (FLASH_MODEL).", file=sys.stderr)
        return 2

    system = RagSystem(
        settings, HybridRetriever.from_settings(settings), llm, prices, args.prompt_version
    )
    meta = build_meta(args, settings, scenarios, judge.model if judge else "none")
    print(f"running {len(scenarios)} scenarios -> {out_dir} (mock={args.mock})")
    result = run_eval(scenarios, system, judge, out_dir, meta)
    overall = result["summary"]["overall"]  # type: ignore[index]
    print(json.dumps(overall, indent=2))
    return 1 if result["meta"]["aborted"] else 0  # type: ignore[index]


if __name__ == "__main__":
    raise SystemExit(main())
