# ADR 0014: City generalization

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

The project starts with NYC but must scale to additional cities without code rewrites in core graph and algorithm modules.

## Decision

Define a city configuration boundary that isolates feed URLs, geospatial bounds, segmentation windows, and local policy parameters in configuration files and adapters.

## Rationale

Configuration-driven city onboarding keeps algorithm implementations stable and reduces onboarding effort for new deployment contexts.

## Consequences

- New city enablement requires config and adapter additions, not core algorithm changes.
- City-specific assumptions are explicit and reviewable.
- Integration tests can run city-specific scenarios by swapping config bundles.

## Related

- [ADR 0001: Why NYC first](/docs/adr/0001_why_nyc_first.md)
- [Module boundaries](/docs/architecture/module_boundaries.md)
- [NYC configuration](/configs/nyc.yaml)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
