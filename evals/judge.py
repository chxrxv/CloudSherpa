"""LLM-as-judge: groundedness, answer correctness and clarification helpfulness.

- Pinned judge model (`JUDGE_MODEL`), deliberately different from the model under test.
- Temperature 0 and structured JSON output validated against the Pydantic schemas below.
- Claim- and fact-level verdicts (not a single 1-10 vibe score), so scores are explainable and
  disagreements with human labels can be traced to a specific claim.
- Judge prompts live here, under evals/, which is never part of the retrieval corpus.
- Backends: Gemini (free tier) or any OpenAI-compatible endpoint such as a local Ollama
  server. Every verdict records backend + model: scores from different judges are not
  comparable. Calls are cached on disk (evals/judge_cache.py) so quota-interrupted runs resume
  without repeating them. A quota-exhaustion error is never swallowed; it stops the run.

Judge scores are reported as UNVALIDATED until judge-vs-human agreement is measured on
evals/judge_labels.jsonl.
"""

from __future__ import annotations

import json
from typing import Literal, Protocol

from pydantic import BaseModel, ValidationError

from core.llm import LLMCallError, LLMClient, QuotaExhaustedError
from evals.judge_cache import JudgeCache
from evals.metrics import behaved_as_refusal
from evals.schema import Scenario
from evals.systems import RunRecord

JUDGE_VERSION = "v1"


# --- structured outputs ------------------------------------------------------------------


class ClaimCheck(BaseModel):
    claim: str
    supported: bool
    evidence: str  # source marker(s) supporting the claim, or "none"


class GroundednessVerdict(BaseModel):
    claims: list[ClaimCheck]
    reasoning: str


class FactCheck(BaseModel):
    fact: str
    status: Literal["covered", "missing", "contradicted"]


class CorrectnessVerdict(BaseModel):
    facts: list[FactCheck]
    reasoning: str


class ClarificationVerdict(BaseModel):
    asks_clarifying_questions: bool
    dimensions_addressed: list[str]
    helpfulness: int  # 1-5, rubric below
    reasoning: str


# --- prompts -----------------------------------------------------------------------------

JUDGE_SYSTEM = (
    "You are a meticulous evaluator of a Google Cloud assistant's answers. Follow the rubric "
    "exactly, judge only what is asked, and respond with JSON matching the schema."
)

GROUNDEDNESS_PROMPT = """\
Rubric — groundedness / faithfulness.
Split the ANSWER into atomic factual claims (ignore greetings, questions to the user and
generic advice that asserts no fact). For each claim decide whether the CONTEXT supports it.
A claim is supported only if the CONTEXT states or directly implies it; prior knowledge does
not count, even if the claim is true. Cite the supporting source marker(s) as `evidence`,
or "none".

CONTEXT:
{context}

ANSWER:
{answer}
"""

CORRECTNESS_PROMPT = """\
Rubric — answer correctness against a reference.
For EACH key fact listed, decide whether the ANSWER covers it (same meaning, wording may
differ), is missing it, or contradicts it. Do not reward facts that are not in the list and
do not penalise extra correct detail.

QUESTION:
{question}

REFERENCE ANSWER:
{reference}

KEY FACTS:
{facts}

ANSWER:
{answer}
"""

CLARIFICATION_PROMPT = """\
Rubric — handling an ambiguous or underspecified request.
The ideal response asks focused clarifying questions about the missing information before
committing to a recommendation (it may also give a brief, clearly conditional overview).
Dimensions worth clarifying: {dimensions}

Helpfulness scale:
5 = asks targeted questions covering most of the important dimensions; no premature commitment
4 = asks useful questions covering several dimensions
3 = asks a generic or single clarifying question, or answers with heavy hedging
2 = commits to a specific recommendation without asking, or the questions are unhelpful
1 = refuses, ignores the request, or is irrelevant

CONVERSATION:
{question}

RESPONSE:
{answer}
"""


def _context_block(rec: RunRecord) -> str:
    return (
        "\n\n".join(f"[S{i}] {r.title}\n{r.text}" for i, r in enumerate(rec.retrieved, start=1))
        or "(no context retrieved)"
    )


def _conversation(sc: Scenario) -> str:
    if isinstance(sc.input, str):
        return f"User: {sc.input}"
    return "\n".join(f"{t.role.capitalize()}: {t.content}" for t in sc.input)


# --- judges ------------------------------------------------------------------------------


class Judge(Protocol):
    model: str
    backend: str

    def judge(self, rec: RunRecord, sc: Scenario) -> dict[str, object]: ...


def applicable_judgements(rec: RunRecord, sc: Scenario) -> list[str]:
    """Which rubrics apply. Wrong refusals are scored deterministically, not sent to the judge."""
    if rec.error:
        return []
    out: list[str] = []
    answered = not behaved_as_refusal(rec)
    if sc.expects_clarification:
        out.append("clarification")
    elif not sc.should_refuse and sc.key_facts:
        out.append("correctness")
    if answered and not sc.should_refuse and not sc.expects_clarification and rec.retrieved:
        out.append("groundedness")
    return out


