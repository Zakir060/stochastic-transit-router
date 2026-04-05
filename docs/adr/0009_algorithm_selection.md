# ADR 0009: Algorithm selection

| Field | Value |
|---|---|
| Owner | Architecture Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

| Field | Value |
| --- | --- |
| Status | Accepted |
| Date | 2026-04-05 |

## Context

The router must support deterministic and stochastic objectives, realtime disruptions, and top-k alternatives with clear complexity statements and correctness tests.

## Decision

Include Dijkstra, bidirectional Dijkstra, A star, Yen top-k, time-dependent dynamic programming, stochastic shortest path approximation, and risk-aware ranking methods in the first major implementation cycle.

## Rationale

The selected set balances theoretical rigor, practical performance, and relevance to transportation reliability analysis. It also supports progressive evaluation from deterministic baseline to advanced risk objectives.

## Consequences

- Algorithm modules require formal complexity docstrings and regression tests.
- Benchmark suites compare methods on identical query workloads.
- Risk-aware algorithms rely on distribution estimators and covariance policy.

## Related

- [Graph Model](/docs/math/graph_model.md)
- [Stochastic Routing](/docs/math/stochastic_routing.md)
- [ADR 0012: Covariance approximation](/docs/adr/0012_covariance_approximation.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
