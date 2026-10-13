"""BM25 keyword index. Catches exact product/SKU terms ("n2-standard-4", "CUD") that dense
embeddings blur together."""

from __future__ import annotations

import re

from rank_bm25 import BM25Okapi

_STOP = frozenset(
    (
        "a an and are as at be by can do does for from how i if in is it its of on or that the "
        "this to was what when where which who why will with you your we our should my me"
    ).split()
)
_TOKEN = re.compile(r"[a-z0-9]+(?:[-_.][a-z0-9]+)*")


def tokenize(text: str) -> list[str]:
    """Lowercase tokens; compound terms are kept whole *and* split into parts."""
    out: list[str] = []
    for tok in _TOKEN.findall(text.lower()):
        if tok in _STOP:
            continue
        out.append(tok)
        parts = re.split(r"[-_.]", tok)
        if len(parts) > 1:
            out.extend(p for p in parts if p and p not in _STOP)
    return out


class BM25Index:
    def __init__(self, ids: list[str], texts: list[str]) -> None:
        self._ids = ids
        self._bm25 = BM25Okapi([tokenize(t) or ["_"] for t in texts])

    def search(self, query: str, k: int) -> list[tuple[str, float]]:
        q = tokenize(query)
        if not q:
            return []
        scores = self._bm25.get_scores(q)
        order = scores.argsort()[::-1][:k]
        return [(self._ids[i], float(scores[i])) for i in order if scores[i] > 0]
