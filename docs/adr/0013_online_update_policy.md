# ADR 0013: Online update policy

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

Realtime observations provide continuous information for travel-time parameter updates, but unfiltered updates can be destabilized by anomalous observations.

## Decision

Use exponential moving average updates for means and variances with configurable alpha and z-score consistency filtering before applying updates.

## Rationale

EMA supports low-latency adaptation while keeping memory requirements bounded. Consistency filtering reduces sensitivity to outliers and feed anomalies.

## Consequences

- Update module logs accepted and rejected observations.
- Sensitivity analysis is required for alpha and z-score threshold choices.
- Distribution parameters can react quickly to disruptions without full refit.

## Related

- [Stochastic Routing](/docs/math/stochastic_routing.md)
- [NYC TLC Dataset](/docs/datasets/nyc_tlc.md)
- [ADR 0010: Realtime feed strategy](/docs/adr/0010_realtime_feed_strategy.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
