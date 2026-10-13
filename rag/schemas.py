"""Typed data models shared across ingestion, retrieval and answering."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Document(BaseModel):
    """One ingested source page."""

    doc_id: str
    title: str
    url: str
    category: str = "general"
    text: str  # Markdown body


class Chunk(BaseModel):
    chunk_id: str  # f"{doc_id}#{n}"
    doc_id: str
    title: str
    url: str
    section: str = ""  # nearest heading path, e.g. "Pricing > Committed use"
    text: str


class RetrievedChunk(BaseModel):
    chunk: Chunk
    score: float  # final score used for ordering (rerank score or fused score)
    confidence: float  # 0..1 relevance estimate, used for the refusal path
    dense_rank: int | None = None
    bm25_rank: int | None = None


class Citation(BaseModel):
    marker: str = Field(description="Inline marker used in the answer, e.g. 'S1'.")
    chunk_id: str
    title: str
    url: str
    section: str = ""
    snippet: str


class RagAnswer(BaseModel):
    question: str
    answer: str
    citations: list[Citation] = Field(default_factory=list)
    refused: bool = False
    refusal_reason: str | None = None
    confidence: float = 0.0
    model: str | None = None
    invalid_citation_markers: list[str] = Field(default_factory=list)
    retrieved: list[RetrievedChunk] = Field(default_factory=list)
    input_tokens: int = 0
    output_tokens: int = 0
    llm_requests: int = 0
    latency_ms: float = 0.0
