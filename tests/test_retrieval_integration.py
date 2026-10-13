"""Retrieval sanity checks against the real corpus + local models (no API key needed).

Requires `make ingest index` first; skipped otherwise. Marked `integration`.
"""

from __future__ import annotations

import pytest

from core.config import Settings
from rag.retriever import HybridRetriever

pytestmark = pytest.mark.integration


@pytest.fixture(scope="module")
def retriever() -> HybridRetriever:
    s = Settings()
    if not (s.index_dir / "chunks.jsonl").exists():
        pytest.skip(f"no index at {s.index_dir}")
    return HybridRetriever.from_settings(s)


@pytest.mark.parametrize(
    "query,expected_doc",
    [
        ("How much notice does a Spot VM get before preemption?", "gce-spot"),
        ("Cloud Storage archive class minimum storage duration", "gcs-storage-classes"),
        ("How do committed use discounts work for Compute Engine?", "gce-cud"),
        ("Cloud SQL high availability failover standby zone", "sql-ha"),
        ("globally consistent horizontally scalable relational database", "spanner-overview"),
    ],
)
def test_known_answers_retrieved(retriever: HybridRetriever, query: str, expected_doc: str) -> None:
    docs = [r.chunk.doc_id for r in retriever.retrieve(query)]
    assert expected_doc in docs[:3], docs


def test_off_topic_query_has_low_confidence(retriever: HybridRetriever) -> None:
    res = retriever.retrieve("What's a good recipe for sourdough bread?")
    assert max(r.confidence for r in res) < retriever.settings.min_confidence
