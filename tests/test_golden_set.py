"""The golden set must stay valid and consistent with the committed corpus."""

from __future__ import annotations

from collections import Counter

import pytest

from core.config import get_settings
from evals.schema import Scenario, load_scenarios

SCENARIOS = load_scenarios()


def test_fifty_unique_scenarios_with_expected_mix() -> None:
    assert len(SCENARIOS) == 50
    assert len({s.id for s in SCENARIOS}) == 50
    assert Counter(s.category for s in SCENARIOS) == {
        "architecture": 15,
        "multi_hop": 8,
        "ambiguous": 7,
        "out_of_scope": 8,
        "prompt_injection": 7,
        "pii": 5,
    }


def test_required_sources_exist_in_corpus() -> None:
    corpus_ids = {p.stem for p in (get_settings().corpus_dir / "docs").glob("*.md")}
    missing = {s.id: [d for d in s.required_sources if d not in corpus_ids] for s in SCENARIOS}
    assert not {k: v for k, v in missing.items() if v}


@pytest.mark.parametrize("s", SCENARIOS, ids=lambda s: s.id)
def test_category_invariants(s: Scenario) -> None:
    if s.category in ("architecture", "multi_hop"):
        assert s.required_sources and s.key_facts and not s.should_refuse
    if s.category == "multi_hop":
        assert len(s.required_sources) >= 2
    if s.category == "out_of_scope":
        assert s.should_refuse and not s.required_sources
    if s.category == "ambiguous":
        assert s.expects_clarification and not s.should_refuse
    if s.category == "prompt_injection":
        assert s.canary and s.canary.startswith("CANARY-")


def test_injection_mix_covers_direct_and_indirect() -> None:
    kinds = {s.injection_type for s in SCENARIOS if s.category == "prompt_injection"}
    assert {"direct", "indirect_retrieved_doc"} <= kinds


def test_golden_set_not_in_retrieval_corpus() -> None:
    """Scenario text (canaries, references) must never leak into the indexed corpus."""
    corpus = "\n".join(
        p.read_text(encoding="utf-8") for p in (get_settings().corpus_dir / "docs").glob("*.md")
    )
    assert "CANARY-" not in corpus
    for s in SCENARIOS:
        assert s.expected not in corpus
