"""Free-tier request governance for Gemini API calls.

- Per-model throttle: at most `rpm` requests per minute, enforced as a minimum interval of
  60/rpm seconds between requests to the same model (smooth, no bursts).
- Per-model daily request budget, persisted to `usage_dir/<pacific-date>.json`, so the count
  survives restarts and resumed runs. Google resets requests-per-day at midnight Pacific time,
  so the budget day is the Pacific calendar day.
- Every attempt counts (including retries after a 429): conservative, never under-counts.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import threading
import time
from collections.abc import Callable
from functools import lru_cache
from pathlib import Path
from zoneinfo import ZoneInfo

PACIFIC = ZoneInfo("America/Los_Angeles")


class DailyBudgetExhausted(RuntimeError):
    def __init__(self, model: str, used: int, budget: int, day: str, reason: str = "") -> None:
        self.model, self.used, self.budget, self.day = model, used, budget, day
        super().__init__(
            f"daily request budget for {model} exhausted ({used}/{budget} on {day} Pacific)"
            + (f": {reason}" if reason else "")
            + ". Resume after midnight Pacific with --resume, or switch the judge to a local "
            "backend."
        )


class RequestGovernor:
    def __init__(
        self,
        rpm: float,
        daily_budget: int,
        usage_dir: Path,
        *,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], None] = time.sleep,
        now: Callable[[], dt.datetime] = lambda: dt.datetime.now(dt.UTC),
    ) -> None:
        if rpm <= 0 or daily_budget <= 0:
            raise ValueError("rpm and daily_budget must be positive")
        self.min_interval = 60.0 / rpm
        self.daily_budget = daily_budget
        self.usage_dir = usage_dir
        self._clock, self._sleep, self._now = clock, sleep, now
        self._last: dict[str, float] = {}
        self._lock = threading.Lock()
        self.waited_s = 0.0  # total throttle sleep, reported per run

    def pacific_day(self) -> str:
        return self._now().astimezone(PACIFIC).date().isoformat()

    def _path(self, day: str) -> Path:
        return self.usage_dir / f"requests-{day}.json"

    def _load(self, day: str) -> dict[str, int]:
        p = self._path(day)
        if not p.exists():
            return {}
        data: dict[str, int] = json.loads(p.read_text(encoding="utf-8"))
        return data

    def _save(self, day: str, counts: dict[str, int]) -> None:
        self.usage_dir.mkdir(parents=True, exist_ok=True)
        tmp = self._path(day).with_suffix(".tmp")
        tmp.write_text(json.dumps(counts, indent=2, sort_keys=True), encoding="utf-8")
        os.replace(tmp, self._path(day))

    def used_today(self, model: str) -> int:
        return self._load(self.pacific_day()).get(model, 0)

    def acquire(self, model: str) -> None:
        """Block until a request to `model` is allowed, then count it. Raises when over budget."""
        with self._lock:
            day = self.pacific_day()
            counts = self._load(day)
            used = counts.get(model, 0)
            if used >= self.daily_budget:
                raise DailyBudgetExhausted(model, used, self.daily_budget, day)
            last = self._last.get(model)
            if last is not None:
                wait = self.min_interval - (self._clock() - last)
                if wait > 0:
                    self._sleep(wait)
                    self.waited_s += wait
            self._last[model] = self._clock()
            counts[model] = used + 1
            self._save(day, counts)

    def mark_exhausted(self, model: str) -> None:
        """The server reported the daily quota as exhausted: stop spending requests today."""
        with self._lock:
            day = self.pacific_day()
            counts = self._load(day)
            counts[model] = max(counts.get(model, 0), self.daily_budget)
            self._save(day, counts)


@lru_cache(maxsize=8)
def get_governor(rpm: float, daily_budget: int, usage_dir: Path) -> RequestGovernor:
    """Process-wide governor per configuration, shared by the answerer and the judge."""
    return RequestGovernor(rpm, daily_budget, usage_dir)
