"""Pluggable vector stores.

- `FaissStore` (default): exact inner-product search over L2-normalised vectors (= cosine).
  The corpus is a few thousand chunks, so a flat index is both exact and fast.
- `VertexVectorSearchStore`: Vertex AI Vector Search. Vectors live in the managed index; chunk
  text and metadata stay in the local chunk store (Vector Search only returns ids). Requires
  the `gcp` extra and a pre-created index + endpoint (see README "Managed backends").
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Protocol

import numpy as np

from core.config import Settings


class VectorStore(Protocol):
    def add(self, ids: list[str], vectors: np.ndarray) -> None: ...

    def search(self, query: np.ndarray, k: int) -> list[tuple[str, float]]: ...

    def save(self, path: Path) -> None: ...


class FaissStore:
    def __init__(self, dim: int) -> None:
        import faiss

        self.dim = dim
        self._index: Any = faiss.IndexFlatIP(dim)
        self._ids: list[str] = []

    def add(self, ids: list[str], vectors: np.ndarray) -> None:
        if vectors.shape[1] != self.dim:
            raise ValueError(f"expected dim {self.dim}, got {vectors.shape[1]}")
        self._index.add(np.ascontiguousarray(vectors, dtype=np.float32))
        self._ids.extend(ids)

    def search(self, query: np.ndarray, k: int) -> list[tuple[str, float]]:
        if not self._ids:
            return []
        q = np.ascontiguousarray(query.reshape(1, -1), dtype=np.float32)
        scores, idx = self._index.search(q, min(k, len(self._ids)))
        return [(self._ids[i], float(s)) for s, i in zip(scores[0], idx[0], strict=True) if i >= 0]

    def save(self, path: Path) -> None:
        import faiss

        path.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self._index, str(path / "faiss.index"))
        (path / "faiss_ids.json").write_text(json.dumps(self._ids), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> FaissStore:
        import faiss

        index = faiss.read_index(str(path / "faiss.index"))
        store = cls(index.d)
        store._index = index
        store._ids = json.loads((path / "faiss_ids.json").read_text(encoding="utf-8"))
        return store


class VertexVectorSearchStore:
    """Vertex AI Vector Search backend (streaming-update index + public endpoint)."""

    def __init__(self, settings: Settings) -> None:
        from google.cloud import aiplatform  # optional dependency: pip install -e .[gcp]

        missing = [
            n
            for n in ("vertex_index_id", "vertex_index_endpoint_id", "vertex_deployed_index_id")
            if not getattr(settings, n)
        ]
        if missing or not settings.google_cloud_project:
            raise ValueError(f"vector_store=vertex requires GOOGLE_CLOUD_PROJECT and {missing}")
        aiplatform.init(
            project=settings.google_cloud_project, location=settings.google_cloud_location
        )
        self._index = aiplatform.MatchingEngineIndex(settings.vertex_index_id)
        self._endpoint = aiplatform.MatchingEngineIndexEndpoint(settings.vertex_index_endpoint_id)
        self._deployed_id = settings.vertex_deployed_index_id

    def add(self, ids: list[str], vectors: np.ndarray) -> None:
        from google.cloud.aiplatform_v1.types import IndexDatapoint

        batch = 500
        for i in range(0, len(ids), batch):
            points = [
                IndexDatapoint(datapoint_id=d, feature_vector=v.tolist())
                for d, v in zip(ids[i : i + batch], vectors[i : i + batch], strict=True)
            ]
            self._index.upsert_datapoints(datapoints=points)

    def search(self, query: np.ndarray, k: int) -> list[tuple[str, float]]:
        res = self._endpoint.find_neighbors(
            deployed_index_id=self._deployed_id, queries=[query.tolist()], num_neighbors=k
        )
        # With DOT_PRODUCT_DISTANCE on normalised vectors, `distance` is the similarity.
        return [(n.id, float(n.distance)) for n in res[0]]

    def save(self, path: Path) -> None:
        # Vectors are persisted server-side; nothing to write locally.
        path.mkdir(parents=True, exist_ok=True)


def load_vector_store(settings: Settings, path: Path) -> VectorStore:
    if settings.vector_store == "faiss":
        return FaissStore.load(path)
    if settings.vector_store == "vertex":
        return VertexVectorSearchStore(settings)
    raise ValueError(f"unknown vector store {settings.vector_store!r}")


def new_vector_store(settings: Settings, dim: int) -> VectorStore:
    if settings.vector_store == "faiss":
        return FaissStore(dim)
    if settings.vector_store == "vertex":
        return VertexVectorSearchStore(settings)
    raise ValueError(f"unknown vector store {settings.vector_store!r}")
