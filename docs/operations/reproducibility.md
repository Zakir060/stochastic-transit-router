# Reproducibility

| Field | Value |
|---|---|
| Owner | DevOps Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

This document defines required metadata and execution records for reproducible routing experiments and benchmarks.

## Reproducibility checklist

| Item | Required field | Storage location | Purpose |
|:--|:--|:--|:--|
| Python runtime | version and platform | experiments/metadata | environment replay |
| Dependencies | package versions | experiments/metadata | deterministic environment |
| Raw data provenance | source URL timestamp SHA256 | data/manifests | input integrity |
| Randomness | seed values | experiment config | stochastic repeatability |

## Related

- [Evaluation plan](/docs/evaluation/evaluation_plan.md)
- [Experiment index](/experiments/metadata/experiment_index.yaml)
- [Snapshot environment script](/scripts/snapshot_environment.py)

---

Document Control

- Owner: Operations Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
