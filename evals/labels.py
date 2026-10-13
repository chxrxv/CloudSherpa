"""Judge validation: human labels vs LLM-judge verdicts.

    python -m evals.labels <tag>          # pick 10 judged scenarios, print a blind labeling
                                           # sheet, write evals/judge_labels.jsonl (labels null)
    python -m evals.labels <tag> --agreement

Labels are binary so agreement is unambiguous:
  groundedness  -> true if EVERY factual claim in the answer is supported by the context
  correctness   -> true if the answer covers the key facts with no contradiction
  clarification -> true if the response asks useful clarifying questions (judge score >= 4/5)
The sheet hides the judge's verdict so labels are not anchored on it.
"""

from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path
from typing import Any

from evals.schema import EVALS_DIR, load_scenarios

LABELS_PATH = EVALS_DIR / "judge_labels.jsonl"
N_LABELS = 10
# How many scenarios per rubric to put in front of the human.
PLAN = {"correctness": 4, "groundedness": 4, "clarification": 2}


def judge_binary(kind: str, verdict: dict) -> bool | None:
    score = verdict.get("score")
    if score is None:
        return None
    if kind == "groundedness":
        return bool(score == 1.0)
    if kind == "correctness":
        return bool(score >= 0.75 and not verdict.get("contradicted"))
    if kind == "clarification":
        return bool(verdict.get("helpfulness_1to5", 0) >= 4)
    raise ValueError(kind)


def read_labels(path: Path = LABELS_PATH) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def cohen_kappa(pairs: list[tuple[bool, bool]]) -> float | None:
    n = len(pairs)
    if n == 0:
        return None
    po = sum(a == b for a, b in pairs) / n
    pa = sum(a for a, _ in pairs) / n
    pb = sum(b for _, b in pairs) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return None if pe == 1 else (po - pe) / (1 - pe)


def agreement(tag: str, path: Path = LABELS_PATH) -> dict[str, Any] | None:
    """Compare filled-in human labels for `tag` with the judge. None if no labels yet."""
    from evals.report import load_run  # local import: report imports this module

    labels = [
        x for x in read_labels(path) if x.get("run_tag") == tag and x.get("human_label") is not None
    ]
    if not labels:
        return None
    _, _, recs = load_run(tag)
    by_id = {r.scenario_id: r for r in recs}
    pairs: list[tuple[bool, bool]] = []
    disagreements = []
    for x in labels:
        verdict = by_id[x["scenario_id"]].judge.get(x["metric"])
        jb = judge_binary(x["metric"], verdict) if isinstance(verdict, dict) else None
        if jb is None:
            continue
        pairs.append((bool(x["human_label"]), jb))
        if bool(x["human_label"]) != jb:
            disagreements.append(f"{x['scenario_id']}/{x['metric']}")
    if not pairs:
        return None
    return {
        "n": len(pairs),
        "agreement": sum(a == b for a, b in pairs) / len(pairs),
        "cohen_kappa": cohen_kappa(pairs),
        "disagreements": disagreements,
    }


def judge_validation_status(tag: str) -> str:
    a = agreement(tag)
    if not a:
        return "**UNVALIDATED** (no human labels yet; see `python -m evals.labels`)"
    kappa = a["cohen_kappa"]
    k = "n/a" if kappa is None else f"{kappa:.2f}"
    return (
        f"validated against {a['n']} human labels: agreement "
        f"{100 * float(a['agreement']):.0f}%, Cohen's κ {k}"
    )


def select_for_labeling(tag: str) -> list[tuple[str, str]]:
    """Deterministic pick of (scenario_id, metric) pairs that the judge actually scored."""
    from evals.report import load_run

    _, _, recs = load_run(tag)
    picked: list[tuple[str, str]] = []
    for kind, k in PLAN.items():
        cands = []
        for r in recs:
            v = r.judge.get(kind)
            # Skip unscored verdicts, deterministic zeros and mock verdicts (they carry "note").
            if isinstance(v, dict) and v.get("score") is not None and "note" not in v:
                cands.append(r.scenario_id)
        # Spread picks across the candidate list rather than taking the first k.
        step = max(1, len(cands) // k) if cands else 1
        picked += [(sid, kind) for sid in cands[::step][:k]]
    return picked[:N_LABELS]


def write_sheet(tag: str, force: bool = False) -> int:
    from evals.report import load_run

    if (
        LABELS_PATH.exists()
        and any(x.get("human_label") is not None for x in read_labels())
        and not force
    ):
        print(
            f"{LABELS_PATH} already has human labels; pass --force to overwrite.", file=sys.stderr
        )
        return 2
    _, _, recs = load_run(tag)
    by_id = {r.scenario_id: r for r in recs}
    scen = {s.id: s for s in load_scenarios()}
    pairs = select_for_labeling(tag)
    rows = []
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    for i, (sid, kind) in enumerate(pairs, start=1):
        r, s = by_id[sid], scen[sid]
        print(f"\n{'=' * 80}\n[{i}/{len(pairs)}] {sid} — label: {kind.upper()}\n{'=' * 80}")
        print(f"QUESTION: {s.full_text()}")
        if kind == "correctness":
            print("KEY FACTS:\n" + "\n".join(f"  - {f}" for f in s.key_facts))
        if kind == "groundedness":
            for j, c in enumerate(r.retrieved, start=1):
                print(f"--- [S{j}] {c.title}\n{c.text}")
        if kind == "clarification":
            print("DIMENSIONS: " + ", ".join(s.key_facts))
        print(f"\nANSWER:\n{r.answer}")
        rows.append(
            {"scenario_id": sid, "run_tag": tag, "metric": kind, "human_label": None, "notes": ""}
        )
    with LABELS_PATH.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    print(f"\nWrote {len(rows)} label slots to {LABELS_PATH}. Set human_label to true/false.")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tag")
    ap.add_argument("--agreement", action="store_true")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args(argv)
    if args.agreement:
        print(json.dumps(agreement(args.tag), indent=2))
        return 0
    return write_sheet(args.tag, args.force)


if __name__ == "__main__":
    raise SystemExit(main())
