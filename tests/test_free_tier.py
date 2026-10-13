"""Free-tier guarantees: guard, RPM throttle, daily budget, 429 handling, judge cache, resume,
local judge backend and the network-blocked deterministic mode. All offline."""

from __future__ import annotations

import datetime as dt
import json
import socket
from pathlib import Path
from typing import Any

import httpx
import pytest
from google.genai import errors

from core.config import FreeTierViolation, Settings
from core.llm import (
    FakeLLM,
    GeminiClient,
    LLMCallError,
    OpenAICompatClient,
    QuotaExhaustedError,
    _quota_details,
)
from core.ratelimit import DailyBudgetExhausted, RequestGovernor
from evals.judge import CorrectnessVerdict, LLMJudge
from evals.judge_cache import JudgeCache
from evals.netguard import NetworkBlocked, no_network
from evals.run import mock_responder, read_results, run_eval
from evals.schema import Scenario, load_scenarios
from evals.systems import RagSystem, RunRecord
from tests.conftest import KeywordReranker, make_retriever, make_settings

GOLDEN = {s.id: s for s in load_scenarios()}


# --- free-tier guard ------------------------------------------------------------------------


def test_free_tier_guard_blocks_billed_paths(tmp_path: Path) -> None:
    s = make_settings(tmp_path)
    s.check_free_tier("gemini-3.8-flash")  # allowed
    with pytest.raises(FreeTierViolation, match="not in FREE_TIER_MODELS"):
        s.check_free_tier("gemini-3.1-pro-preview")
    with pytest.raises(FreeTierViolation, match="Vertex"):
        make_settings(tmp_path, google_genai_use_vertexai=True).check_free_tier()
    with pytest.raises(FreeTierViolation, match="vertex"):
        make_settings(tmp_path, vector_store="vertex").check_free_tier()
    make_settings(tmp_path, free_tier_only=False).check_free_tier("anything")  # opt-out


def test_defaults_are_free_tier_flash_and_judge_differs() -> None:
    s = Settings(_env_file=None)  # type: ignore[call-arg]
    for m in (s.flash_model, s.strong_model, s.judge_model):
        assert m in s.free_tier_models and "pro" not in m
    assert s.judge_model != s.flash_model
    assert not make_settings(
        Path("."), google_genai_use_vertexai=True, google_cloud_project="p"
    ).has_llm_credentials


# --- governor -----------------------------------------------------------------------------


class Clock:
    def __init__(self) -> None:
        self.t = 1000.0
        self.slept: list[float] = []

    def __call__(self) -> float:
        return self.t

    def sleep(self, s: float) -> None:
        self.slept.append(s)
        self.t += s


def _gov(
    tmp_path: Path,
    rpm: float = 6,
    budget: int = 3,
    when: str = "2026-10-13T12:00:00",
    clock: Clock | None = None,
) -> RequestGovernor:
    clock = clock or Clock()
    now = dt.datetime.fromisoformat(when).replace(tzinfo=dt.UTC)
    return RequestGovernor(rpm, budget, tmp_path, clock=clock, sleep=clock.sleep, now=lambda: now)


def test_rpm_throttle_spaces_requests_per_model(tmp_path: Path) -> None:
    clock = Clock()
    g = _gov(tmp_path, rpm=6, budget=100, clock=clock)  # 10 s apart
    g.acquire("a")
    g.acquire("a")
    g.acquire("b")  # different model: no wait
    assert clock.slept == [10.0]
    clock.t += 25
    g.acquire("a")  # 25 s since last: no wait
    assert clock.slept == [10.0]


def test_daily_budget_persists_and_aborts(tmp_path: Path) -> None:
    g = _gov(tmp_path, budget=2)
    g.acquire("m")
    g.acquire("m")
    with pytest.raises(DailyBudgetExhausted, match="2/2"):
        g.acquire("m")
    # a new process (fresh governor) sees the same persisted count
    with pytest.raises(DailyBudgetExhausted):
        _gov(tmp_path, budget=2).acquire("m")
    assert _gov(tmp_path, budget=2).used_today("other") == 0


def test_budget_day_is_pacific_and_resets(tmp_path: Path) -> None:
    # 06:59 UTC on Oct 14 is still Oct 13 in Pacific time (UTC-7 in October).
    late = _gov(tmp_path, budget=1, when="2026-10-14T06:59:00")
    assert late.pacific_day() == "2026-10-13"
    late.acquire("m")
    with pytest.raises(DailyBudgetExhausted):
        late.acquire("m")
    nextday = _gov(tmp_path, budget=1, when="2026-10-14T07:01:00")
    assert nextday.pacific_day() == "2026-10-14"
    nextday.acquire("m")  # fresh budget after midnight Pacific


