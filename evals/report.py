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
from evals.run import RUNS_DIR
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
    with (d / "results.jsonl").open(encoding="utf-8") as f:
        recs = [RunRecord.model_validate_json(line) for line in f if line.strip()]
    return meta, summary, recs


def _pct(m: dict | None) -> str:
    if not m or m.get("mean") is None:
        return "—"
    return f"{100 * m['mean']:.0f}% ({m['n']})"


def _delta(new: dict | None, old: dict | None) -> str:
    cell = _pct(new)
    if new and old and new.get("mean") is not None and old.get("mean") is not None:
        d = 100 * (new["mean"] - old["mean"])
        cell = f"{_pct(old).split(' ')[0]} → {cell} ({d:+.0f} pp)"
    return cell


def _ms(v: float | None) -> str:
    return "—" if v is None else f"{v / 1000:.2f} s"


def _usd(v: float | None) -> str:
    return "unpriced" if v is None else f"${v:.5f}"


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
        "| Category | p50 latency | p95 latency | Cost / query | Errors |",
        "|---|---|---|---|---|",
    ]
    base_rows = dict(_rows(base)) if base else {}
    for name, g in _rows(summary):
        b = base_rows.get(name)
        p50, p95, cost = (
            _ms(g["latency_p50_ms"]),
            _ms(g["latency_p95_ms"]),
            _usd(g["cost_per_query_usd"]),
        )
        if b:
            p50 = f"{_ms(b['latency_p50_ms'])} → {p50}"
            p95 = f"{_ms(b['latency_p95_ms'])} → {p95}"
            cost = f"{_usd(b['cost_per_query_usd'])} → {cost}"
        lines.append(f"| {name} | {p50} | {p95} | {cost} | {g['errors']} |")
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
    base = load_run(compare)[1] if compare else None
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
    lines += [
        f"- Date: {meta.get('started_at')}",
        f"- Commit: `{(git.get('commit') or 'unknown')[:10]}`"
        + (" (dirty working tree)" if git.get("dirty") else ""),
        f"- System: {meta.get('system')} (prompt {meta.get('prompt_version')}); "
        f"generator `{cfg.get('flash_model')}`; judge `{meta.get('judge_model')}`",
        f"- Retrieval: {cfg.get('retrieval_mode')} / {cfg.get('chunking_strategy')} chunks "
        f"({cfg.get('chunk_size')}/{cfg.get('chunk_overlap')}) / reranker {cfg.get('reranker')}"
        f" / top_k {cfg.get('top_k')} / min_confidence {cfg.get('min_confidence')}",
        f"- Scenarios: {meta.get('completed')}/{meta.get('planned')} "
        f"(golden sha256 `{meta.get('golden_sha256')}`)",
        "",
        "## Deterministic metrics",
        "",
        "Cells: mean (n applicable). Metrics that don't apply to a scenario are excluded.",
        "",
        metric_table(summary, DET_COLS, base),
        "",
        f"## LLM-as-judge metrics — {judge_validation_status(tag)}",
        "",
        metric_table(summary, JUDGE_COLS, base),
        "",
        "## Latency and cost (system under test; judge cost excluded)",
        "",
        perf_table(summary, base),
        "",
        f"Judge cost for this run: {_usd(summary.get('judge_cost_total_usd'))}",
        "",
        f"## {k_worst} worst scenarios (lowest mean of applicable metrics)",
        "",
        worst(summary, recs, k_worst),
        "",
    ]
    return "\n".join(lines)


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
