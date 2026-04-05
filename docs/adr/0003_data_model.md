# ADR 0003: Data model

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

The repository consumes heterogeneous data formats including GTFS text tables, GTFS realtime protobuf payloads, Parquet trip records, and OSM Overpass JSON documents. Inconsistent structures increase ingestion risk and reduce testability.

## Decision

Define canonical internal models with explicit field types and validation logic for each data family, then map source-specific records into those canonical models.

## Rationale

Canonical modeling isolates source volatility, enables strict schema and contract testing, and ensures downstream algorithms receive consistent typed structures.

## Consequences

- Ingestion modules must include schema validation and mapping layers.
- Contract schemas are versioned and tested independently.
- Parsing errors become explicit and traceable instead of implicit runtime faults.

## Related

- [Data Flow](/docs/architecture/data_flow.md)
- [GTFS Dataset](/docs/datasets/gtfs.md)
- [GTFS Realtime Dataset](/docs/datasets/gtfs_realtime.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
