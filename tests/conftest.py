from __future__ import annotations

from pathlib import Path

import pytest

from core.config import Settings
from rag.bm25 import tokenize
from rag.chunking import chunk_documents
from rag.embeddings import HashEmbedder
from rag.retriever import HybridRetriever
from rag.schemas import Document
from rag.vectorstores import FaissStore

DOCS = [
    Document(
        doc_id="spot",
        title="Spot VMs",
        url="https://example.test/spot",
        category="cost",
        text=(
            "# Spot VMs\n\nSpot VMs are excess Compute Engine capacity offered at a steep "
            "discount. Compute Engine might preempt Spot VMs at any time to reclaim capacity.\n\n"
            "## Preemption\n\nWhen preempted, a Spot VM receives a 30 second preemption notice. "
            "Use Spot VMs for fault-tolerant batch workloads."
        ),
    ),
    Document(
        doc_id="sql",
        title="Cloud SQL overview",
        url="https://example.test/sql",
        category="database",
        text=(
            "# Cloud SQL\n\nCloud SQL is a fully managed relational database service for MySQL, "
            "PostgreSQL and SQL Server.\n\n## High availability\n\nA regional Cloud SQL "
            "instance has a primary and a standby in different zones with synchronous "
            "replication and automatic failover."
        ),
    ),
    Document(
        doc_id="gcs",
        title="Storage classes",
        url="https://example.test/gcs",
        category="storage",
        text=(
            "# Storage classes\n\nCloud Storage offers Standard, Nearline, Coldline and Archive "
            "storage classes. Archive storage is the lowest-cost class for data accessed less "
            "than once a year, with a 365 day minimum storage duration."
        ),
    ),
]


class KeywordReranker:
    """Fake cross-encoder: logit grows with query-term overlap."""

    def score(self, query: str, passages: list[str]) -> list[float]:
        q = set(tokenize(query))
        return [float(len(q & set(tokenize(p)))) * 2.0 - 3.0 for p in passages]


def make_settings(tmp_path: Path, **overrides: object) -> Settings:
    base: dict[str, object] = {
        "data_dir": tmp_path,
        "gemini_api_key": None,
        "chunking_strategy": "markdown",
        "chunk_size": 400,
        "chunk_overlap": 50,
        "candidate_k": 10,
        "top_k": 3,
    }
    base.update(overrides)
    return Settings(_env_file=None, **base)  # type: ignore[call-arg]


def make_retriever(settings: Settings, reranker: object | None = None) -> HybridRetriever:
    chunks = chunk_documents(
        DOCS, settings.chunking_strategy, settings.chunk_size, settings.chunk_overlap
    )
    emb = HashEmbedder()
    store = FaissStore(emb.dim)
    store.add([c.chunk_id for c in chunks], emb.embed_documents([c.text for c in chunks]))
    return HybridRetriever(settings, chunks, store, emb, reranker)  # type: ignore[arg-type]


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    return make_settings(tmp_path)
