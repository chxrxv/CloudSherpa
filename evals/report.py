"""Render an eval run as Markdown.

python -m evals.report baseline
python -m evals.report improved --compare baseline
python -m evals.report baseline --worst 3
"""

from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

from evals.labels import judge_validation_status
from evals.run import RUNS_DIR, read_results
from evals.summary import CATEGORY_ORDER
from evals.systems import RunRecord

DET_COLS = [
    ("retrieval_hit_rate", "Retrieval hit"),
    ("citation_validity", "Citation validity"),
    ("citation_recall", "Citation recall"),
    ("refusal_correct", "Refusal correct"),
    ("injection_resisted", "Injection resisted"),
    ("pii_leak_free", "PII leak-free"),
    ("asked_clarification", "Asked clarifying Q"),
]
SMALL_N = 5  # cells with fewer applicable scenarios are flagged as anecdotal
SMALL_N_MARK = "†"
SMALL_N_NOTE = f"{SMALL_N_MARK} n < {SMALL_N}: too few scenarios to read as a rate."
OUTCOME_LABELS = [
    ("refused", "Refused"),
    ("answered", "Answered"),
    ("no_decision", "No decision*"),
    ("error", "Error"),
    ("not_run", "Not run"),
]

JUDGE_COLS = [
    ("judge_groundedness", "Groundedness"),
    ("judge_correctness", "Correctness"),
    ("judge_clarification", "Clarification"),
]


def load_run(tag: str) -> tuple[dict, dict, list[RunRecord]]:
    d = RUNS_DIR / tag
    if not (d / "summary.json").exists():
        raise SystemExit(f"no run at {d}")
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    summary = json.loads((d / "summary.json").read_text(encoding="utf-8"))
    recs = list(read_results(d / "results.jsonl").values())
    return meta, summary, recs


def _pct(m: dict | None) -> str:
    if not m or m.get("mean") is None:
        return "—"
    flag = SMALL_N_MARK if m["n"] < SMALL_N else ""
    return f"{100 * m['mean']:.0f}% ({m['n']}){flag}"


def _delta(new: dict | None, old: dict | None) -> str:
    cell = _pct(new)
    if new and old and new.get("mean") is not None and old.get("mean") is not None:
        d = 100 * (new["mean"] - old["mean"])
        cell = f"{_pct(old).split(' ')[0]} → {cell} ({d:+.0f} pp)"
    return cell


def _ms(v: float | None) -> str:
    return "—" if v is None else f"{v / 1000:.2f} s"


def _judge_label(meta: dict) -> str:
    j = meta.get("judge") or {}
    label = f"{j.get('backend')}:{j.get('model')}"
    return label + (f" @ {j['base_url']}" if j.get("base_url") else "")


def _rows(summary: dict) -> list[tuple[str, dict]]:
    cats = summary["by_category"]
    return [(c, cats[c]) for c in CATEGORY_ORDER if c in cats] + [
        ("**overall**", summary["overall"])
    ]


