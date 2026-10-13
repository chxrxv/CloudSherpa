"""Aggregate scored RunRecords into per-category and overall metrics."""

from __future__ import annotations

from collections import defaultdict

from evals.metrics import DETERMINISTIC, latency_cost_summary, mean_applicable
from evals.schema import Scenario
from evals.systems import RunRecord

JUDGE_METRICS = ("groundedness", "correctness", "clarification")
CATEGORY_ORDER = (
    "architecture",
    "multi_hop",
    "ambiguous",
    "out_of_scope",
    "prompt_injection",
    "pii",
)


def judge_score(rec: RunRecord, kind: str) -> float | None:
    v = rec.judge.get(kind)
    if isinstance(v, dict):
        s = v.get("score")
        return float(s) if isinstance(s, int | float) else None
    return None


def composite(rec: RunRecord) -> float | None:
    """Mean of every applicable metric for one scenario (bools as 0/1). Used to rank worst."""
    vals = [float(v) for v in rec.metrics.values() if v is not None]
    vals += [s for k in JUDGE_METRICS if (s := judge_score(rec, k)) is not None]
    return sum(vals) / len(vals) if vals else None


def _group(recs: list[RunRecord]) -> dict[str, object]:
    out: dict[str, object] = {"n": len(recs)}
    for name in DETERMINISTIC:
        mean, n = mean_applicable(r.metrics.get(name) for r in recs)
        out[name] = {"mean": mean, "n": n}
    for kind in JUDGE_METRICS:
        mean, n = mean_applicable(judge_score(r, kind) for r in recs)
        out[f"judge_{kind}"] = {"mean": mean, "n": n}
    out.update(latency_cost_summary(recs))
    return out


def summarize(records: list[RunRecord], scenarios: dict[str, Scenario]) -> dict[str, object]:
    by_cat: dict[str, list[RunRecord]] = defaultdict(list)
    for r in records:
        by_cat[r.category].append(r)
    judged = [r.judge for r in records if r.judge]

    def _total(key: str) -> int:
        return sum(int(j.get(key, 0) or 0) for j in judged)  # type: ignore[call-overload]

    return {
        "overall": _group(records),
        "by_category": {c: _group(by_cat[c]) for c in CATEGORY_ORDER if c in by_cat},
        "per_scenario": [
            {
                "id": r.scenario_id,
                "category": r.category,
                "composite": composite(r),
                "error": r.error,
                "needs_human_review": scenarios[r.scenario_id].needs_human_review
                if r.scenario_id in scenarios
                else False,
            }
            for r in records
        ],
        "judge": {
            "backends": sorted(
                {f"{j.get('judge_backend')}:{j.get('judge_model')}" for j in judged}
            ),
            "requests": _total("judge_requests"),
            "cache_hits": _total("judge_cache_hits"),
            "input_tokens": _total("judge_input_tokens"),
            "output_tokens": _total("judge_output_tokens"),
            "cost_usd": 0.0,  # free tier or local backend
        },
    }
