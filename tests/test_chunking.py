from __future__ import annotations

import pytest

from rag.chunking import chunk_documents, embedding_text, fixed_windows, markdown_sections
from tests.conftest import DOCS


def test_fixed_windows_cover_text_and_respect_size() -> None:
    text = " ".join(f"word{i}" for i in range(500))
    chunks = fixed_windows(text, size=200, overlap=40)
    assert all(len(c) <= 200 for c in chunks)
    assert chunks[0].startswith("word0") and chunks[-1].endswith("word499")
    # every word survives chunking
    seen = set(" ".join(chunks).split())
    assert seen == set(text.split())


def test_fixed_windows_do_not_split_words() -> None:
    text = " ".join(["abcdefghij"] * 100)
    for c in fixed_windows(text, size=105, overlap=20):
        assert all(tok == "abcdefghij" for tok in c.split())


def test_fixed_windows_overlap() -> None:
    text = " ".join(f"w{i}" for i in range(300))
    a, b = fixed_windows(text, size=120, overlap=40)[:2]
    assert set(a.split()) & set(b.split()), "consecutive chunks should overlap"


@pytest.mark.parametrize("size,overlap", [(0, 0), (100, 100), (100, -1)])
def test_fixed_windows_rejects_bad_params(size: int, overlap: int) -> None:
    with pytest.raises(ValueError):
        fixed_windows("abc", size, overlap)


def test_markdown_sections_track_heading_path() -> None:
    md = "# A\n\nintro\n\n## B\n\nbee text\n\n### C\n\nsee text\n\n## D\n\ndee text"
    secs = dict((t, s) for s, t in markdown_sections(md, 500, 50))
    assert secs["intro"] == "A"
    assert secs["bee text"] == "A > B"
    assert secs["see text"] == "A > B > C"
    assert secs["dee text"] == "A > D"  # sibling resets deeper levels


def test_markdown_ignores_headings_inside_code_blocks() -> None:
    md = "# Real\n\n```bash\n# not a heading\necho hi\n```\n\nafter"
    secs = markdown_sections(md, 500, 50)
    assert len(secs) == 1 and secs[0][0] == "Real"
    assert "# not a heading" in secs[0][1]


def test_markdown_never_merges_across_headings() -> None:
    md = "# A\n\nshort a\n\n# B\n\nshort b"
    pieces = markdown_sections(md, 1000, 50)
    assert [t for _, t in pieces] == ["short a", "short b"]


def test_markdown_splits_oversized_paragraphs() -> None:
    md = "# A\n\n" + " ".join(["lorem"] * 400)
    pieces = markdown_sections(md, 300, 30)
    assert len(pieces) > 1 and all(len(t) <= 300 for _, t in pieces)


def test_chunk_documents_ids_and_metadata() -> None:
    chunks = chunk_documents(DOCS, "markdown", 400, 50)
    ids = [c.chunk_id for c in chunks]
    assert len(ids) == len(set(ids))
    spot = [c for c in chunks if c.doc_id == "spot"]
    assert spot[0].chunk_id == "spot#0" and spot[0].url == "https://example.test/spot"
    assert any(c.section == "Spot VMs > Preemption" for c in spot)


def test_unknown_strategy_raises() -> None:
    with pytest.raises(ValueError):
        chunk_documents(DOCS, "semantic", 400, 50)


def test_embedding_text_context_header() -> None:
    c = next(c for c in chunk_documents(DOCS, "markdown", 400, 50) if c.section)
    assert embedding_text(c, False) == c.text
    assert embedding_text(c, True).startswith(f"{c.title} — {c.section}\n\n")
