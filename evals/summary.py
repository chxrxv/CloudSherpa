"""Aggregate scored RunRecords into per-category and overall metrics."""

from __future__ import annotations

from collections import defaultdict

from evals.metrics import DETERMINISTIC, behaved_as_refusal, latency_cost_summary, mean_applicable
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


OUTCOMES = ("refused", "answered", "no_decision", "error", "not_run")


def outcome(rec: RunRecord | None) -> str:
    """Refusal outcome of one scenario. `no_decision`: the retrieval gate let it through but
    generation was skipped (retrieval-only run), so whether the system refuses is unknown."""
    if rec is None:
        return "not_run"
    if rec.error:
        return "error"
    if behaved_as_refusal(rec):
        return "refused"
    return "no_decision" if not rec.generated else "answered"


def _rate(num: int, n: int, undecided: int) -> dict[str, object]:
    """Rate with bounds: undecided cases could go either way once the LLM decides."""
    if n == 0:
        return {"n": 0, "count": 0, "undecided": 0, "lower": None, "upper": None}
    return {
        "n": n,
        "count": num,
        "undecided": undecided,
        "lower": num / n,
        "upper": (num + undecided) / n,
    }


def refusal_confusion(
    records: list[RunRecord], scenarios: dict[str, Scenario]
) -> dict[str, object]:
    """should_refuse x outcome counts over ALL planned scenarios, plus over/under-refusal."""
    by_id = {r.scenario_id: r for r in records}
    matrix = {label: dict.fromkeys(OUTCOMES, 0) for label in ("should_refuse", "should_answer")}
    for sid, sc in scenarios.items():
        row = "should_refuse" if sc.should_refuse else "should_answer"
        matrix[row][outcome(by_id.get(sid))] += 1

    def _subset(pred: object) -> dict[str, int]:
        counts = dict.fromkeys(OUTCOMES, 0)
        for sid, sc in scenarios.items():
            if pred(sc):  # type: ignore[operator]
                counts[outcome(by_id.get(sid))] += 1
        return counts

    ans, ref = matrix["should_answer"], matrix["should_refuse"]
    oos = _subset(lambda sc: sc.category == "out_of_scope")

    def unknown(c: dict[str, int]) -> int:
        return c["no_decision"] + c["error"] + c["not_run"]

    return {
        "matrix": {k: {**v, "n": sum(v.values())} for k, v in matrix.items()},
        # Over-refusal: answerable scenarios that were refused.
        "over_refusal": _rate(ans["refused"], sum(ans.values()), unknown(ans)),
        # Under-refusal: should-refuse scenarios that were answered.
        "under_refusal_all": _rate(ref["answered"], sum(ref.values()), unknown(ref)),
        "under_refusal_out_of_scope": _rate(oos["answered"], sum(oos.values()), unknown(oos)),
    }


def summarize(records: list[RunRecord], scenarios: dict[str, Scenario]) -> dict[str, object]:
    by_cat: dict[str, list[RunRecord]] = defaultdict(list)
    for r in records:
        by_cat[r.category].append(r)
    judged = [r.judge for r in records if r.judge]

    def _total(key: str) -> int:
        return sum(int(j.get(key, 0) or 0) for j in judged)  # type: ignore[call-overload]

    return {
        "overall": _group(records),
        "refusal_confusion": refusal_confusion(records, scenarios),
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


def main(argv: list[str] | None = None) -> int:
    """Recompute summary.json for a finished run from its results.jsonl (no model calls)."""
    import argparse
    import json

    from evals.run import RUNS_DIR, file_sha256, read_results
    from evals.schema import EVALS_DIR, load_scenarios

    ap = argparse.ArgumentParser(description=main.__doc__)
    ap.add_argument("tag")
    args = ap.parse_args(argv)
    run_dir = RUNS_DIR / args.tag
    meta = json.loads((run_dir / "meta.json").read_text(encoding="utf-8"))
    golden = EVALS_DIR / meta.get("golden_file", "golden.jsonl")
    if file_sha256(golden) != meta.get("golden_sha256"):
        raise SystemExit("golden set changed since this run; refusing to re-summarize")
    planned = set(meta["scenario_ids"])
    scenarios = {s.id: s for s in load_scenarios(golden) if s.id in planned}
    records = [
        r for r in read_results(run_dir / "results.jsonl").values() if not r.judge.get("pending")
    ]
    summary = summarize(records, scenarios)
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"rewrote {run_dir / 'summary.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
