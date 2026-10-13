# Archived runs

These runs are kept for transparency. They are **not** reported as results.

| Run | Why archived |
|---|---|
| `det-baseline-stalled` | First run of the deterministic, retrieval-only baseline (2026-10-13). Scenario `pii-02` stalled for about 20 minutes (1,215,872 ms), and latencies drifted from about 1.3 s to 30–54 s late in the run. Retrieval-only work cannot block like that, so the cause looks environmental (machine contention). The same configuration re-run as `det-baseline-r2`, which is the reported baseline, gave identical retrieved chunks, refusals and metrics for all 50 scenarios (checked programmatically) and latencies of 1.1–2.1 s. Only the latency figures of this archived run are unreliable. |
