# Evaluation Plan

| Field | Value |
|---|---|
| Owner | Performance Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

This document defines empirical questions, metrics, and required data artifacts for algorithm and system evaluation.

## Evaluation questions

| Question ID | Question text | Metric | Data required | Status |
|:--|:--|:--|:--|:--|
| Q1 | Realtime updates improve route quality over static routing | mean realized seconds reduction | GTFS RT snapshots and static baseline | planned |
| Q2 | Stochastic optimum divergence from deterministic route | fraction with gap above one sigma | TLC calibrated edge distributions | planned |
| Q3 | Top k stability under disruptions | Jaccard similarity | service alert scenarios | planned |
| Q4 | Graph update latency after poll | wall time milliseconds | realtime ingest logs | planned |
| Q5 | OSM walking connectors improve transfer realism | transfer error reduction fraction | OSM edges and fallback baseline | planned |

## Routing objectives

| Objective | Formula | Algorithm | Expected vs deterministic difference |
|:--|:--|:--|:--|
| fastest | min E[T_p] | dijkstra time dependent | baseline |
| reliable | max P(T_p \<= tau) | reliability_router | favors narrow distributions |
| robust | min E[T_p] + lambda sigma_p | robust_router | penalizes variance |
| cvar | min CVaR_alpha(T_p) | cvar_router | prioritizes tail safety |

## Related

- [Benchmark protocol](/docs/evaluation/benchmark_protocol.md)
- [Risk metrics](/docs/math/risk_metrics.md)
- [NYC experiment README](/experiments/nyc/README.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: zakirbayramov942@gmail.com