def test_mark_exhausted_blocks_rest_of_day(tmp_path: Path) -> None:
    g = _gov(tmp_path, budget=50)
    g.mark_exhausted("m")
    with pytest.raises(DailyBudgetExhausted):
        g.acquire("m")


# --- Gemini client 429 handling -------------------------------------------------------------


def _quota_error(quota_id: str | None = None, delay: str | None = None) -> errors.APIError:
    details: list[dict[str, Any]] = []
    if quota_id:
        details.append(
            {
                "@type": "type.googleapis.com/google.rpc.QuotaFailure",
                "violations": [
                    {
                        "quotaMetric": "generate_content_free_tier_requests",
                        "quotaId": quota_id,
                        "quotaValue": "20",
                    }
                ],
            }
        )
    if delay:
        details.append({"@type": "type.googleapis.com/google.rpc.RetryInfo", "retryDelay": delay})
    return errors.APIError(
        429,
        {
            "error": {
                "code": 429,
                "message": "quota",
                "status": "RESOURCE_EXHAUSTED",
                "details": details,
            }
        },
    )


class _FakeModels:
    def __init__(self, outcomes: list[Any]) -> None:
        self.outcomes = outcomes
        self.calls = 0

    def generate_content(self, **_: object) -> Any:
        self.calls += 1
        out = self.outcomes.pop(0)
        if isinstance(out, Exception):
            raise out
        return out


class _Resp:
    text = "ok"
    usage_metadata = None


def _client(
    tmp_path: Path, outcomes: list[Any], budget: int = 100
) -> tuple[GeminiClient, _FakeModels, Clock]:
    clock = Clock()
    s = make_settings(tmp_path, gemini_api_key="test-key", llm_max_retries=4)
    gov = RequestGovernor(1000, budget, tmp_path / "usage", clock=clock, sleep=clock.sleep)
    c = GeminiClient(s, governor=gov, sleep=clock.sleep)
    models = _FakeModels(outcomes)
    c._client = type("C", (), {"models": models})()
    return c, models, clock


def test_quota_details_parsing() -> None:
    delay, v = _quota_details(
        _quota_error("GenerateRequestsPerDayPerProjectPerModel-FreeTier", "37s").details
    )
    assert delay == 37.0 and v[0]["quotaValue"] == "20"


def test_429_backs_off_honouring_server_hint_then_succeeds(tmp_path: Path) -> None:
    c, models, clock = _client(
        tmp_path,
        [_quota_error("GenerateRequestsPerMinutePerProjectPerModel-FreeTier", "37s"), _Resp()],
    )
    r = c.generate("p", model="gemini-3.8-flash")
    assert r.text == "ok" and r.requests == 2 and models.calls == 2
    assert 37.0 <= clock.slept[-1] <= 38.0  # server hint beats the 4 s exponential base
    assert c.observed_quota and "PerMinute" in c.observed_quota[0]["quotaId"]


def test_exponential_backoff_without_hint(tmp_path: Path) -> None:
    c, _, clock = _client(tmp_path, [_quota_error(), _quota_error(), _Resp()])
    c.generate("p", model="gemini-3.8-flash")
    backoffs = [s for s in clock.slept if s > 2]
    assert 4 <= backoffs[0] < 5 and 8 <= backoffs[1] < 9


def test_daily_quota_429_aborts_immediately_and_marks_day(tmp_path: Path) -> None:
    c, models, _ = _client(
        tmp_path, [_quota_error("GenerateRequestsPerDayPerProjectPerModel-FreeTier"), _Resp()]
    )
    with pytest.raises(QuotaExhaustedError, match="daily free-tier quota"):
        c.generate("p", model="gemini-3.8-flash")
    assert models.calls == 1  # no retries against a daily quota
    with pytest.raises(QuotaExhaustedError):  # later calls today stop before any HTTP request
        c.generate("p", model="gemini-3.8-flash")
    assert models.calls == 1


def test_budget_exhaustion_spends_no_request(tmp_path: Path) -> None:
    c, models, _ = _client(tmp_path, [_Resp(), _Resp()], budget=1)
    c.generate("p", model="gemini-3.8-flash")
    with pytest.raises(QuotaExhaustedError, match="budget"):
        c.generate("p", model="gemini-3.8-flash")
    assert models.calls == 1


