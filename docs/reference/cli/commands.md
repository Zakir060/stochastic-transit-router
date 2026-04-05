# CLI Reference: Commands

| Field | Value |
|---|---|
| Owner | Dev Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

The command-line interface is implemented with Typer and provides a thin wrapper around a subset of the ingest and routing functionality.

## Entry point

The CLI is currently invoked as a Python module:

```powershell
python -m src.cli.main --help
```

## Command summary

| Command | Purpose | Primary modules |
| --- | --- | --- |
| `ingest-gtfs` | Index GTFS raw directory and write an ingest manifest. | [src/ingest/pipeline.py](/src/ingest/pipeline.py) |
| `ingest-gtfs-realtime` | Index realtime raw directory and write an ingest manifest. | [src/ingest/pipeline.py](/src/ingest/pipeline.py) |
| `ingest-tlc` | Index TLC raw directory and write an ingest manifest. | [src/ingest/pipeline.py](/src/ingest/pipeline.py) |
| `ingest-osm` | Index OSM raw directory and write an ingest manifest. | [src/ingest/pipeline.py](/src/ingest/pipeline.py) |
| `build-graph` | Build or load the in-memory graph and print a status summary. | [src/api/deps.py](/src/api/deps.py), [src/graph/core.py](/src/graph/core.py) |
| `fit-distributions` | Placeholder for distribution fitting workflow. | (scaffold) |
| `route` | Compute a single deterministic shortest path. | [src/algorithms/dijkstra.py](/src/algorithms/dijkstra.py) |
| `route-topk` | Compute top-$k$ loopless paths. | [src/algorithms/yens.py](/src/algorithms/yens.py) |
| `benchmark` | Placeholder benchmark runner. | (scaffold) |
| `evaluate` | Placeholder evaluation runner. | (scaffold) |
| `report` | Placeholder report renderer. | (scaffold) |
| `validate-datasets` | Placeholder dataset validation runner. | (scaffold) |

## Operational guidance

For end-to-end data acquisition and reproducible artifact generation, prefer the repository scripts under `scripts/`.

```powershell
python scripts/download_official_data.py
python scripts/check_feed_freshness.py
python scripts/prepare_data_for_training.py
```

## Implementation

- Typer app: [src/cli/main.py](/src/cli/main.py)

## Related

- [CLI Reference: Configuration](/docs/reference/cli/configuration.md)
- [Scripts](/scripts/README.md)
- [Documentation Index](/docs/index.md)

---

Document Control

- Owner: Development Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
