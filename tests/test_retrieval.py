from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from core.config import Settings
from rag.bm25 import BM25Index, tokenize
from rag.embeddings import HashEmbedder
from rag.index import build_index, read_chunks
from rag.ingest import write_document
from rag.reranker import sigmoid
from rag.retriever import HybridRetriever, reciprocal_rank_fusion
from rag.vectorstores import FaissStore
from tests.conftest import DOCS, KeywordReranker, make_retriever, make_settings


def test_tokenize_keeps_compound_terms_and_parts() -> None:
    toks = tokenize("Use an n2-standard-4 VM for the API")
    assert "n2-standard-4" in toks and "standard" in toks and "n2" in toks
    assert "the" not in toks and "an" not in toks


def test_bm25_ranks_exact_term_first() -> None:
    idx = BM25Index(["a", "b", "c"], ["spot vm preemption", "cloud sql database", "archive"])
    assert idx.search("preemption notice", 3)[0][0] == "a"
    assert idx.search("the of and", 3) == []  # stopwords only


def test_rrf_math() -> None:
    fused = dict(reciprocal_rank_fusion([["a", "b"], ["b", "c"]], k=60))
    assert fused["b"] == pytest.approx(1 / 62 + 1 / 61)
    assert fused["a"] == pytest.approx(1 / 61)
    assert max(fused, key=fused.__getitem__) == "b"  # in both lists -> wins


def test_faiss_store_search_and_roundtrip(tmp_path: Path) -> None:
    emb = HashEmbedder(64)
    vecs = emb.embed_documents(["alpha beta", "gamma delta", "alpha gamma"])
    store = FaissStore(64)
    store.add(["x", "y", "z"], vecs)
    hits = store.search(emb.embed_query("alpha beta"), 2)
    assert hits[0][0] == "x" and hits[0][1] == pytest.approx(1.0, abs=1e-5)
    store.save(tmp_path)
    loaded = FaissStore.load(tmp_path)
    assert loaded.search(emb.embed_query("alpha beta"), 1)[0][0] == "x"


def test_faiss_rejects_wrong_dim() -> None:
    with pytest.raises(ValueError):
        FaissStore(8).add(["a"], np.zeros((1, 4), dtype=np.float32))


@pytest.mark.parametrize("mode", ["dense", "bm25", "hybrid"])
def test_retrieval_modes_find_relevant_doc(settings: Settings, mode: str) -> None:
    s = settings.model_copy(update={"retrieval_mode": mode, "reranker": "none"})
    r = make_retriever(s)
    top = r.retrieve("spot vm preemption notice")
    assert top[0].chunk.doc_id == "spot"


def test_hybrid_records_component_ranks(settings: Settings) -> None:
    r = make_retriever(settings)
    top = r.retrieve("archive storage class minimum duration")[0]
    assert top.chunk.doc_id == "gcs"
    assert top.dense_rank is not None and top.bm25_rank is not None


def test_reranker_orders_and_sets_confidence(settings: Settings) -> None:
    r = make_retriever(settings, reranker=KeywordReranker())
    res = r.retrieve("regional cloud sql standby failover")
    assert res[0].chunk.doc_id == "sql"
    assert [x.score for x in res] == sorted((x.score for x in res), reverse=True)
    for x in res:
        assert x.confidence == pytest.approx(sigmoid(x.score))


def test_reranker_low_confidence_for_unrelated_query(settings: Settings) -> None:
    r = make_retriever(settings, reranker=KeywordReranker())
    res = r.retrieve("recipe for banana bread")
    assert max(x.confidence for x in res) < 0.1


def test_bm25_only_never_reports_low_confidence(settings: Settings) -> None:
    s = settings.model_copy(update={"retrieval_mode": "bm25", "reranker": "none"})
    assert all(x.confidence == 1.0 for x in make_retriever(s).retrieve("cloud sql"))


def test_top_k_respected(settings: Settings) -> None:
    assert len(make_retriever(settings).retrieve("cloud", top_k=2)) <= 2


def test_build_index_end_to_end(tmp_path: Path) -> None:
    s = make_settings(tmp_path)
    for d in DOCS:
        write_document(d, s.corpus_dir / "docs", "2026-01-01T00:00:00+00:00")
    meta = build_index(s, embedder=HashEmbedder())
    assert meta["documents"] == 3 and meta["chunks"] > 3
    chunks = read_chunks(s.index_dir / "chunks.jsonl")
    assert len(chunks) == meta["chunks"]
    store = FaissStore.load(s.index_dir)
    r = HybridRetriever(s, chunks, store, HashEmbedder(), None)
    assert r.retrieve("spot preemption")[0].chunk.doc_id == "spot"


def test_build_index_without_corpus_errors(tmp_path: Path) -> None:
    with pytest.raises(RuntimeError, match="ingest_corpus"):
        build_index(make_settings(tmp_path), embedder=HashEmbedder())


def test_index_dir_varies_with_chunking(tmp_path: Path) -> None:
    a = make_settings(tmp_path, chunking_strategy="fixed")
    b = make_settings(tmp_path, chunking_strategy="markdown")
    c = make_settings(tmp_path, chunking_strategy="markdown", contextual_headers=True)
    assert len({a.index_dir, b.index_dir, c.index_dir}) == 3
