# ADR 0004: Stochastic approximation

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

Path-level travel time uncertainty requires combining edge-level distributions while accounting for covariance under sparse observations. Full joint modeling is often infeasible at city scale.

## Decision

Use empirical edge distributions conditioned by time-of-day and weekday flags, propagate means and variances to path-level scores, and apply logged covariance approximations when pairwise observations are insufficient.

## Rationale

This approach is computationally tractable for production queries while preserving mathematically explicit uncertainty handling and auditability of approximation decisions.

## Consequences

- Stochastic and robust route ranking depends on data availability diagnostics.
- Approximation assumptions must be documented in logs and experiment metadata.
- Sparse segments may produce wider confidence intervals and conservative route ranks.

## Related

- [Stochastic Routing](/docs/math/stochastic_routing.md)
- [ADR 0012: Covariance approximation](/docs/adr/0012_covariance_approximation.md)
- [Estimation](/docs/math/estimation.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
