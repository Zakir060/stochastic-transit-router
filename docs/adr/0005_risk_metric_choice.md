# ADR 0005: Risk metric choice

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

Users and researchers need alternative route rankings that trade expected travel time against tail risk and reliability requirements, especially during service disruptions.

## Decision

Support four risk views in first-class routing objectives: expected time, mean-variance score, reliability at threshold tau, and CVaR at configurable alpha.

## Rationale

The selected metrics cover both operational needs and research analysis. CVaR is coherent for tail risk, reliability is user-facing and intuitive, and mean-variance remains computationally efficient for online ranking.

## Consequences

- API and CLI contracts expose lambda, tau, and alpha parameters.
- Evaluation includes calibration and stability analysis across risk settings.
- Documentation must align notation between mathematical definitions and implementation signatures.

## Related

- [Risk Metrics](/docs/math/risk_metrics.md)
- [Stochastic Routing](/docs/math/stochastic_routing.md)
- [Evaluation Plan](/docs/evaluation/evaluation_plan.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
