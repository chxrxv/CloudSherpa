"""Build and load the retrieval index (chunk store + vector store).

Layout of `settings.index_dir`:
    chunks.jsonl   one Chunk per line (source of truth for text + citation metadata)
    meta.json      embedder, dim, chunking config, corpus size
    faiss.index    (faiss backend only)
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from core.config import Settings
from rag.chunking import chunk_documents, embedding_text
from rag.embeddings import Embedder, make_embedder
from rag.ingest import load_corpus
from rag.schemas import Chunk
from rag.vectorstores import new_vector_store


def build_index(settings: Settings, embedder: Embedder | None = None) -> dict[str, object]:
    t0 = time.perf_counter()
    docs = load_corpus(settings.corpus_dir)
    if not docs:
        raise RuntimeError(
            f"No documents in {settings.corpus_dir / 'docs'} — run scripts/ingest_corpus.py first."
        )
    chunks = chunk_documents(
        docs, settings.chunking_strategy, settings.chunk_size, settings.chunk_overlap
    )
    embedder = embedder or make_embedder(settings)
    vectors = embedder.embed_documents(
        [embedding_text(c, settings.contextual_headers) for c in chunks]
    )
    store = new_vector_store(settings, int(vectors.shape[1]))
    store.add([c.chunk_id for c in chunks], vectors)

    out = settings.index_dir
    store.save(out)
    write_chunks(out / "chunks.jsonl", chunks)
    meta = {
        "embedder": embedder.name,
        "dim": int(vectors.shape[1]),
        "documents": len(docs),
        "chunks": len(chunks),
        "chunking_strategy": settings.chunking_strategy,
        "chunk_size": settings.chunk_size,
        "chunk_overlap": settings.chunk_overlap,
        "contextual_headers": settings.contextual_headers,
        "vector_store": settings.vector_store,
        "build_seconds": round(time.perf_counter() - t0, 1),
    }
    (out / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return meta


def write_chunks(path: Path, chunks: list[Chunk]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(c.model_dump_json() + "\n")


def read_chunks(path: Path) -> list[Chunk]:
    with path.open(encoding="utf-8") as f:
        return [Chunk.model_validate_json(line) for line in f if line.strip()]
