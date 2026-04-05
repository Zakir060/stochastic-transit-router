# Scripts Directory

| Field | Value |
|---|---|
| Owner | Dev Team |
| Department | Development |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Operational scripts for data acquisition, graph construction, validation, feed monitoring, and environment capture.

**Purpose:** Automate repetitive workflows for reproducible data processing and artifact generation



## Overview

Scripts in this directory handle:
- **Data Acquisition:** Downloading official feeds from authorized sources with integrity verification
- **Graph Construction:** Building routable transit graphs from GTFS + pedestrian network data
- **Feed Validation:** Checking data freshness, schema compliance, and consistency
- **Environment Capture:** Recording system state for reproducibility audits
- **Data Preparation:** Splitting datasets for training, validation, and testing

All scripts:
- ✓ Record provenance metadata (source URL, timestamp, SHA-256)
- ✓ Support deterministic (seeded) execution for reproducibility
- ✓ Emit structured logs for debugging and auditing
- ✓ Fail loudly with informative error messages
- ✓ Respect configuration from `configs/` directory



## Key Scripts

| Script | Purpose | Outputs | Run Time |
|--------|---------|---------|----------|
| **download_official_data.py** | Download official raw sources and validate file integrity | `data/raw/`, `data/manifests/runs/` | ~10–30 min (network-dependent) |
| **check_feed_freshness.py** | Compute freshness report for configured sources; detect staleness | `data/cache/`, `data/exports/freshness_report.json` | ~2–5 min |
| **build_graph_nyc.py** | Generate graph seed summaries from current raw snapshots; serialize graph | `data/processed/graph/`, `data/exports/graph_stats.json` | ~5–10 min |
| **prepare_data_for_training.py** | Create training/validation/test split manifests without copying data | `data/processed/training/`, `data/cache/indexes/` | ~1 min |

### Usage Examples

#### 1. Download & Validate Data

```bash
# Download all configured feeds
python scripts/download_official_data.py

# Download specific feeds only
python scripts/download_official_data.py --feeds gtfs,osm

# Verbose logging for debugging
python scripts/download_official_data.py --verbose
```

**Output:** Full download record in `data/manifests/runs/` with SHA-256 checksums.

#### 2. Check Feed Freshness

```bash
# Generate freshness report
python scripts/check_feed_freshness.py

# Output formats: json, markdown, csv
python scripts/check_feed_freshness.py --format markdown
```

**Output:** Staleness report with recommendations for data refresh.

#### 3. Build Graph

```bash
# Build NYC transit graph from current raw data
python scripts/build_graph_nyc.py

# With statistics export
python scripts/build_graph_nyc.py --export-stats
```

**Output:** Serialized graph at `data/processed/graph/nyc_latest.pkl`, statistics summary.

#### 4. Prepare Data for ML

```bash
# Create reproducible train/val/test splits
python scripts/prepare_data_for_training.py

# Custom split ratios
python scripts/prepare_data_for_training.py --train 0.7 --val 0.15 --test 0.15

# With seed for reproducibility
python scripts/prepare_data_for_training.py --seed 42
```

**Output:** Split manifests (no data copying; manifests reference original files by hash).



## Common Workflows

### Full Data Refresh

```bash
# 1. Download latest official data
python scripts/download_official_data.py

# 2. Check freshness
python scripts/check_feed_freshness.py

# 3. Build graph
python scripts/build_graph_nyc.py

# 4. Prepare ML splits (if applicable)
python scripts/prepare_data_for_training.py
```

**Total time:** ~20–50 minutes (network-dependent)

### Development Setup

```bash
# Quick local setup with small data slices
python scripts/download_official_data.py --test-mode

# Build local graph
python scripts/build_graph_nyc.py

# Ready to develop!
```

**Total time:** ~2–3 minutes

### Research Reproducibility

```bash
# Reproduce exact environment
python scripts/download_official_data.py --manifest data/manifests/runs/2026-04-05_baseline.json

# Ensures byte-for-byte identical data
```



## Configuration

Scripts respect hierarchical configuration:

```yaml
# configs/scripts.yaml (example)
data_sources:
  gtfs:
    url: "https://new.mta.info/sites/default/files/2026-04/path/to/gtfs.zip"
    timeout: 60
  osm_overpass:
    url: "https://overpass-api.de/api/interpreter"
    query: "[bbox: 40.5,-74.3,40.9,-73.7]"
graph:
  min_walking_distance: 50  # meters
  max_walking_distance: 1500  # meters
  cache_directory: "data/cache/graphs/"
```

Override via environment variables:

```bash
export STR_DATA_SOURCES__GTFS__URL="https://custom-feed-url.com/gtfs.zip"
python scripts/download_official_data.py
```



## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Connection timeout** | Increase `--timeout` or check network connectivity |
| **SHA-256 mismatch** | Feed data may have changed; inspect `data/manifests/` for details |
| **Out of memory** | For large graphs, increase Python heap: `python -Xmx4g scripts/build_graph_nyc.py` |
| **Permission denied** | Ensure `data/` directory is writable; check file permissions |
| **Stale data error** | Run `python scripts/check_feed_freshness.py` to diagnose age |



## Environment Requirements

- **Python:** 3.12+
- **Disk Space:** ~2 GB for full NYC dataset
- **Network:** Stable connection (for downloads)
- **Memory:** 4 GB (for graph construction)



## Testing Scripts

Before running on production data, validate with test mode:

```bash
# Test download logic with small sample
python scripts/download_official_data.py --test-mode --dry-run

# Display what would be downloaded without actually downloading
```



## Monitoring & Logging

Scripts emit structured JSON logs:

```bash
# View recent logs
tail -100 logs/scripts.log | jq '.'

# Filter for errors
jq 'select(.level=="ERROR")' logs/scripts.log
```

**Log levels:** DEBUG, INFO, WARNING, ERROR, CRITICAL



## Contributing New Scripts

When adding scripts:
1. Place in `scripts/` root directory
2. Include docstring explaining purpose
3. Use consistent argument parsing (argparse or Click)
4. Record provenance metadata in `data/manifests/`
5. Add entry to this README
6. Include unit tests in `tests/scripts/`
7. Document in [Reproducibility Guide](/docs/operations/reproducibility.md) if applicable



## Related

- [Data Refresh Procedures](/docs/operations/data_refresh.md)
- [Reproducibility Guide](/docs/operations/reproducibility.md)
- [Data Directory](/data/README.md)
- [Makefile](/Makefile) — High-level workflow automation
- [Project README](/README.md) — Quick start commands

---

Document Control

- Owner: Development Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: zakirbayramov942@gmail.com
