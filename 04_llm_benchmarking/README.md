# Phase 4: LLM Performance Benchmarking

Benchmark LLM models for **speed**, **throughput**, and **consistency** — this is pure performance engineering applied to AI.

## Key Metrics to Measure

| Metric | Description | Your Analogy |
|--------|-------------|-------------|
| **TTFT** | Time to First Token | Time to First Byte (TTFB) |
| **TPS** | Tokens Per Second | Throughput (TPS in LoadRunner) |
| **Total Latency** | End-to-end response time | Response Time |
| **P95 Latency** | 95th percentile | P95 in LoadRunner summary |
| **Error Rate** | Failed API calls | % Failed Transactions |

## Files
- `llm_benchmark.py` — Run N requests to an LLM and collect performance stats
- `benchmark_results/` — Auto-generated CSV reports from benchmark runs

## Run
```bash
python llm_benchmark.py
```
