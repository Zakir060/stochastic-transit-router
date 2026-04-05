# Benchmark Protocol

| Field | Value |
|---|---|
| Owner | Performance Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

This document defines benchmark suites and environment metadata requirements for reproducible performance comparisons.

## Benchmark suites

| Suite name | Algorithm | Graph size | Metric measured | Baseline comparison |
|:--|:--|:--|:--|:--|
| baseline shortest path | dijkstra | small to large | latency nodes expanded | bidirectional dijkstra |
| heuristic routing | astar | medium to large | latency and path cost | dijkstra |
| top k paths | yens | medium | candidate generation cost | k equals 1 shortest path |
| temporal routing | time dependent | medium | state expansion and latency | static dijkstra |
| risk aware | robust and cvar | medium | risk metric quality and latency | deterministic route |

## Environment metadata fields

| Field | Description | How recorded | File location |
|:--|:--|:--|:--|
| python_version | interpreter version | runtime probe | experiments/metadata |
| platform | OS and kernel | platform module | experiments/metadata |
| package_versions | pinned dependencies | pip freeze snapshot | experiments/metadata |
| config_hash | benchmark config fingerprint | sha256 over config files | benchmarks/results metadata |

## Related

- [Benchmarks overview](/benchmarks/README.md)
- [Snapshot environment script](/scripts/snapshot_environment.py)
- [Reproducibility requirements](/docs/operations/reproducibility.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: zakirbayramov942@gmail.com