def test_non_retryable_error_raises_llm_call_error(tmp_path: Path) -> None:
    c, models, _ = _client(tmp_path, [errors.APIError(400, {"error": {"message": "bad"}})])
    with pytest.raises(LLMCallError, match="400"):
        c.generate("p", model="gemini-3.8-flash")
    assert models.calls == 1


def test_client_refuses_non_free_model(tmp_path: Path) -> None:
    c, models, _ = _client(tmp_path, [_Resp()])
    with pytest.raises(FreeTierViolation):
        c.generate("p", model="gemini-3.1-pro-preview")
    assert models.calls == 0


# --- OpenAI-compatible (Ollama) judge backend -------------------------------------------------


def test_openai_compat_client_sends_schema_and_parses_usage() -> None:
    seen: dict[str, Any] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen.update(json.loads(request.content))
        seen["url"] = str(request.url)
        return httpx.Response(
            200,
            json={
                "choices": [{"message": {"content": '{"facts": [], "reasoning": "r"}'}}],
                "usage": {"prompt_tokens": 12, "completion_tokens": 7},
            },
        )

    c = OpenAICompatClient("http://localhost:11434/v1/", transport=httpx.MockTransport(handler))
    r = c.generate(
        "prompt",
        model="llama3.2:1b",
        system="sys",
        temperature=0.0,
        response_schema=CorrectnessVerdict,
    )
    assert seen["url"] == "http://localhost:11434/v1/chat/completions"
    assert seen["messages"][0] == {"role": "system", "content": "sys"}
    assert seen["response_format"]["type"] == "json_schema" and seen["temperature"] == 0.0
    assert (r.input_tokens, r.output_tokens, r.requests) == (12, 7, 1)


def test_openai_compat_errors_become_llm_call_error() -> None:
    c = OpenAICompatClient(
        "http://x/v1", transport=httpx.MockTransport(lambda req: httpx.Response(500, text="boom"))
    )
    with pytest.raises(LLMCallError):
        c.generate("p", model="m")


# --- judge cache --------------------------------------------------------------------------------


def _judge_inputs() -> tuple[RunRecord, Scenario]:
    sc = Scenario(
        id="t",
        category="architecture",
        input="q",
        expected="ref",
        key_facts=["fact a"],
        required_sources=["spot"],
    )
    rec = RunRecord(
        scenario_id="t",
        category="architecture",
        answer="Spot is cheap [S1].",
        retrieved=[
            {
                "chunk_id": "spot#0",
                "doc_id": "spot",
                "title": "Spot",  # type: ignore[list-item]
                "url": "u",
                "confidence": 0.9,
                "text": "Spot VMs are cheap.",
            }
        ],
    )
    return rec, sc


def _responder(prompt: str) -> str:
    if "groundedness" in prompt:
        return json.dumps(
            {"claims": [{"claim": "c", "supported": True, "evidence": "S1"}], "reasoning": "r"}
        )
    return json.dumps({"facts": [{"fact": "fact a", "status": "covered"}], "reasoning": "r"})


def test_judge_cache_avoids_repeat_calls(tmp_path: Path) -> None:
    cache = JudgeCache(tmp_path)
    llm = FakeLLM(_responder)
    first = LLMJudge(llm, "gemini-3.6-flash", "gemini", cache).judge(*_judge_inputs())
    assert len(llm.calls) == 2 and first["judge_requests"] == 2
    llm2 = FakeLLM(_responder)
    second = LLMJudge(llm2, "gemini-3.6-flash", "gemini", JudgeCache(tmp_path)).judge(
        *_judge_inputs()
    )
    assert llm2.calls == [] and second["judge_cache_hits"] == 2 and second["judge_requests"] == 0
    assert second["correctness"] == first["correctness"]


def test_judge_cache_key_separates_models_and_backends(tmp_path: Path) -> None:
    base = dict(backend="gemini", model="m", system="s", prompt="p", schema="x", temperature=0.0)
    k = JudgeCache.key(**base)  # type: ignore[arg-type]
    assert k != JudgeCache.key(**{**base, "model": "m2"})  # type: ignore[arg-type]
    assert k != JudgeCache.key(**{**base, "backend": "openai_compat"})  # type: ignore[arg-type]
    assert k != JudgeCache.key(**{**base, "prompt": "p2"})  # type: ignore[arg-type]


def test_invalid_judge_output_is_not_cached(tmp_path: Path) -> None:
    cache = JudgeCache(tmp_path)
    LLMJudge(FakeLLM(lambda p: "nope"), "m", "gemini", cache).judge(*_judge_inputs())
    assert not list(tmp_path.rglob("*.json"))


