# ADR 0012: Covariance approximation

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

Path variance estimation depends on covariance between edge travel times. Sparse historical samples make full covariance estimation unstable for many edge pairs.

## Decision

When pairwise observation count is below configurable min_obs, assume zero covariance for that pair, log a warning event, and record approximation use in experiment metadata.

## Rationale

The decision preserves numerical stability and throughput while keeping approximation behavior explicit and auditable.

## Consequences

- Variance outputs include approximation metadata.
- Risk ranking may be conservative or under-dispersed on sparse paths.
- Sensitivity studies must quantify impact of min_obs choices.

## Related

- [Stochastic Routing](/docs/math/stochastic_routing.md)
- [Estimation](/docs/math/estimation.md)
- [ADR 0004: Stochastic approximation](/docs/adr/0004_stochastic_approximation.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
