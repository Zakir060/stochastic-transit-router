# ADR 0011: Walking edge model

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

Transit transfer realism requires pedestrian connectors around stations. Straight-line assumptions alone can bias transfer times and route ranking.

## Decision

Construct walking edges from OSM Overpass data within configurable radius, compute shortest walk paths where possible, and use haversine-based fallback only when routing geometry is unavailable.

## Rationale

OSM-based walking connectors improve physical realism and transfer plausibility while retaining robustness when local path extraction fails.

## Consequences

- OSM ingestion becomes part of graph build prerequisites.
- Walking edge provenance records query bounds and response metadata.
- Evaluation compares OSM connectors against straight-line fallback effects.

## Related

- [OSM Overpass Dataset](/docs/datasets/osm_overpass.md)
- [Graph Model](/docs/math/graph_model.md)
- [Evaluation Plan](/docs/evaluation/evaluation_plan.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
