"""LLM client layer.

- `GeminiClient`: `google-genai` against the Gemini Developer API with an AI Studio key.
  While FREE_TIER_ONLY is set it refuses Vertex AI and any model not on the verified free-tier
  list, throttles every attempt through the shared `RequestGovernor` (RPM + daily budget),
  and backs off exponentially on 429s, honouring the server's RetryInfo delay. A 429 that
  names a per-day quota aborts immediately instead of retrying.
- `OpenAICompatClient`: any OpenAI-compatible chat endpoint (e.g. a local Ollama server),
  used as a fallback judge backend.
- `FakeLLM`: deterministic stand-in for tests and mocked smoke runs.

Every response reports tokens, latency and the number of HTTP requests it took.
"""

from __future__ import annotations

import json
import random
import re
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any, Protocol

import httpx
from pydantic import BaseModel

from core.config import Settings, get_settings
from core.ratelimit import DailyBudgetExhausted, RequestGovernor, get_governor

# HTTP status codes worth retrying (rate limit, transient server errors).
_RETRYABLE = {429, 500, 502, 503, 504}


@dataclass
class LLMResponse:
    text: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    latency_ms: float = 0.0
    requests: int = 1  # HTTP attempts, including retries


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


class QuotaExhaustedError(LLMCallError):
    """Daily request budget or server-side daily quota exhausted: the run must stop cleanly."""


def _quota_details(details: Any) -> tuple[float | None, list[dict[str, str]]]:
    """Extract (retry delay seconds, quota violations) from a Gemini 429 error payload."""
    err = details.get("error", {}) if isinstance(details, dict) else {}
    delay: float | None = None
    violations: list[dict[str, str]] = []
    for d in err.get("details", []) or []:
        kind = str(d.get("@type", ""))
        if kind.endswith("RetryInfo"):
            m = re.match(r"([\d.]+)s", str(d.get("retryDelay", "")))
            delay = float(m.group(1)) if m else None
        elif kind.endswith("QuotaFailure"):
            for v in d.get("violations", []) or []:
                violations.append(
                    {k: str(v.get(k, "")) for k in ("quotaMetric", "quotaId", "quotaValue")}
                )
    return delay, violations


def _is_daily_quota(violations: list[dict[str, str]]) -> bool:
    return any("perday" in v.get("quotaId", "").lower() for v in violations)


class GeminiClient:
    """Gemini Developer API client with free-tier guards and rate-limit handling."""

    def __init__(
        self,
        settings: Settings | None = None,
        governor: RequestGovernor | None = None,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        from google import genai

        self.settings = settings or get_settings()
        s = self.settings
        s.check_free_tier()
        self.governor = governor or get_governor(s.llm_rpm, s.llm_daily_request_budget, s.usage_dir)
        self._sleep = sleep
        # Quota violations seen in 429 responses: the only way to learn the project's real
        # free-tier limits programmatically, since they are not published.
        self.observed_quota: list[dict[str, str]] = []
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
                    "Set GEMINI_API_KEY (an AI Studio key on a project without billing). "
                    "See .env.example."
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

        self.settings.check_free_tier(model)
        config = types.GenerateContentConfig(
            system_instruction=system,
            temperature=self.settings.llm_temperature if temperature is None else temperature,
            response_mime_type="application/json" if response_schema else None,
            response_schema=response_schema,
        )
        t0 = time.perf_counter()
        resp, attempts = self._call_with_retry(model, prompt, config)
        latency_ms = (time.perf_counter() - t0) * 1000
        usage = resp.usage_metadata
        return LLMResponse(
            text=resp.text or "",
            model=model,
            input_tokens=(usage.prompt_token_count or 0) if usage else 0,
            # Thinking tokens count as output tokens.
            output_tokens=(
                (usage.candidates_token_count or 0) + (usage.thoughts_token_count or 0)
                if usage
                else 0
            ),
            latency_ms=latency_ms,
            requests=attempts,
        )

    def backoff_delay(self, attempt: int, server_hint: float | None) -> float:
        s = self.settings
        expo = min(s.llm_backoff_base_s * 2**attempt, s.llm_backoff_max_s)
        delay = max(expo, server_hint or 0.0)
        return min(delay + random.uniform(0, 1), s.llm_backoff_max_s + 1)

    def _call_with_retry(
        self, model: str, prompt: str, config: Any, attempts: int | None = None
    ) -> tuple[Any, int]:
        from google.genai import errors

        attempts = attempts or self.settings.llm_max_retries
        for n in range(attempts):
            try:
                self.governor.acquire(model)
            except DailyBudgetExhausted as exc:
                raise QuotaExhaustedError(str(exc)) from exc
            try:
                resp = self._client.models.generate_content(
                    model=model, contents=prompt, config=config
                )
                return resp, n + 1
            except errors.APIError as exc:
                hint, violations = _quota_details(exc.details)
                self.observed_quota.extend(violations)
                if exc.code == 429 and _is_daily_quota(violations):
                    self.governor.mark_exhausted(model)
                    raise QuotaExhaustedError(
                        f"{model}: server reports daily free-tier quota exhausted "
                        f"({violations}). Resume after midnight Pacific with --resume."
                    ) from exc
                if exc.code not in _RETRYABLE or n == attempts - 1:
                    raise LLMCallError(f"{model}: {exc.code} {exc.message}") from exc
                self._sleep(self.backoff_delay(n, hint))
        raise AssertionError("unreachable")

    @property
    def raw(self) -> Any:
        """Underlying `genai.Client` (used by the Gemini embedder)."""
        return self._client


class OpenAICompatClient:
    """Chat-completions client for OpenAI-compatible servers (Ollama: http://localhost:11434/v1).

    Structured output uses `response_format: json_schema`; the caller still validates the JSON.
    Local backends are not rate-limited by the Gemini governor.
    """

    def __init__(
        self,
        base_url: str,
        api_key: str | None = None,
        timeout_s: float = 300.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        self._http = httpx.Client(headers=headers, timeout=timeout_s, transport=transport)

    def generate(
        self,
        prompt: str,
        *,
        model: str,
        system: str | None = None,
        temperature: float | None = None,
        response_schema: type[BaseModel] | None = None,
    ) -> LLMResponse:
        messages = ([{"role": "system", "content": system}] if system else []) + [
            {"role": "user", "content": prompt}
        ]
        body: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": 0.2 if temperature is None else temperature,
        }
        if response_schema is not None:
            body["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": response_schema.__name__,
                    "schema": response_schema.model_json_schema(),
                    "strict": True,
                },
            }
        t0 = time.perf_counter()
        try:
            r = self._http.post(f"{self.base_url}/chat/completions", json=body)
            r.raise_for_status()
            data = r.json()
            text = data["choices"][0]["message"]["content"] or ""
        except (httpx.HTTPError, KeyError, IndexError, json.JSONDecodeError) as exc:
            raise LLMCallError(f"{self.base_url} {model}: {exc}") from exc
        usage = data.get("usage") or {}
        return LLMResponse(
            text=text,
            model=model,
            input_tokens=int(usage.get("prompt_tokens") or 0),
            output_tokens=int(usage.get("completion_tokens") or 0),
            latency_ms=(time.perf_counter() - t0) * 1000,
            requests=1,
        )


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
