"""Grounded question answering with inline citations and refusal paths.

Flow: retrieve -> confidence gate (refuse before spending tokens) -> generate with numbered
sources -> parse and validate [S#] markers -> RagAnswer.
"""

from __future__ import annotations

import re
import time
from typing import Any

from core.config import Settings
from core.llm import LLMClient
from rag.prompts import INSUFFICIENT, PROMPTS, build_user_prompt, format_sources
from rag.retriever import Retriever
from rag.schemas import Citation, RagAnswer, RetrievedChunk

_MARKER = re.compile(r"\[S(\d+)\]")

LOW_CONFIDENCE_MESSAGE = (
    "I couldn't find enough support for that in the Google Cloud documentation I have, so I "
    "won't guess. Could you rephrase, or ask about a specific Google Cloud product or "
    "architecture topic?"
)


class KnowledgeAnswerer:
    def __init__(
        self,
        settings: Settings,
        retriever: Retriever,
        llm: LLMClient,
        prompt_version: str = "v1",
    ) -> None:
        self.settings = settings
        self.retriever = retriever
        self.llm = llm
        self.prompt_version = prompt_version
        self.system_prompt = PROMPTS[prompt_version]

    def retrieve_and_gate(self, question: str) -> tuple[list[RetrievedChunk], float, bool]:
        """Retrieval + low-confidence gate: (chunks, top confidence, passes gate).

        This is the whole pipeline up to the LLM call; the no-network eval baseline uses it.
        """
        retrieved = self.retriever.retrieve(question)
        confidence = max((r.confidence for r in retrieved), default=0.0)
        return retrieved, confidence, confidence >= self.settings.min_confidence

    def answer(
        self,
        question: str,
        model: str | None = None,
        history: list[tuple[str, str]] | None = None,
    ) -> RagAnswer:
        """Answer `question`. `history` is prior (role, content) turns; retrieval uses only
        the current question, the prompt includes the conversation."""
        t0 = time.perf_counter()
        model = model or self.settings.flash_model
        retrieved, confidence, passes_gate = self.retrieve_and_gate(question)

        if not passes_gate:
            return RagAnswer(
                question=question,
                answer=LOW_CONFIDENCE_MESSAGE,
                refused=True,
                refusal_reason="low_retrieval_confidence",
                confidence=confidence,
                retrieved=retrieved,
                latency_ms=(time.perf_counter() - t0) * 1000,
            )

        markers = {f"S{i}": r for i, r in enumerate(retrieved, start=1)}
        sources_block = format_sources(
            [(m, r.chunk.title, r.chunk.section, r.chunk.text) for m, r in markers.items()]
        )
        resp = self.llm.generate(
            build_user_prompt(question, sources_block, history),
            model=model,
            system=self.system_prompt,
        )
        text = resp.text.strip()
        base: dict[str, Any] = dict(
            question=question,
            confidence=confidence,
            model=resp.model,
            retrieved=retrieved,
            input_tokens=resp.input_tokens,
            output_tokens=resp.output_tokens,
            llm_requests=resp.requests,
        )

        if INSUFFICIENT in text:
            return RagAnswer(
                **base,
                answer=LOW_CONFIDENCE_MESSAGE,
                refused=True,
                refusal_reason="model_insufficient_context",
                latency_ms=(time.perf_counter() - t0) * 1000,
            )

        cleaned, citations, invalid = resolve_citations(text, markers)
        return RagAnswer(
            **base,
            answer=cleaned,
            citations=citations,
            invalid_citation_markers=invalid,
            latency_ms=(time.perf_counter() - t0) * 1000,
        )


def resolve_citations(
    text: str, markers: dict[str, RetrievedChunk]
) -> tuple[str, list[Citation], list[str]]:
    """Map [S#] markers to sources; strip markers that point at no source (hallucinated)."""
    used: list[str] = []
    invalid: list[str] = []

    def _sub(m: re.Match[str]) -> str:
        key = f"S{m.group(1)}"
        if key in markers:
            if key not in used:
                used.append(key)
            return m.group(0)
        invalid.append(key)
        return ""

    cleaned = _MARKER.sub(_sub, text)
    cleaned = re.sub(r"[ \t]+([.,;:])", r"\1", cleaned)  # tidy spaces left by removed markers
    citations = [
        Citation(
            marker=key,
            chunk_id=markers[key].chunk.chunk_id,
            title=markers[key].chunk.title,
            url=markers[key].chunk.url,
            section=markers[key].chunk.section,
            snippet=_snippet(markers[key].chunk.text),
        )
        for key in used
    ]
    return cleaned, citations, invalid


def _snippet(text: str, n: int = 240) -> str:
    flat = " ".join(text.split())
    return flat if len(flat) <= n else flat[: n - 1].rsplit(" ", 1)[0] + "…"