# --- quota stop + resume ------------------------------------------------------------------------


class _QuotaAfter:
    """LLM wrapper that raises QuotaExhaustedError after `n` successful calls."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.calls = 0
        self.inner = FakeLLM(mock_responder)

    def generate(self, prompt: str, **kw: Any) -> Any:
        if self.calls >= self.n:
            raise QuotaExhaustedError("daily request budget exhausted")
        self.calls += 1
        return self.inner.generate(prompt, **kw)


def _scenarios() -> list[Scenario]:
    return [GOLDEN[i] for i in ("arch-03", "mh-05", "inj-04", "pii-02")]


def test_quota_stop_then_resume_without_repeating_calls(tmp_path: Path) -> None:
    s = make_settings(tmp_path, flash_model="m")
    retriever = make_retriever(s, KeywordReranker())
    first = _QuotaAfter(2)
    out = run_eval(_scenarios(), RagSystem(s, retriever, first), None, tmp_path / "run", {})  # type: ignore[arg-type]
    assert out["meta"]["aborted"].startswith("quota") and out["meta"]["completed"] == 2
    saved = read_results(tmp_path / "run" / "results.jsonl")
    assert len(saved) == 2

    second = _QuotaAfter(100)
    out2 = run_eval(
        _scenarios(),
        RagSystem(s, retriever, second),
        None,
        tmp_path / "run",  # type: ignore[arg-type]
        {},
        previous=saved,
    )
    assert out2["meta"]["aborted"] is None and out2["meta"]["completed"] == 4
    assert out2["meta"]["reused_from_previous"] == 2
    # Interrupted + resumed spends exactly what one uninterrupted run would: nothing repeated.
    uninterrupted = _QuotaAfter(100)
    run_eval(_scenarios(), RagSystem(s, retriever, uninterrupted), None, tmp_path / "ref", {})  # type: ignore[arg-type]
    assert first.calls + second.calls == uninterrupted.calls
    final = read_results(tmp_path / "run" / "results.jsonl")
    assert final["arch-03"].answer == saved["arch-03"].answer
    assert list(final) == [sc.id for sc in _scenarios()]


class _QuotaJudge:
    model = "j"
    backend = "gemini"

    def __init__(self, fail: bool) -> None:
        self.fail = fail
        self.calls = 0

    def judge(self, rec: RunRecord, sc: Scenario) -> dict[str, object]:
        self.calls += 1
        if self.fail:
            raise QuotaExhaustedError("judge quota")
        return {"judge_backend": "gemini", "judge_model": "j", "correctness": {"score": 1.0}}


def test_judge_quota_keeps_answer_and_resume_only_rejudges(tmp_path: Path) -> None:
    s = make_settings(tmp_path, flash_model="m")
    llm = FakeLLM(mock_responder)
    system = RagSystem(s, make_retriever(s, KeywordReranker()), llm)
    run_dir = tmp_path / "run"
    out = run_eval(_scenarios()[:2], system, _QuotaJudge(fail=True), run_dir, {})
    assert out["meta"]["completed"] == 0 and len(llm.calls) == 1
    pending = read_results(run_dir / "results.jsonl")
    assert pending["arch-03"].judge.get("pending")

    out2 = run_eval(
        _scenarios()[:2], system, _QuotaJudge(fail=False), run_dir, {}, previous=pending
    )
    assert out2["meta"]["rejudged"] == 1 and out2["meta"]["completed"] == 2
    assert len(llm.calls) == 2  # arch-03 was NOT regenerated; only mh-05 was new


# --- deterministic, network-free mode ---------------------------------------------------------


def test_network_guard_blocks_connections_and_restores() -> None:
    with no_network(), pytest.raises(NetworkBlocked):
        socket.create_connection(("example.com", 443), timeout=1)
    assert socket.create_connection is not None and "_blocked" not in repr(socket.create_connection)


def test_retrieval_only_system_never_generates(tmp_path: Path) -> None:
    s = make_settings(tmp_path)
    system = RagSystem(s, make_retriever(s, KeywordReranker()), None)
    with no_network():
        ok = system.run(
            GOLDEN["arch-03"].model_copy(update={"input": "regional cloud sql standby failover"})
        )
        refused = system.run(GOLDEN["oos-01"])
    assert ok.generated is False and ok.answer == "" and ok.llm_requests == 0
    assert refused.refused and refused.generated
    assert system.name == "rag-v1-retrieval-only"
