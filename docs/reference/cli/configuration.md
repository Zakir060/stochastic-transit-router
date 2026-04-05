# CLI Reference: Configuration

| Field | Value |
|---|---|
| Owner | Dev Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This page documents how configuration files are represented in the repository and how the current CLI surfaces configuration options.

## Configuration hierarchy

Configuration files live under `configs/` and are grouped by concern:

| Area | Path prefix | Examples |
| --- | --- | --- |
| Runtime presets | `configs/*.yaml` | `configs/default.yaml`, `configs/production.yaml` |
| Feed definitions | `configs/feeds/` | `configs/feeds/mta_gtfs.yaml`, `configs/feeds/mta_realtime.yaml` |
| Graph construction | `configs/graph/` | `configs/graph/construction.yaml`, `configs/graph/walking_edges.yaml` |
| Risk and statistics | `configs/risk/`, `configs/stats/` | `configs/risk/alpha_levels.yaml`, `configs/stats/bootstrap.yaml` |
| API settings | `configs/api/` | `configs/api/feeds.yaml`, `configs/api/routes.yaml` |

## CLI options

Most CLI commands accept:

- `--config`: a path to a runtime configuration file (default: `configs/nyc.yaml`).
- `--log-level`: logging verbosity (default: `INFO`).

Example:

```powershell
python -m src.cli.main ingest-gtfs --config configs/nyc.yaml --log-level DEBUG
```

## Current limitations

The configuration loader in `src/config/` is currently scaffolded, and the CLI accepts `--config` primarily for contract stability and future wiring. Operational scripts under `scripts/` parse selected configuration files directly when needed (for example, realtime feed URL extraction).

## Related

- [CLI Reference: Commands](/docs/reference/cli/commands.md)
- [Architecture Overview](/docs/architecture/overview.md)
- [Feed Configuration: MTA Realtime](/configs/feeds/mta_realtime.yaml)

---

Document Control

- Owner: Development Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
