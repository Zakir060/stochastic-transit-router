# Runtime Modes

| Field | Value |
|---|---|
| Owner | Architecture Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

This document defines runtime profiles and execution constraints for development, production, benchmarking, and evaluation workloads.

## Mode summary

| Mode | Primary command | Logging level | Data requirement |
|:--|:--|:--|:--|
| development | python -m src.cli.main | DEBUG | small official slices |
| production | uvicorn src.api.app:app | INFO | full validated graph artifacts |
| benchmark | python benchmarks/run_all.py | INFO | benchmark query set and graph snapshot |
| evaluation | python -m src.cli.main evaluate | INFO | experiment configs and manifests |

## Related

- [Development config](/configs/development.yaml)
- [Production config](/configs/production.yaml)
- [Benchmark protocol](/docs/evaluation/benchmark_protocol.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
