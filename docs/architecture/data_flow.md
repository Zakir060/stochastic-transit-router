# Data Flow

| Field | Value |
|---|---|
| Owner | Architecture Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

This document describes how official datasets flow from acquisition through validation, graph construction, routing, and evaluation artifacts.

## Pipeline stages

| Stage | Input | Output | Module | Cache strategy |
|:--|:--|:--|:--|:--|
| Acquire | Official feed endpoints | Raw files in data/raw | src/ingest/pipeline.py | SHA based local cache |
| Validate | Raw records | Validated canonical rows | src/validation/schema_validator.py | Per file schema hash |
| Transform | Canonical rows | Graph and distribution features | src/graph/builder.py and src/tlc/feature_extractor.py | Incremental by manifest |
| Serve | Graph and stats artifacts | API and CLI route responses | src/api and src/cli | In memory graph snapshot |

## Related

- [Architecture overview](/docs/architecture/overview.md)
- [GTFS dataset](/docs/datasets/gtfs.md)
- [Reproducibility](/docs/operations/reproducibility.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
