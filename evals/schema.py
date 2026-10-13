"""Golden-set scenario schema and loader."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, model_validator

EVALS_DIR = Path(__file__).resolve().parent
GOLDEN_PATH = EVALS_DIR / "golden.jsonl"
SMOKE_PATH = EVALS_DIR / "smoke.jsonl"

Category = Literal[
    "architecture", "multi_hop", "ambiguous", "out_of_scope", "prompt_injection", "pii"
]


class Turn(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class InjectedContext(BaseModel):
    """A poisoned document the harness plants at rank 1 of the retrieved set (never indexed)."""

    title: str
    url: str
    text: str


class Scenario(BaseModel):
    id: str
    category: Category
    input: str | list[Turn]
    expected: str
    key_facts: list[str] = Field(default_factory=list)
    required_sources: list[str] = Field(default_factory=list)
    should_refuse: bool = False
    expects_clarification: bool = False
    needs_human_review: bool = False
    review_note: str | None = None
    # prompt injection
    canary: str | None = None
    injection_type: str | None = None
    injected_context: InjectedContext | None = None
    forbidden_phrases: list[str] = Field(default_factory=list)
    # PII
    pii: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _check(self) -> Scenario:
        if self.category == "prompt_injection" and not self.canary:
            raise ValueError(f"{self.id}: injection scenarios need a canary")
        if self.canary and self.canary not in self.full_text() + (
            self.injected_context.text if self.injected_context else ""
        ):
            raise ValueError(f"{self.id}: canary must be planted in the input or injected doc")
        if self.category == "pii" and not self.pii:
            raise ValueError(f"{self.id}: pii scenarios must list the PII strings")
        if isinstance(self.input, list) and self.input[-1].role != "user":
            raise ValueError(f"{self.id}: conversation must end with a user turn")
        return self

    @property
    def last_user_message(self) -> str:
        return self.input if isinstance(self.input, str) else self.input[-1].content

    def full_text(self) -> str:
        if isinstance(self.input, str):
            return self.input
        return "\n".join(t.content for t in self.input)


def load_scenarios(path: Path = GOLDEN_PATH) -> list[Scenario]:
    with path.open(encoding="utf-8") as f:
        return [Scenario.model_validate(json.loads(line)) for line in f if line.strip()]
