# CloudSherpa — developer entry points. On Windows use Git Bash (or WSL) with GNU make.
PY ?= $(if $(wildcard .venv/Scripts/python.exe),.venv/Scripts/python,$(if $(wildcard .venv/bin/python),.venv/bin/python,python))
export PYTHONUTF8 := 1

.PHONY: help install ingest index ask test test-all lint fmt typecheck

help:  ## list targets
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*## "}{printf "  %-12s %s\n",$$1,$$2}'

install:  ## create venv and install with dev extras
	python -m venv .venv
	$(PY) -m pip install -U pip
	$(PY) -m pip install -e ".[dev]"

ingest:  ## fetch the GCP docs corpus into data/corpus (already committed; re-run to refresh)
	$(PY) scripts/ingest_corpus.py

index:  ## chunk + embed the corpus into the configured vector store
	$(PY) scripts/build_index.py

ask:  ## ask a question: make ask Q="..."
	$(PY) scripts/ask.py "$(Q)"

test:  ## unit tests (no network, no API key)
	$(PY) -m pytest -m "not integration"

test-all:  ## unit + integration tests (needs `make index`)
	$(PY) -m pytest

lint:  ## ruff lint + format check
	$(PY) -m ruff check .
	$(PY) -m ruff format --check .

fmt:  ## auto-format
	$(PY) -m ruff check --fix .
	$(PY) -m ruff format .

typecheck:  ## mypy
	$(PY) -m mypy core rag scripts
