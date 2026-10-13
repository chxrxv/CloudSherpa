"""Hybrid retriever: dense + BM25 candidates -> reciprocal rank fusion -> cross-encoder rerank.

Each stage is switchable from config (`retrieval_mode`, `reranker`) so evals can ablate them.
"""

from __future__ import annotations

from typing import Protocol

from core.config import Settings
from rag.bm25 import BM25Index
from rag.chunking import embedding_text
from rag.embeddings import Embedder, make_embedder
from rag.index import read_chunks
from rag.reranker import CrossEncoderReranker, Reranker, sigmoid
from rag.schemas import Chunk, RetrievedChunk
from rag.vectorstores import VectorStore, load_vector_store


class Retriever(Protocol):
    def retrieve(self, query: str, top_k: int | None = None) -> list[RetrievedChunk]: ...


def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
    """Standard RRF: score(d) = sum over rankings of 1 / (k + rank)."""
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)


class HybridRetriever:
    def __init__(
        self,
        settings: Settings,
        chunks: list[Chunk],
        vector_store: VectorStore | None,
        embedder: Embedder | None,
        reranker: Reranker | None,
    ) -> None:
        self.settings = settings
        self.chunks = {c.chunk_id: c for c in chunks}
        self.vector_store = vector_store
        self.embedder = embedder
        self.reranker = reranker
        ids = [c.chunk_id for c in chunks]
        self.bm25 = BM25Index(ids, [embedding_text(c, True) for c in chunks])

    @classmethod
    def from_settings(cls, settings: Settings) -> HybridRetriever:
        index_dir = settings.index_dir
        if not (index_dir / "chunks.jsonl").exists():
            raise RuntimeError(f"No index at {index_dir} — run scripts/build_index.py first.")
        chunks = read_chunks(index_dir / "chunks.jsonl")
        need_dense = settings.retrieval_mode in ("dense", "hybrid")
        store = load_vector_store(settings, index_dir) if need_dense else None
        embedder = make_embedder(settings) if need_dense else None
        reranker = (
            CrossEncoderReranker(settings.reranker_model)
            if settings.reranker == "cross-encoder"
            else None
        )
        return cls(settings, chunks, store, embedder, reranker)

    def retrieve(self, query: str, top_k: int | None = None) -> list[RetrievedChunk]:
        s = self.settings
        top_k = top_k or s.top_k
        dense: list[tuple[str, float]] = []
        sparse: list[tuple[str, float]] = []
        if s.retrieval_mode in ("dense", "hybrid"):
            assert self.vector_store is not None and self.embedder is not None
            dense = self.vector_store.search(self.embedder.embed_query(query), s.candidate_k)
        if s.retrieval_mode in ("bm25", "hybrid"):
            sparse = self.bm25.search(query, s.candidate_k)

        dense_rank = {cid: r for r, (cid, _) in enumerate(dense, start=1)}
        dense_sim = dict(dense)
        bm25_rank = {cid: r for r, (cid, _) in enumerate(sparse, start=1)}
        fused = reciprocal_rank_fusion([[c for c, _ in dense], [c for c, _ in sparse]], k=s.rrf_k)[
            : s.candidate_k
        ]
        candidates = [self.chunks[cid] for cid, _ in fused if cid in self.chunks]

        if self.reranker is not None and candidates:
            logits = self.reranker.score(query, [embedding_text(c, True) for c in candidates])
            scored = sorted(zip(candidates, logits, strict=True), key=lambda x: x[1], reverse=True)
            results = [
                RetrievedChunk(
                    chunk=c,
                    score=logit,
                    confidence=sigmoid(logit),
                    dense_rank=dense_rank.get(c.chunk_id),
                    bm25_rank=bm25_rank.get(c.chunk_id),
                )
                for c, logit in scored
            ]
        else:
            fused_score = dict(fused)
            results = [
                RetrievedChunk(
                    chunk=c,
                    score=fused_score[c.chunk_id],
                    # Without a reranker, cosine similarity is the best available signal.
                    # BM25-only mode has no calibrated signal, so it never refuses.
                    confidence=max(0.0, dense_sim.get(c.chunk_id, 0.0)) if dense else 1.0,
                    dense_rank=dense_rank.get(c.chunk_id),
                    bm25_rank=bm25_rank.get(c.chunk_id),
                )
                for c in candidates
            ]
        return results[:top_k]
