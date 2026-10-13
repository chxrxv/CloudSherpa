"""Corpus ingestion: fetch GCP doc pages, extract the article body, save as Markdown.

Pages are stored as `data/corpus/docs/<id>.md` with a YAML front-matter header holding the
citation metadata (title, canonical URL, category, fetch time). The processed corpus is
committed so eval runs are reproducible even as the live docs change.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify

from rag.schemas import Document

USER_AGENT = "CloudSherpa-corpus-ingest/0.1 (portfolio project; polite single-threaded fetch)"

# DevSite chrome that sneaks into the article body.
_NOISE_SELECTORS = [
    "script",
    "style",
    "noscript",
    "devsite-feedback",
    "devsite-thumb-rating",
    "devsite-bookmark",
    "devsite-toc",
    "devsite-code-button",
    "button",
    "nav",
    ".devsite-article-meta",
    ".devsite-breadcrumb-list",
    ".devsite-banner",
    "devsite-page-rating",
    ".devsite-hidden",
    "[aria-hidden=true]",
    "devsite-hats-survey",
    ".devsite-nav-buttons",
    "devsite-actions",
]


@dataclass
class Source:
    id: str
    url: str
    category: str


def load_sources(path: Path) -> list[Source]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    return [Source(**s) for s in raw["sources"]]


def html_to_document(html: str, source: Source, final_url: str | None = None) -> Document:
    """Extract title + article body from a DevSite page and convert it to Markdown."""
    soup = BeautifulSoup(html, "html.parser")

    # <title> is "Page name | Google Cloud Documentation"; the <h1> also contains DevSite
    # button labels ("Stay organized with collections…"), so prefer <title>.
    title = ""
    if soup.title:
        title = " ".join(soup.title.get_text(" ").split()).split("|")[0].strip()
    if not title:
        h1 = soup.select_one("h1.devsite-page-title") or soup.find("h1")
        title = h1.get_text(" ", strip=True) if h1 else ""

    body = (
        soup.select_one(".devsite-article-body")
        or soup.find("article")
        or soup.find("main")
        or soup.body
    )
    if body is None:
        raise ValueError(f"No article body found for {source.url}")
    for sel in _NOISE_SELECTORS:
        for el in body.select(sel):
            el.decompose()

    md = markdownify(str(body), heading_style="ATX", bullets="-", strip=["img", "a"])
    md = _clean_markdown(md)
    return Document(
        doc_id=source.id,
        title=title or source.id,
        url=final_url or source.url,
        category=source.category,
        text=md,
    )


def _clean_markdown(md: str) -> str:
    md = md.replace("\xa0", " ")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    # Drop heading anchors / permalink glyphs DevSite appends.
    md = re.sub(r"(#+ .*?)\s*link\s*$", r"\1", md, flags=re.MULTILINE)
    return md.strip() + "\n"


def write_document(doc: Document, out_dir: Path, fetched_at: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    meta = {
        "doc_id": doc.doc_id,
        "title": doc.title,
        "url": doc.url,
        "category": doc.category,
        "fetched_at": fetched_at,
        "license": "CC BY 4.0 (Google Cloud documentation)",
    }
    path = out_dir / f"{doc.doc_id}.md"
    header = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True)
    path.write_text(f"---\n{header}---\n\n{doc.text}", encoding="utf-8")
    return path


def read_document(path: Path) -> Document:
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n\n?(.*)$", raw, flags=re.DOTALL)
    if not m:
        raise ValueError(f"{path} is missing front matter")
    meta = yaml.safe_load(m.group(1))
    return Document(
        doc_id=meta["doc_id"],
        title=meta["title"],
        url=meta["url"],
        category=meta.get("category", "general"),
        text=m.group(2),
    )


def load_corpus(corpus_dir: Path) -> list[Document]:
    docs_dir = corpus_dir / "docs"
    return [read_document(p) for p in sorted(docs_dir.glob("*.md"))]


def ingest(
    sources: list[Source],
    corpus_dir: Path,
    *,
    delay_s: float = 1.0,
    skip_existing: bool = False,
    client: httpx.Client | None = None,
) -> dict[str, list[dict[str, Any]]]:
    """Fetch every source; return a summary with successes and failures."""
    docs_dir = corpus_dir / "docs"
    fetched_at = dt.datetime.now(dt.UTC).isoformat(timespec="seconds")
    ok: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []
    own_client = client is None
    client = client or httpx.Client(
        headers={"User-Agent": USER_AGENT}, follow_redirects=True, timeout=30.0
    )
    try:
        for i, src in enumerate(sources):
            if skip_existing and (docs_dir / f"{src.id}.md").exists():
                continue
            try:
                resp = _get_with_retry(client, src.url)
                doc = html_to_document(resp.text, src, final_url=str(resp.url))
                if len(doc.text) < 500:
                    raise ValueError(f"extracted body too short ({len(doc.text)} chars)")
                write_document(doc, docs_dir, fetched_at)
                ok.append({"id": src.id, "chars": len(doc.text), "title": doc.title})
            except Exception as exc:
                failed.append({"id": src.id, "url": src.url, "error": str(exc)[:200]})
            if delay_s and i < len(sources) - 1:
                time.sleep(delay_s)
    finally:
        if own_client:
            client.close()

    manifest = {
        "fetched_at": fetched_at,
        "documents": [
            read_document(p).model_dump(exclude={"text"}) for p in sorted(docs_dir.glob("*.md"))
        ],
    }
    (corpus_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return {"ok": ok, "failed": failed}


def _get_with_retry(client: httpx.Client, url: str, attempts: int = 3) -> httpx.Response:
    last: Exception | None = None
    for n in range(attempts):
        try:
            resp = client.get(url)
            resp.raise_for_status()
            return resp
        except httpx.HTTPError as exc:
            last = exc
            time.sleep(2**n)
    assert last is not None
    raise last
