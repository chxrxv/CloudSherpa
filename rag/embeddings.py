"""Embedding providers.

- `local` (default): fastembed ONNX model (BAAI/bge-small-en-v1.5, 384-d). No API key needed,
  deterministic, runs on CPU — keeps evals reproducible and free.
- `gemini`: Gemini embedding model via google-genai (Developer API or Vertex AI).
- `HashEmbedder`: dependency-free bag-of-words hashing embedder for unit tests.
"""

from __future__ import annotations

import hashlib
import re
from typing import Protocol

import numpy as np

from core.config import Settings


class Embedder(Protocol):
    name: str

    def embed_documents(self, texts: list[str]) -> np.ndarray: ...

    def embed_query(self, text: str) -> np.ndarray: ...


def _normalize(m: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(m, axis=-1, keepdims=True)
    return (m / np.clip(norms, 1e-12, None)).astype(np.float32)


class FastEmbedEmbedder:
    def __init__(self, model_name: str) -> None:
        from fastembed import TextEmbedding

        self.name = model_name
        self._model = TextEmbedding(model_name)

    def embed_documents(self, texts: list[str]) -> np.ndarray:
        return _normalize(np.array(list(self._model.passage_embed(texts, batch_size=64))))

    def embed_query(self, text: str) -> np.ndarray:
        return _normalize(np.array(list(self._model.query_embed([text])))[0])


class GeminiEmbedder:
    BATCH = 100

    def __init__(self, settings: Settings) -> None:
        from core.llm import GeminiClient

        self.name = settings.gemini_embedding_model
        self._client = GeminiClient(settings).raw

    def _embed(self, texts: list[str], task_type: str) -> np.ndarray:
        from google.genai import types

        vecs: list[list[float]] = []
        for i in range(0, len(texts), self.BATCH):
            resp = self._client.models.embed_content(
                model=self.name,
                contents=texts[i : i + self.BATCH],
                config=types.EmbedContentConfig(task_type=task_type),
            )
            vecs.extend(e.values for e in resp.embeddings or [] if e.values is not None)
        return _normalize(np.array(vecs))

    def embed_documents(self, texts: list[str]) -> np.ndarray:
        return self._embed(texts, "RETRIEVAL_DOCUMENT")

    def embed_query(self, text: str) -> np.ndarray:
        return self._embed([text], "RETRIEVAL_QUERY")[0]


class HashEmbedder:
    """Feature-hashed bag of words. Crude, but deterministic and instant for tests."""

    def __init__(self, dim: int = 256) -> None:
        self.name = f"hash-{dim}"
        self.dim = dim

    def _vec(self, text: str) -> np.ndarray:
        v = np.zeros(self.dim, dtype=np.float32)
        for tok in re.findall(r"[a-z0-9]+", text.lower()):
            h = int(hashlib.md5(tok.encode()).hexdigest(), 16)
            v[h % self.dim] += 1.0
        return v

    def embed_documents(self, texts: list[str]) -> np.ndarray:
        return _normalize(np.stack([self._vec(t) for t in texts]))

    def embed_query(self, text: str) -> np.ndarray:
        return _normalize(self._vec(text))


def make_embedder(settings: Settings) -> Embedder:
    if settings.embedding_provider == "local":
        return FastEmbedEmbedder(settings.local_embedding_model)
    if settings.embedding_provider == "gemini":
        return GeminiEmbedder(settings)
    if settings.embedding_provider == "hash":
        return HashEmbedder()
    raise ValueError(f"unknown embedding provider {settings.embedding_provider!r}")
