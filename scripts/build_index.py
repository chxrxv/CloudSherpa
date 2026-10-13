"""Chunk + embed the ingested corpus into the configured vector store.

python scripts/build_index.py
CHUNKING_STRATEGY=markdown python scripts/build_index.py   # variant index, separate dir
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.config import get_settings
from rag.index import build_index


def main() -> int:
    s = get_settings()
    meta = build_index(s)
    print(f"index written to {s.index_dir}")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