class LLMJudge:
    def __init__(
        self, llm: LLMClient, model: str, backend: str, cache: JudgeCache | None = None
    ) -> None:
        self.llm = llm
        self.model = model
        self.backend = backend
        self.cache = cache

    def _ask(self, prompt: str, schema: type[BaseModel]) -> tuple[BaseModel, dict[str, int]]:
        key = JudgeCache.key(
            backend=self.backend,
            model=self.model,
            system=JUDGE_SYSTEM,
            prompt=prompt,
            schema=json.dumps(schema.model_json_schema(), sort_keys=True),
            temperature=0.0,
        )
        if self.cache is not None and (hit := self.cache.get(key)) is not None:
            usage = {"requests": 0, "cache_hits": 1, "in": 0, "out": 0}
            return schema.model_validate_json(hit["text"]), usage
        resp = self.llm.generate(
            prompt,
            model=self.model,
            system=JUDGE_SYSTEM,
            temperature=0.0,
            response_schema=schema,
        )
        verdict = schema.model_validate_json(resp.text)  # only valid verdicts get cached
        if self.cache is not None:
            self.cache.put(
                key,
                {
                    "text": resp.text,
                    "model": self.model,
                    "backend": self.backend,
                    "input_tokens": resp.input_tokens,
                    "output_tokens": resp.output_tokens,
                },
            )
        usage = {
            "requests": resp.requests,
            "cache_hits": 0,
            "in": resp.input_tokens,
            "out": resp.output_tokens,
        }
        return verdict, usage

    def judge(self, rec: RunRecord, sc: Scenario) -> dict[str, object]:
        result: dict[str, object] = {
            "judge_backend": self.backend,
            "judge_model": self.model,
            "judge_version": JUDGE_VERSION,
        }
        totals = {"requests": 0, "cache_hits": 0, "in": 0, "out": 0}
        for kind in applicable_judgements(rec, sc):
            try:
                if kind == "correctness":
                    if behaved_as_refusal(rec):
                        # Should have answered but refused: deterministic zero, no judge call.
                        result["correctness"] = {"score": 0.0, "note": "refused"}
                        continue
                    v, usage = self._ask(
                        CORRECTNESS_PROMPT.format(
                            question=_conversation(sc),
                            reference=sc.expected,
                            facts="\n".join(f"- {f}" for f in sc.key_facts),
                            answer=rec.answer,
                        ),
                        CorrectnessVerdict,
                    )
                    assert isinstance(v, CorrectnessVerdict)
                    result["correctness"] = score_correctness(v)
                elif kind == "groundedness":
                    v, usage = self._ask(
                        GROUNDEDNESS_PROMPT.format(context=_context_block(rec), answer=rec.answer),
                        GroundednessVerdict,
                    )
                    assert isinstance(v, GroundednessVerdict)
                    result["groundedness"] = score_groundedness(v)
                else:
                    v, usage = self._ask(
                        CLARIFICATION_PROMPT.format(
                            dimensions=", ".join(sc.key_facts),
                            question=_conversation(sc),
                            answer=rec.answer,
                        ),
                        ClarificationVerdict,
                    )
                    assert isinstance(v, ClarificationVerdict)
                    result["clarification"] = score_clarification(v)
                totals = {k: totals[k] + usage[k] for k in totals}
            except QuotaExhaustedError:
                raise  # the runner stops cleanly; the cache keeps what was already judged
            except (LLMCallError, ValidationError, ValueError) as exc:
                result[kind] = {"score": None, "error": str(exc)[:300]}
        result.update(
            judge_requests=totals["requests"],
            judge_cache_hits=totals["cache_hits"],
            judge_input_tokens=totals["in"],
            judge_output_tokens=totals["out"],
        )
        return result


def score_groundedness(v: GroundednessVerdict) -> dict[str, object]:
    n = len(v.claims)
    supported = sum(c.supported for c in v.claims)
    return {
        "score": supported / n if n else None,  # no factual claims -> not applicable
        "claims": n,
        "unsupported": [c.claim for c in v.claims if not c.supported],
        "reasoning": v.reasoning,
    }


def score_correctness(v: CorrectnessVerdict) -> dict[str, object]:
    n = len(v.facts)
    covered = sum(f.status == "covered" for f in v.facts)
    contradicted = [f.fact for f in v.facts if f.status == "contradicted"]
    return {
        "score": covered / n if n else None,
        "missing": [f.fact for f in v.facts if f.status == "missing"],
        "contradicted": contradicted,
        "reasoning": v.reasoning,
    }


def score_clarification(v: ClarificationVerdict) -> dict[str, object]:
    h = min(5, max(1, v.helpfulness))
    return {
        "score": (h - 1) / 4,  # normalised 0..1 for aggregation
        "helpfulness_1to5": h,
        "asks_clarifying_questions": v.asks_clarifying_questions,
        "dimensions_addressed": v.dimensions_addressed,
        "reasoning": v.reasoning,
    }


class MockJudge:
    """For CI smoke runs only: exercises the plumbing, produces NO quality signal."""

    model = "mock-judge"
    backend = "mock"

    def judge(self, rec: RunRecord, sc: Scenario) -> dict[str, object]:
        out: dict[str, object] = {
            "judge_backend": self.backend,
            "judge_model": self.model,
            "judge_version": JUDGE_VERSION,
        }
        for kind in applicable_judgements(rec, sc):
            out[kind] = {"score": 0.5, "note": "mock"}
        out.update(
            judge_requests=0, judge_cache_hits=0, judge_input_tokens=0, judge_output_tokens=0
        )
        return out
