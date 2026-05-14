# Phase 6: SRE & Observability Concepts

Bridge from Performance Testing to **SRE (Site Reliability Engineering)** — your target role.

## Key SRE Concepts

### SLI → SLO → Error Budget

| Term | Meaning | Performance Testing Analogy |
|------|---------|----------------------------|
| **SLI** | Service Level Indicator — a metric (e.g., latency, error rate) | Your LoadRunner KPI |
| **SLO** | Service Level Objective — target for an SLI (e.g., P99 < 500ms) | Your performance acceptance criteria |
| **Error Budget** | How much failure is allowed per month | Like your max allowed failed transactions |
| **SLA** | Service Level Agreement — contractual commitment | Client SLA in your projects |

## Files
- `slo_calculator.py` — Calculate SLO compliance and error budget from test results

## The SRE Mindset Shift
- Performance Engineer: "Does the system meet the SLA under load?"
- SRE: "What's the reliability target, and how do we measure + alert on it continuously?"

Your performance testing background is a huge advantage for SRE!
