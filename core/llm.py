"""Thin LLM client layer over the `google-genai` SDK.

The same client works against the Gemini Developer API (GEMINI_API_KEY) or Vertex AI
(ADC credentials, GOOGLE_GENAI_USE_VERTEXAI=true). Every call returns token usage and
latency so callers can do per-request cost accounting.
"""

from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, Protocol

from pydantic import BaseModel

from core.config import Settings, get_settings

# HTTP status codes worth retrying (rate limit, transient server errors).
_RETRYABLE = {429, 500, 502, 503, 504}


@dataclass
class LLMResponse:
    text: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    latency_ms: float = 0.0


class LLMClient(Protocol):
    def generate(
        self,
        prompt: str,
        *,
        model: str,
        system: str | None = None,
        temperature: float | None = None,
        response_schema: type[BaseModel] | None = None,
    ) -> LLMResponse: ...


class MissingCredentialsError(RuntimeError):
    pass


class LLMCallError(RuntimeError):
    """Raised after retries are exhausted; callers record it rather than guessing an output."""


class GeminiClient:
    """`google-genai` client; picks Developer API vs Vertex AI from settings."""

    def __init__(self, settings: Settings | None = None) -> None:
        from google import genai

        self.settings = settings or get_settings()
        s = self.settings
        if s.google_genai_use_vertexai:
            if not s.google_cloud_project:
                raise MissingCredentialsError(
                    "GOOGLE_GENAI_USE_VERTEXAI=true requires GOOGLE_CLOUD_PROJECT."
                )
            self._client = genai.Client(
                vertexai=True, project=s.google_cloud_project, location=s.google_cloud_location
            )
        else:
            if not s.gemini_api_key:
                raise MissingCredentialsError(
                    "Set GEMINI_API_KEY (or GOOGLE_GENAI_USE_VERTEXAI=true). See .env.example."
                )
            self._client = genai.Client(api_key=s.gemini_api_key)

    def generate(
        self,
        prompt: str,
        *,
        model: str,
        system: str | None = None,
        temperature: float | None = None,
        response_schema: type[BaseModel] | None = None,
    ) -> LLMResponse:
        from google.genai import types

        config = types.GenerateContentConfig(
            system_instruction=system,
            temperature=self.settings.llm_temperature if temperature is None else temperature,
            response_mime_type="application/json" if response_schema else None,
            response_schema=response_schema,
        )
        t0 = time.perf_counter()
        resp = self._call_with_retry(model, prompt, config)
        latency_ms = (time.perf_counter() - t0) * 1000
        usage = resp.usage_metadata
        return LLMResponse(
            text=resp.text or "",
            model=model,
            input_tokens=(usage.prompt_token_count or 0) if usage else 0,
            # Thinking tokens are billed as output tokens.
            output_tokens=(
                (usage.candidates_token_count or 0) + (usage.thoughts_token_count or 0)
                if usage
                else 0
            ),
            latency_ms=latency_ms,
        )

    def _call_with_retry(self, model: str, prompt: str, config: Any, attempts: int = 5) -> Any:
        from google.genai import errors

        for n in range(attempts):
            try:
                return self._client.models.generate_content(
                    model=model, contents=prompt, config=config
                )
            except errors.APIError as exc:
                if exc.code not in _RETRYABLE or n == attempts - 1:
                    raise LLMCallError(f"{model}: {exc.code} {exc.message}") from exc
                time.sleep(min(2**n * 2, 30))
        raise AssertionError("unreachable")

    @property
    def raw(self) -> Any:
        """Underlying `genai.Client` (used by the Gemini embedder)."""
        return self._client


@dataclass
class FakeLLM:
    """Deterministic stand-in for tests: returns `responder(prompt)` and records calls."""

    responder: Callable[[str], str]
    calls: list[dict[str, object]] = field(default_factory=list)

    def generate(
        self,
        prompt: str,
        *,
        model: str,
        system: str | None = None,
        temperature: float | None = None,
        response_schema: type[BaseModel] | None = None,
    ) -> LLMResponse:
        self.calls.append(
            {"prompt": prompt, "model": model, "system": system, "schema": response_schema}
        )
        text = self.responder(prompt)
        return LLMResponse(
            text=text,
            model=model,
            input_tokens=len(prompt) // 4,
            output_tokens=len(text) // 4,
            latency_ms=0.0,
        )
