"""Cross-encoder reranking.

The cross-encoder scores (query, passage) jointly, which is much sharper than either BM25 or
bi-encoder similarity. Its logit, passed through a sigmoid, doubles as a calibrated-ish
relevance probability that drives the low-confidence refusal path.
"""

from __future__ import annotations

import math
from typing import Protocol


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


class Reranker(Protocol):
    def score(self, query: str, passages: list[str]) -> list[float]:
        """Return one relevance logit per passage."""
        ...


class CrossEncoderReranker:
    def __init__(self, model_name: str) -> None:
        from fastembed.rerank.cross_encoder import TextCrossEncoder

        self.name = model_name
        self._model = TextCrossEncoder(model_name)

    def score(self, query: str, passages: list[str]) -> list[float]:
        if not passages:
            return []
        return [float(s) for s in self._model.rerank(query, passages, batch_size=32)]
