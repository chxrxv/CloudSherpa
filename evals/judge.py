"""LLM-as-judge: groundedness, answer correctness and clarification helpfulness.

- Pinned judge model (`JUDGE_MODEL`), deliberately different from the model under test.
- Temperature 0 and structured JSON output validated against the Pydantic schemas below.
- Claim- and fact-level verdicts (not a single 1-10 vibe score), so scores are explainable and
  disagreements with human labels can be traced to a specific claim.
- Judge prompts live here, under evals/, which is never part of the retrieval corpus.

Judge scores are reported as UNVALIDATED until judge-vs-human agreement is measured on
evals/judge_labels.jsonl.
"""

from __future__ import annotations

from typing import Literal, Protocol

from pydantic import BaseModel, ValidationError

from core.llm import LLMCallError, LLMClient
from core.pricing import PriceTable
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
    def __init__(self, llm: LLMClient, model: str, prices: PriceTable) -> None:
        self.llm = llm
        self.model = model
        self.prices = prices

    def _ask(self, prompt: str, schema: type[BaseModel]) -> tuple[BaseModel, int, int]:
        resp = self.llm.generate(
            prompt,
            model=self.model,
            system=JUDGE_SYSTEM,
            temperature=0.0,
            response_schema=schema,
        )
        return schema.model_validate_json(resp.text), resp.input_tokens, resp.output_tokens

    def judge(self, rec: RunRecord, sc: Scenario) -> dict[str, object]:
        result: dict[str, object] = {"judge_model": self.model, "judge_version": JUDGE_VERSION}
        tin = tout = 0
        for kind in applicable_judgements(rec, sc):
            try:
                if kind == "correctness":
                    if behaved_as_refusal(rec):
                        # Should have answered but refused: deterministic zero, no judge call.
                        result["correctness"] = {"score": 0.0, "note": "refused"}
                        continue
                    v, i, o = self._ask(
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
                    v, i, o = self._ask(
                        GROUNDEDNESS_PROMPT.format(context=_context_block(rec), answer=rec.answer),
                        GroundednessVerdict,
                    )
                    assert isinstance(v, GroundednessVerdict)
                    result["groundedness"] = score_groundedness(v)
                else:
                    v, i, o = self._ask(
                        CLARIFICATION_PROMPT.format(
                            dimensions=", ".join(sc.key_facts),
                            question=_conversation(sc),
                            answer=rec.answer,
                        ),
                        ClarificationVerdict,
                    )
                    assert isinstance(v, ClarificationVerdict)
                    result["clarification"] = score_clarification(v)
                tin, tout = tin + i, tout + o
            except (LLMCallError, ValidationError, ValueError) as exc:
                result[kind] = {"score": None, "error": str(exc)[:300]}
        result["judge_input_tokens"] = tin
        result["judge_output_tokens"] = tout
        result["judge_cost_usd"] = self.prices.cost_usd(self.model, tin, tout)
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

    def judge(self, rec: RunRecord, sc: Scenario) -> dict[str, object]:
        out: dict[str, object] = {"judge_model": self.model, "judge_version": JUDGE_VERSION}
        for kind in applicable_judgements(rec, sc):
            out[kind] = {"score": 0.5, "note": "mock"}
        out.update(judge_input_tokens=0, judge_output_tokens=0, judge_cost_usd=0.0)
        return out
