# ADR 0008: Benchmark protocol

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

Algorithm speed and quality claims require fair and reproducible benchmark procedures with controlled inputs and environment metadata.

## Decision

Define benchmark suites with shared query sets, common graph snapshots, explicit random seeds, and mandatory environment snapshots for each run.

## Rationale

A fixed protocol prevents cherry-picking and enables direct method comparison across code revisions and hardware contexts.

## Consequences

- Benchmark runner records machine and dependency metadata for every run.
- Benchmark sanity tests verify structural integrity of timing outputs.
- Reports reference both performance and statistical quality metrics.

## Related

- [Benchmark Protocol](/docs/evaluation/benchmark_protocol.md)
- [Benchmarks README](/benchmarks/README.md)
- [ADR 0009: Algorithm selection](/docs/adr/0009_algorithm_selection.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
