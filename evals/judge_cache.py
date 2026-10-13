"""Resumable on-disk cache of judge calls.

Key = SHA-256 over (backend, model, system prompt, user prompt, response schema, temperature),
so a run interrupted by a quota resumes without repeating any judge call, while changing the
judge model, backend, rubric or schema can never return a stale verdict. Only responses that
validated against the schema are stored. Entries are written atomically (temp file + rename),
so a crash mid-write cannot leave a corrupt entry.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
from typing import Any


class JudgeCache:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.hits = 0
        self.misses = 0

    @staticmethod
    def key(
        *, backend: str, model: str, system: str, prompt: str, schema: str, temperature: float
    ) -> str:
        payload = json.dumps(
            {
                "backend": backend,
                "model": model,
                "system": system,
                "prompt": prompt,
                "schema": schema,
                "temperature": temperature,
            },
            sort_keys=True,
            ensure_ascii=False,
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def _path(self, key: str) -> Path:
        return self.root / key[:2] / f"{key}.json"

    def get(self, key: str) -> dict[str, Any] | None:
        p = self._path(key)
        if not p.exists():
            self.misses += 1
            return None
        self.hits += 1
        data: dict[str, Any] = json.loads(p.read_text(encoding="utf-8"))
        return data

    def put(self, key: str, value: dict[str, Any]) -> None:
        p = self._path(key)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_suffix(".tmp")
        record = {**value, "cached_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds")}
        tmp.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
        os.replace(tmp, p)
