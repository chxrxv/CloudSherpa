"""Ask the Knowledge (RAG) pipeline a question from the command line.

python scripts/ask.py "When should I use Cloud Spanner instead of Cloud SQL?"
python scripts/ask.py --retrieve-only "spot vm preemption"     # no LLM / API key needed
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.config import get_settings
from rag.retriever import HybridRetriever


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("question")
    ap.add_argument("--retrieve-only", action="store_true")
    args = ap.parse_args()

    s = get_settings()
    retriever = HybridRetriever.from_settings(s)

    if args.retrieve_only:
        for i, r in enumerate(retriever.retrieve(args.question), start=1):
            c = r.chunk
            print(
                f"[S{i}] conf={r.confidence:.3f} score={r.score:.3f} "
                f"dense#{r.dense_rank} bm25#{r.bm25_rank}  {c.chunk_id}"
            )
            print(f"     {c.title} — {c.section}" if c.section else f"     {c.title}")
            print(f"     {' '.join(c.text.split())[:200]}\n")
        return 0

    from core.llm import GeminiClient
    from rag.answer import KnowledgeAnswerer

    ans = KnowledgeAnswerer(s, retriever, GeminiClient(s)).answer(args.question)
    print(ans.answer)
    print()
    for cit in ans.citations:
        section = f" — {cit.section}" if cit.section else ""
        print(f"[{cit.marker}] {cit.title}{section}\n     {cit.url}")
    status = f"refused ({ans.refusal_reason})" if ans.refused else "answered"
    print(
        f"\n{status} | confidence={ans.confidence:.3f} | model={ans.model} | "
        f"tokens in/out={ans.input_tokens}/{ans.output_tokens} | {ans.latency_ms:.0f} ms"
    )
    if ans.invalid_citation_markers:
        print(f"stripped invalid citation markers: {ans.invalid_citation_markers}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
