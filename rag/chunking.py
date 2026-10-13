"""Chunking strategies.

- `fixed`: sliding character window snapped to whitespace. Structure-blind baseline.
- `markdown`: splits on headings, packs paragraphs up to `chunk_size`, and records the heading
  path (e.g. "Pricing > Committed use discounts") on each chunk so it can be cited and
  prepended as retrieval context.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from rag.schemas import Chunk, Document

_HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


def chunk_documents(
    docs: Iterable[Document], strategy: str, chunk_size: int, overlap: int
) -> list[Chunk]:
    out: list[Chunk] = []
    for doc in docs:
        if strategy == "fixed":
            pieces = [("", t) for t in fixed_windows(doc.text, chunk_size, overlap)]
        elif strategy == "markdown":
            pieces = markdown_sections(doc.text, chunk_size, overlap)
        else:
            raise ValueError(f"unknown chunking strategy {strategy!r}")
        for n, (section, text) in enumerate(pieces):
            out.append(
                Chunk(
                    chunk_id=f"{doc.doc_id}#{n}",
                    doc_id=doc.doc_id,
                    title=doc.title,
                    url=doc.url,
                    section=section,
                    text=text,
                )
            )
    return out


def fixed_windows(text: str, size: int, overlap: int) -> list[str]:
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError("require size > 0 and 0 <= overlap < size")
    text = text.strip()
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        if end < len(text):
            # Snap back to the last whitespace so we don't cut words in half.
            ws = text.rfind(" ", start + size // 2, end)
            nl = text.rfind("\n", start + size // 2, end)
            end = max(ws, nl) if max(ws, nl) > start else end
        piece = text[start:end].strip()
        if piece:
            chunks.append(piece)
        if end >= len(text):
            break
        # Start the next window `overlap` chars back, snapped forward to a word boundary.
        nxt = end - overlap
        while nxt < end and not text[nxt - 1].isspace():
            nxt += 1
        start = max(nxt, start + 1)
    return chunks


def markdown_sections(text: str, size: int, overlap: int) -> list[tuple[str, str]]:
    """Return (heading_path, text) pieces; never merges content across headings."""
    sections: list[tuple[list[str], list[str]]] = []
    path: list[tuple[int, str]] = []
    buf: list[str] = []

    def flush() -> None:
        if any(line.strip() for line in buf):
            sections.append(([h for _, h in path], buf.copy()))
        buf.clear()

    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
        m = None if in_code else _HEADING.match(line)
        if m:
            flush()
            level = len(m.group(1))
            path = [(lv, h) for lv, h in path if lv < level] + [(level, m.group(2))]
        else:
            buf.append(line)
    flush()

    out: list[tuple[str, str]] = []
    for heads, lines in sections:
        section = " > ".join(heads)
        body = "\n".join(lines).strip()
        for piece in _pack_paragraphs(body, size, overlap):
            out.append((section, piece))
    return out


def _pack_paragraphs(body: str, size: int, overlap: int) -> list[str]:
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    pieces: list[str] = []
    cur = ""
    for p in paras:
        if len(p) > size:
            if cur:
                pieces.append(cur)
                cur = ""
            pieces.extend(fixed_windows(p, size, overlap))
            continue
        if cur and len(cur) + len(p) + 2 > size:
            pieces.append(cur)
            cur = p
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        pieces.append(cur)
    return pieces


def embedding_text(chunk: Chunk, with_context: bool) -> str:
    """Text actually embedded/indexed. Context headers help short or ambiguous chunks."""
    if not with_context:
        return chunk.text
    header = chunk.title + (f" — {chunk.section}" if chunk.section else "")
    return f"{header}\n\n{chunk.text}"
