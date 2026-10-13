# Corpus attribution

The Markdown files in `docs/` are extracts of Google Cloud documentation pages, fetched by
`scripts/ingest_corpus.py` from the URLs in `rag/sources.yaml`. Each file's front matter
records its source URL and fetch time.

Google Cloud documentation content is licensed under the
[Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and
code samples under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
Content has been converted from HTML to Markdown, and navigation and feedback widgets
were removed; it is otherwise unmodified. Google is not affiliated with this project and does not endorse it.

The snapshot is committed so that evaluation results are reproducible even as the live docs change.
Run `make ingest` to refresh it.
