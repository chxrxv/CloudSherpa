# CloudSherpa evaluation results

Every number in this file comes from a real harness run, saved under `evals/runs/<tag>/`.
Each run directory records the git commit, the config snapshot and the golden-set hash.
The harness and golden set are described in [evals/README.md](evals/README.md).

## Metrics

| Metric | Type | Definition |
|---|---|---|
| Retrieval hit | deterministic | Fraction of `required_sources` present among the retrieved chunks |
| Citation validity | deterministic | Every cited marker points at a chunk that was actually retrieved; no hallucinated markers |
| Citation recall | deterministic | Fraction of `required_sources` the answer cites (a wrong refusal scores 0) |
| Refusal correct | deterministic | Refused (system flag or refusal phrasing) == `should_refuse` |
| Injection resisted | deterministic | The scenario's canary string and any forbidden phrases are absent from the output |
| PII leak-free | deterministic | No PII from the input is echoed; digit runs are compared ignoring separators |
| Asked clarifying Q | deterministic (heuristic) | For ambiguous scenarios: a non-refusal reply that contains a question |
| Groundedness | LLM judge | Share of the answer's atomic claims that the retrieved context supports |
| Correctness | LLM judge | Share of the reference key facts that the answer covers; contradictions are listed |
| Clarification | LLM judge | 1–5 rubric for ambiguous requests, normalized to 0–1 |
| Latency p50 / p95 | measured | End-to-end wall clock per scenario (retrieval + generation) |
| Cost / query | computed | Tokens × the price table in `core/pricing.yaml`. Reported as "unpriced" rather than guessed |

The judge is a pinned model (`JUDGE_MODEL`, default `gemini-3.1-pro-preview`), which is
different from the generator. It runs at temperature 0 with schema-validated JSON verdicts.
Judge metrics stay marked **unvalidated** until judge-vs-human agreement has been measured on
`evals/judge_labels.jsonl`.

## Baseline

**Not run yet.** The full 50-scenario baseline calls the Gemini API, so it is on hold for two
reasons:

1. The golden set is waiting for human review, as requested before spending API credits.
2. No `GEMINI_API_KEY` or Vertex AI credentials are configured in this environment. Without
   them the harness refuses to start and writes no results.

The only run so far is the CI smoke run (`--mock`). It uses a fake model and a fake judge, so it
tests plumbing only and its numbers are deliberately not reported here.
