"""Token-cost estimation from the configurable price table in `core/pricing.yaml`."""

from __future__ import annotations

import datetime as dt
from functools import lru_cache
from pathlib import Path

import yaml
from pydantic import BaseModel

DEFAULT_PRICE_TABLE = Path(__file__).resolve().parent / "pricing.yaml"


class PriceEntry(BaseModel):
    effective_from: dt.date
    input: float  # USD per 1M input tokens
    output: float  # USD per 1M output tokens
    long_context_threshold: int | None = None
    long_input: float | None = None
    long_output: float | None = None


class PriceTable(BaseModel):
    source: str
    retrieved: str
    models: dict[str, list[PriceEntry]]

    def price_for(self, model: str, on: dt.date | None = None) -> PriceEntry | None:
        entries = self.models.get(model)
        if not entries:
            return None
        on = on or dt.date.today()
        applicable = [e for e in entries if e.effective_from <= on]
        return max(applicable, key=lambda e: e.effective_from) if applicable else None

    def cost_usd(
        self, model: str, input_tokens: int, output_tokens: int, on: dt.date | None = None
    ) -> float | None:
        """Estimated USD cost, or None if the model is not in the table (never guessed)."""
        p = self.price_for(model, on)
        if p is None:
            return None
        rate_in, rate_out = p.input, p.output
        if p.long_context_threshold and input_tokens > p.long_context_threshold:
            rate_in = p.long_input if p.long_input is not None else rate_in
            rate_out = p.long_output if p.long_output is not None else rate_out
        return (input_tokens * rate_in + output_tokens * rate_out) / 1_000_000


@lru_cache(maxsize=4)
def load_price_table(path: Path = DEFAULT_PRICE_TABLE) -> PriceTable:
    return PriceTable.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")))