def metric_table(
    summary: dict,
    cols: list[tuple[str, str]],
    base: dict | None = None,
) -> str:
    head = "| Category | n | " + " | ".join(label for _, label in cols) + " |"
    sep = "|---|---|" + "---|" * len(cols)
    lines = [head, sep]
    base_rows = dict(_rows(base)) if base else {}
    for name, g in _rows(summary):
        b = base_rows.get(name)
        cells = [_delta(g.get(key), b.get(key)) if b else _pct(g.get(key)) for key, _ in cols]
        lines.append(f"| {name} | {g['n']} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def perf_table(summary: dict, base: dict | None = None) -> str:
    lines = [
        "| Category | n | p50 latency | p95 latency | LLM requests | Tokens in / out | Cost "
        "| Errors |",
        "|---|---|---|---|---|---|---|---|",
    ]
    base_rows = dict(_rows(base)) if base else {}
    for name, g in _rows(summary):
        b = base_rows.get(name)
        p50, p95 = _ms(g["latency_p50_ms"]), _ms(g["latency_p95_ms"])
        reqs = str(g.get("llm_requests", 0))
        if b:
            p50 = f"{_ms(b['latency_p50_ms'])} → {p50}"
            p95 = f"{_ms(b['latency_p95_ms'])} → {p95}"
            reqs = f"{b.get('llm_requests', 0)} → {reqs}"
        tokens = f"{g.get('input_tokens', 0):,} / {g.get('output_tokens', 0):,}"
        lines.append(
            f"| {name} | {g['n']} | {p50} | {p95} | {reqs} | {tokens} | $0 (free tier) "
            f"| {g['errors']} |"
        )
    return "\n".join(lines)


def _bounded(r: dict) -> str:
    n = r["n"]
    if not n:
        return "— (n=0)"
    flag = SMALL_N_MARK if n < SMALL_N else ""
    lo, hi = 100 * r["lower"], 100 * r["upper"]
    rng = f"{lo:.0f}%" if r["undecided"] == 0 else f"{lo:.0f}–{hi:.0f}%"
    extra = f"; {r['undecided']} undecided" if r["undecided"] else ""
    return f"{rng} ({r['count']}/{n}{extra}){flag}"


def confusion_section(summary: dict) -> str:
    c = summary.get("refusal_confusion")
    if not c:
        return "_(not available for this run; re-summarize with `python -m evals.summary`)_"
    head = "| Expected → outcome | n | " + " | ".join(lbl for _, lbl in OUTCOME_LABELS) + " |"
    lines = [head, "|---|---|" + "---|" * len(OUTCOME_LABELS)]
    for key, label in (
        ("should_refuse", "should_refuse = true"),
        ("should_answer", "should_refuse = false"),
    ):
        row = c["matrix"][key]
        cells = " | ".join(str(row[k]) for k, _ in OUTCOME_LABELS)
        lines.append(f"| {label} | {row['n']} | {cells} |")
    lines += [
        "",
        r"\* No decision: the retrieval gate passed the question to the LLM, but this run made "
        "no LLM call, so the final refuse/answer outcome is unknown. Rates below are shown "
        "as a range: the low end counts unknown outcomes as not refused/answered, the high "
        "end counts them as refused/answered.",
        "",
        "| Rate | Definition | Value |",
        "|---|---|---|",
        f"| Over-refusal | answerable scenarios refused | {_bounded(c['over_refusal'])} |",
        f"| Under-refusal (out_of_scope) | out-of-scope scenarios answered | "
        f"{_bounded(c['under_refusal_out_of_scope'])} |",
        f"| Under-refusal (all should_refuse) | out-of-scope + injection scenarios answered | "
        f"{_bounded(c['under_refusal_all'])} |",
    ]
    return "\n".join(lines)


def worst(summary: dict, recs: list[RunRecord], k: int) -> str:
    scored = [p for p in summary["per_scenario"] if p["composite"] is not None]
    scored.sort(key=lambda p: (p["composite"], p["id"]))
    by_id = {r.scenario_id: r for r in recs}
    out = []
    for p in scored[:k]:
        r = by_id[p["id"]]
        failing = [
            f"{m}={v:.2f}" if isinstance(v, float) and not isinstance(v, bool) else m
            for m, v in r.metrics.items()
            if v is not None and float(v) < 1.0
        ]
        notes = []
        for kind in ("correctness", "groundedness", "clarification"):
            j = r.judge.get(kind)
            if isinstance(j, dict) and j.get("score") is not None and j["score"] < 1.0:
                detail = j.get("missing") or j.get("unsupported") or j.get("contradicted") or ""
                notes.append(f"{kind}={j['score']:.2f} {detail}".strip())
        excerpt = " ".join(r.answer.split())[:220]
        review = " (scenario flagged needs_human_review)" if p.get("needs_human_review") else ""
        out.append(
            f"- **{p['id']}** ({p['category']}, composite {p['composite']:.2f}){review}\n"
            f"  - failing: {', '.join(failing) or 'none'}; refused={r.refused}"
            f" ({r.refusal_reason})\n"
            + (f"  - judge: {'; '.join(notes)}\n" if notes else "")
            + f'  - answer: "{excerpt}"'
        )
    return "\n".join(out)


def render(tag: str, compare: str | None = None, k_worst: int = 3) -> str:
    meta, summary, recs = load_run(tag)
    base_meta, base = (load_run(compare)[:2]) if compare else (None, None)
    git = meta.get("git", {})
    cfg = meta.get("config", {})
    lines = [f"# Eval report: `{tag}`" + (f" vs `{compare}`" if compare else ""), ""]
    if meta.get("mock"):
        lines += [
            "> **MOCK RUN** — fake model and judge. Tests plumbing only; not a quality "
            "measurement. Do not publish these numbers.",
            "",
        ]
    if meta.get("aborted"):
        lines += [f"> **INCOMPLETE RUN** — {meta['aborted']}", ""]
    if meta.get("mode") == "no_llm":
        lines += [
            "> **Deterministic, retrieval-only run** — no LLM calls (network blocked). "
            "Generation-dependent metrics are N/A unless the retrieval gate refused.",
            "",
        ]
    if base_meta is not None and _judge_label(base_meta) != _judge_label(meta):
        lines += [
            f"> **Judge differs** (`{_judge_label(base_meta)}` vs `{_judge_label(meta)}`): "
            "judge-metric deltas are NOT comparable. Deterministic metrics are.",
            "",
        ]
    lines += [
        f"- Date: {meta.get('started_at')}",
        f"- Commit: `{(git.get('commit') or 'unknown')[:10]}`"
        + (" (dirty working tree)" if git.get("dirty") else ""),
        f"- System: {meta.get('system')} (prompt {meta.get('prompt_version')}); "
        f"generator `{cfg.get('flash_model') if meta.get('mode') != 'no_llm' else 'none'}`; "
        f"judge `{_judge_label(meta)}`",
        f"- Billing: {meta.get('billing')}; rate limits {meta.get('rate_limits')}",
        f"- Retrieval: {cfg.get('retrieval_mode')} / {cfg.get('chunking_strategy')} chunks "
        f"({cfg.get('chunk_size')}/{cfg.get('chunk_overlap')}) / reranker {cfg.get('reranker')}"
        f" / top_k {cfg.get('top_k')} / min_confidence {cfg.get('min_confidence')}",
        f"- Scenarios: {meta.get('completed')}/{meta.get('planned')} "
        f"(golden sha256 `{meta.get('golden_sha256')}`)",
        "",
        "## Deterministic metrics",
        "",
        "Cells: mean (n applicable). Metrics that don't apply to a scenario are excluded. "
        + SMALL_N_NOTE,
        "",
        metric_table(summary, DET_COLS, base),
        "",
        f"## LLM-as-judge metrics — {judge_validation_status(tag)}",
        "",
        metric_table(summary, JUDGE_COLS, base),
        "",
        "## Refusal behaviour (all planned scenarios)",
        "",
        confusion_section(summary),
        "",
        "## Latency, requests and cost (system under test)",
        "",
        perf_table(summary, base),
        "",
        _judge_usage(summary),
        "",
        f"## {k_worst} worst scenarios (lowest mean of applicable metrics)",
        "",
        worst(summary, recs, k_worst),
        "",
    ]
    return "\n".join(lines)


def _judge_usage(summary: dict) -> str:
    j = summary.get("judge") or {}
    if not j.get("backends"):
        return "Judge: not run."
    return (
        f"Judge ({', '.join(j['backends'])}): {j.get('requests', 0)} requests, "
        f"{j.get('cache_hits', 0)} cache hits, "
        f"{j.get('input_tokens', 0):,} / {j.get('output_tokens', 0):,} tokens, "
        "cost $0 (free tier / local)."
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tag")
    ap.add_argument("--compare")
    ap.add_argument("--worst", type=int, default=3)
    ap.add_argument("--out", type=Path, help="also write the Markdown to this file")
    args = ap.parse_args(argv)
    md = render(args.tag, args.compare, args.worst)
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    print(md)
    if args.out:
        args.out.write_text(md, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
