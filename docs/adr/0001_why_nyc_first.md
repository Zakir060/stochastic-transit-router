# ADR 0001: Why NYC first

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

The project requires a first city with dense multimodal transit service, well-documented static and realtime feeds, extensive historical mobility data, and rich pedestrian geospatial context. A weak initial city would make algorithm validation and reproducibility difficult.

## Decision

Use New York City as the default first case study and deployment context.

## Rationale

NYC combines official MTA GTFS and GTFS realtime data, accessible TLC trip records, and robust OpenStreetMap coverage. This combination supports deterministic routing, stochastic modeling, disruption analysis, and realistic transfer walking estimates in one city context.

## Consequences

- Core configs default to nyc.
- Data ingestion adapters prioritize MTA, TLC, and NYC geospatial bounds first.
- Future city onboarding must map to the same interfaces rather than changing core algorithm code.

## Related

- [Architecture Overview](/docs/architecture/overview.md)
- [ADR 0014: City generalization](/docs/adr/0014_city_generalization.md)
- [GTFS Dataset](/docs/datasets/gtfs.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
