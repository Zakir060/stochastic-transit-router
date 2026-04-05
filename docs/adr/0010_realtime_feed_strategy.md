# ADR 0010: Realtime feed strategy

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

Realtime GTFS data improves route relevance but introduces feed instability, parse uncertainty, and update propagation complexity.

## Decision

Adopt a polling-based realtime ingest strategy with configurable interval, bounded retries, strict parse error logging, and incremental graph update propagation.

## Rationale

Polling aligns with standard GTFS realtime access models and allows deterministic scheduling of update cycles, while explicit fallback behavior preserves service operation during feed interruptions.

## Consequences

- Realtime adapters must log poll timestamp, entity counts, and parse failures.
- Missing realtime access raises documented availability exceptions.
- Dynamic updater supports hot-swap edge updates without full graph rebuild for most events.

## Related

- [GTFS Realtime Dataset](/docs/datasets/gtfs_realtime.md)
- [ADR 0013: Online update policy](/docs/adr/0013_online_update_policy.md)
- [Evaluation Plan](/docs/evaluation/evaluation_plan.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
