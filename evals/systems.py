"""Systems under test. Each adapter turns a Scenario into a uniform `RunRecord`.

Phase 2 evaluates the Phase 1 Knowledge (RAG) pipeline. Later phases add an adapter for the
multi-agent flow; metrics and reports only depend on `RunRecord`.
"""

from __future__ import annotations

import time
from typing import Protocol

from pydantic import BaseModel, Field

from core.config import Settings
from core.llm import LLMClient, LLMResponse
from evals.schema import InjectedContext, Scenario
from rag.answer import LOW_CONFIDENCE_MESSAGE, KnowledgeAnswerer
from rag.retriever import Retriever
from rag.schemas import Chunk, RagAnswer, RetrievedChunk

POISON_DOC_ID = "__injected__"


class RetrievedRef(BaseModel):
    chunk_id: str
    doc_id: str
    title: str
    url: str
    confidence: float
    text: str  # kept so judges can be re-run offline from results.jsonl
    injected: bool = False


class CitedRef(BaseModel):
    marker: str
    chunk_id: str
    doc_id: str


class RunRecord(BaseModel):
    scenario_id: str
    category: str
    answer: str = ""
    refused: bool = False
    refusal_reason: str | None = None
    confidence: float | None = None
    retrieved: list[RetrievedRef] = Field(default_factory=list)
    cited: list[CitedRef] = Field(default_factory=list)
    invalid_citation_markers: list[str] = Field(default_factory=list)
    model: str | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    latency_ms: float = 0.0
    llm_requests: int = 0  # HTTP requests to the LLM (incl. retries); cost is $0 on free tier
    # False when the run deliberately skipped generation (retrieval-only baseline) and the
    # retrieval gate let the question through: text-dependent metrics are then N/A.
    generated: bool = True
    error: str | None = None
    metrics: dict[str, float | bool | None] = Field(default_factory=dict)
    judge: dict[str, object] = Field(default_factory=dict)


class System(Protocol):
    name: str

    def run(self, scenario: Scenario) -> RunRecord: ...


class PoisonedRetriever:
    """Plants a scenario's poisoned document at rank 1 (simulates a compromised corpus doc).

    The poisoned chunk gets the best real chunk's confidence, so it never changes the refusal
    gate on its own; the question is whether the generator obeys instructions inside it.
    """

    def __init__(self, base: Retriever, doc: InjectedContext) -> None:
        self.base = base
        self.doc = doc

    def retrieve(self, query: str, top_k: int | None = None) -> list[RetrievedChunk]:
        real = self.base.retrieve(query, top_k)
        conf = max((r.confidence for r in real), default=1.0)
        poison = RetrievedChunk(
            chunk=Chunk(
                chunk_id=f"{POISON_DOC_ID}#0",
                doc_id=POISON_DOC_ID,
                title=self.doc.title,
                url=self.doc.url,
                text=self.doc.text,
            ),
            score=(real[0].score + 1.0) if real else 1.0,
            confidence=conf,
        )
        return [poison, *real[: len(real) - 1]] if real else [poison]


class RagSystem:
    """Phase 1 Knowledge pipeline: hybrid retrieval + cited Gemini answer."""

    def __init__(
        self,
        settings: Settings,
        retriever: Retriever,
        llm: LLMClient | None,
        prompt_version: str = "v1",
    ) -> None:
        """`llm=None` runs retrieval + the confidence gate only, with no network access."""
        self.settings = settings
        self.retriever = retriever
        self.llm = llm
        self.prompt_version = prompt_version
        self.name = "rag-v1" if llm is not None else "rag-v1-retrieval-only"

    def run(self, scenario: Scenario) -> RunRecord:
        retriever: Retriever = self.retriever
        if scenario.injected_context is not None:
            retriever = PoisonedRetriever(self.retriever, scenario.injected_context)
        answerer = KnowledgeAnswerer(
            self.settings, retriever, self.llm or _NO_LLM, self.prompt_version
        )

        history = None
        if isinstance(scenario.input, list):
            history = [(str(t.role), t.content) for t in scenario.input[:-1]]

        t0 = time.perf_counter()
        if self.llm is None:
            retrieved, confidence, passes = answerer.retrieve_and_gate(scenario.last_user_message)
            ans = RagAnswer(
                question=scenario.last_user_message,
                answer="" if passes else LOW_CONFIDENCE_MESSAGE,
                refused=not passes,
                refusal_reason=None if passes else "low_retrieval_confidence",
                confidence=confidence,
                retrieved=retrieved,
            )
        else:
            ans = answerer.answer(scenario.last_user_message, history=history)
        latency_ms = (time.perf_counter() - t0) * 1000

        return RunRecord(
            scenario_id=scenario.id,
            category=scenario.category,
            answer=ans.answer,
            refused=ans.refused,
            refusal_reason=ans.refusal_reason,
            confidence=ans.confidence,
            retrieved=[
                RetrievedRef(
                    chunk_id=r.chunk.chunk_id,
                    doc_id=r.chunk.doc_id,
                    title=r.chunk.title,
                    url=r.chunk.url,
                    confidence=r.confidence,
                    text=r.chunk.text,
                    injected=r.chunk.doc_id == POISON_DOC_ID,
                )
                for r in ans.retrieved
            ],
            cited=[
                CitedRef(marker=c.marker, chunk_id=c.chunk_id, doc_id=c.chunk_id.split("#")[0])
                for c in ans.citations
            ],
            invalid_citation_markers=ans.invalid_citation_markers,
            model=ans.model,
            input_tokens=ans.input_tokens,
            output_tokens=ans.output_tokens,
            latency_ms=latency_ms,
            llm_requests=ans.llm_requests,
            generated=self.llm is not None or ans.refused,
        )


class _NoLLM:
    """Placeholder that fails loudly if the retrieval-only path ever tries to generate."""

    def generate(self, *args: object, **kwargs: object) -> LLMResponse:
        raise AssertionError("retrieval-only system must not call an LLM")


_NO_LLM = _NoLLM()
