from __future__ import annotations

from pathlib import Path

import pytest

from core.config import Settings
from rag.ingest import Source, html_to_document, load_corpus, read_document, write_document
from tests.conftest import DOCS, make_settings

HTML = """<html><head><title>Spot VMs &nbsp;|&nbsp; Google Cloud Documentation</title></head>
<body><nav>Site nav junk</nav>
<h1 class="devsite-page-title">Spot VMs <button>Stay organized with collections</button></h1>
<div class="devsite-article-body">
<p>Spot VMs are <a href="/x">discounted</a> capacity.</p>
<devsite-feedback>Was this helpful?</devsite-feedback>
<h2>Preemption</h2><p>You get a 30 second notice.</p>
<script>var tracking = 1;</script>
<ul><li>batch</li><li>CI</li></ul>
</div></body></html>"""


def test_html_to_document_extracts_clean_markdown() -> None:
    doc = html_to_document(HTML, Source(id="spot", url="https://x/spot", category="cost"))
    assert doc.title == "Spot VMs"
    assert "## Preemption" in doc.text
    assert "Spot VMs are discounted capacity." in doc.text  # link text kept, href dropped
    assert "- batch" in doc.text
    for junk in ("Was this helpful", "tracking", "Site nav", "Stay organized"):
        assert junk not in doc.text


def test_final_url_used_for_citations() -> None:
    doc = html_to_document(
        HTML, Source(id="s", url="https://old/s", category="c"), final_url="https://new/s"
    )
    assert doc.url == "https://new/s"


def test_document_roundtrip(tmp_path: Path) -> None:
    path = write_document(DOCS[0], tmp_path / "docs", "2026-01-01T00:00:00+00:00")
    assert read_document(path) == DOCS[0]
    assert load_corpus(tmp_path)[0].doc_id == DOCS[0].doc_id


def test_read_document_requires_front_matter(tmp_path: Path) -> None:
    p = tmp_path / "bad.md"
    p.write_text("no header", encoding="utf-8")
    with pytest.raises(ValueError):
        read_document(p)


def test_settings_env_override(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("CHUNKING_STRATEGY", "markdown")
    monkeypatch.setenv("TOP_K", "7")
    s = Settings(_env_file=None, data_dir=tmp_path)  # type: ignore[call-arg]
    assert s.chunking_strategy == "markdown" and s.top_k == 7


def test_settings_reject_invalid_choice(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        make_settings(tmp_path, retrieval_mode="magic")


def test_snapshot_has_no_secrets(tmp_path: Path) -> None:
    s = make_settings(tmp_path, gemini_api_key="sk-secret")
    snap = s.snapshot()
    assert "sk-secret" not in str(snap) and "gemini_api_key" not in snap
    assert s.has_llm_credentials


def test_vertex_mode_requires_project(tmp_path: Path) -> None:
    s = make_settings(tmp_path, google_genai_use_vertexai=True, google_cloud_project=None)
    assert not s.has_llm_credentials
