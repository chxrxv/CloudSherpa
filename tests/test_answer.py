from __future__ import annotations

from core.config import Settings
from core.llm import FakeLLM
from rag.answer import LOW_CONFIDENCE_MESSAGE, KnowledgeAnswerer, resolve_citations
from rag.prompts import INSUFFICIENT
from rag.schemas import RagAnswer
from tests.conftest import KeywordReranker, make_retriever


def _answerer(settings: Settings, reply: str) -> tuple[KnowledgeAnswerer, FakeLLM]:
    llm = FakeLLM(lambda _prompt: reply)
    retriever = make_retriever(settings, reranker=KeywordReranker())
    return KnowledgeAnswerer(settings, retriever, llm), llm


def test_answer_resolves_citations(settings: Settings) -> None:
    ans, llm = _answerer(settings, "Spot VMs get a 30 second notice [S1].")
    out = ans.answer("spot vm preemption notice")
    assert not out.refused
    assert [c.marker for c in out.citations] == ["S1"]
    assert out.citations[0].url == "https://example.test/spot"
    assert out.citations[0].chunk_id == out.retrieved[0].chunk.chunk_id
    # the prompt carried numbered sources and the system prompt
    assert "[S1]" in str(llm.calls[0]["prompt"]) and llm.calls[0]["system"]
    assert llm.calls[0]["model"] == settings.flash_model


def test_hallucinated_markers_are_stripped(settings: Settings) -> None:
    ans, _ = _answerer(settings, "Spot VMs are cheap [S1][S9]. Really [S42].")
    out = ans.answer("spot vm preemption notice")
    assert out.invalid_citation_markers == ["S9", "S42"]
    assert "[S9]" not in out.answer and "[S42]" not in out.answer
    assert out.answer.endswith("Really.")


def test_low_confidence_refuses_without_calling_llm(settings: Settings) -> None:
    ans, llm = _answerer(settings, "should never be used [S1]")
    out = ans.answer("recipe for banana bread")
    assert out.refused and out.refusal_reason == "low_retrieval_confidence"
    assert out.answer == LOW_CONFIDENCE_MESSAGE and out.citations == []
    assert llm.calls == []


def test_model_insufficient_context_refuses(settings: Settings) -> None:
    ans, llm = _answerer(settings, INSUFFICIENT)
    out = ans.answer("spot vm preemption notice")
    assert out.refused and out.refusal_reason == "model_insufficient_context"
    assert len(llm.calls) == 1


def test_answer_records_usage_and_validates_schema(settings: Settings) -> None:
    ans, _ = _answerer(settings, "Regional instances fail over automatically [S1].")
    out = ans.answer("regional cloud sql standby failover")
    assert out.input_tokens > 0 and out.output_tokens > 0
    # round-trips through the Pydantic schema
    assert RagAnswer.model_validate_json(out.model_dump_json()) == out


def test_resolve_citations_dedupes_and_orders(settings: Settings) -> None:
    retrieved = make_retriever(settings).retrieve("cloud storage sql spot")
    markers = {f"S{i}": r for i, r in enumerate(retrieved, start=1)}
    text, cits, invalid = resolve_citations("b [S2] a [S1] b again [S2]", markers)
    assert [c.marker for c in cits] == ["S2", "S1"] and invalid == []
    assert text == "b [S2] a [S1] b again [S2]"
