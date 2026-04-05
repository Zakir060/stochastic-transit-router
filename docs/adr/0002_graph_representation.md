# ADR 0002: Graph representation

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

The router must support static shortest paths, time-dependent updates, disruption penalties, and walking connectors in one graph abstraction while remaining performant enough for API requests.

## Decision

Adopt a custom adjacency-based directed graph representation in src/graph/core.py with typed node and edge entities, and use NetworkX only as a reference implementation for verification.

## Rationale

A custom graph gives precise control over memory layout, serialization, and update semantics. NetworkX is valuable for baseline correctness checks but is not sufficient as the only production graph implementation for this performance target.

## Consequences

- Graph builders and algorithms target custom interfaces first.
- Validation tests compare selected outputs with NetworkX reference runs.
- Serialization format and schema versioning become first-class design concerns.

## Related

- [Graph Model](/docs/math/graph_model.md)
- [ADR 0009: Algorithm selection](/docs/adr/0009_algorithm_selection.md)
- [Module Boundaries](/docs/architecture/module_boundaries.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
