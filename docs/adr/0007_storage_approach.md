# ADR 0007: Storage approach

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

The project requires efficient storage for graph artifacts, provenance manifests, and benchmark outputs while preserving schema evolution and reproducibility.

## Decision

Use Arrow IPC or MessagePack for graph and distribution artifacts, JSONL manifests for provenance events, and keep processed outputs outside version control.

## Rationale

Arrow and MessagePack provide compact serialization with broad language support. Manifest logs in line-delimited JSON improve auditability and incremental processing.

## Consequences

- Serialization modules include schema version tags and compatibility checks.
- Processed artifacts are regenerated from raw data and manifests.
- Continuous integration validates schema contracts but does not store generated artifacts.

## Related

- [Data Flow](/docs/architecture/data_flow.md)
- [Reproducibility](/docs/operations/reproducibility.md)
- [ADR 0013: Online update policy](/docs/adr/0013_online_update_policy.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
