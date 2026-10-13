"""Fetch the GCP docs corpus listed in rag/sources.yaml into data/corpus/.

python scripts/ingest_corpus.py [--skip-existing] [--only run-overview,gce-spot]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.config import get_settings
from rag.ingest import ingest, load_sources


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skip-existing", action="store_true")
    ap.add_argument("--only", help="comma-separated source ids")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between requests")
    args = ap.parse_args()

    s = get_settings()
    sources = load_sources(s.corpus_sources)
    if args.only:
        wanted = set(args.only.split(","))
        sources = [src for src in sources if src.id in wanted]

    result = ingest(sources, s.corpus_dir, delay_s=args.delay, skip_existing=args.skip_existing)
    for item in result["ok"]:
        print(f"  ok   {item['id']:<34} {item['chars']:>7} chars  {item['title']}")
    for item in result["failed"]:
        print(f"  FAIL {item['id']:<34} {item['error']}")
    print(json.dumps({"ok": len(result["ok"]), "failed": len(result["failed"])}))
    return 1 if result["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
