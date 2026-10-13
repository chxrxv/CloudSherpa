# CloudSherpa — developer entry points. On Windows use Git Bash (or WSL) with GNU make.
PY ?= $(if $(wildcard .venv/Scripts/python.exe),.venv/Scripts/python,$(if $(wildcard .venv/bin/python),.venv/bin/python,python))
export PYTHONUTF8 := 1

.PHONY: help install ingest index ask test test-all lint fmt typecheck eval eval-subset eval-smoke report labels

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
	$(PY) -m mypy core rag scripts evals

TAG ?= baseline
N ?= 10

eval:  ## full golden-set eval (costs API credits): make eval TAG=baseline
	$(PY) -m evals.run --tag $(TAG)

eval-subset:  ## stratified subset: make eval-subset N=10 TAG=quick
	$(PY) -m evals.run --tag $(TAG) --subset $(N)

eval-smoke:  ## 5-scenario smoke eval with a mocked model (free; what CI runs)
	EMBEDDING_PROVIDER=hash RERANKER=none $(PY) scripts/build_index.py
	EMBEDDING_PROVIDER=hash RERANKER=none $(PY) -m evals.run --tag ci-smoke --smoke --mock --force
	$(PY) -m evals.report ci-smoke

report:  ## markdown report: make report TAG=x [BASE=y]
	$(PY) -m evals.report $(TAG) $(if $(BASE),--compare $(BASE))

labels:  ## print a blind labeling sheet for judge validation: make labels TAG=baseline
	$(PY) -m evals.labels $(TAG)
