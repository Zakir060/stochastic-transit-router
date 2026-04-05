# Data Directory

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Data |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Storage for raw data references, processed artifact boundaries, cache outputs, exports, and comprehensive provenance manifests.

**Policy:** All data is derived state, not version-controlled; reproducibility via manifest tracking



## Directory Structure

```
data/
├── raw/                    # Original files from official sources (git-ignored)
│   ├── gtfs/              # GTFS schedule archives
│   ├── gtfs_realtime/     # Real-time feed snapshots
│   ├── osm/               # OpenStreetMap extracts
│   └── tlc/               # NYC TLC trip records
├── processed/             # Derived artifacts (git-ignored)
│   ├── graph/             # Routable transit graphs
│   ├── training/          # ML dataset splits
│   └── indexes/           # Ingest and split indexes
├── manifests/             # Machine-readable provenance (committed)
│   ├── runs/              # Run-level provenance logs
│   ├── source_registry.yaml  # Data source catalog
│   └── splits/            # Dataset split definitions
├── cache/                 # Temporary reusable outputs (git-ignored)
│   ├── feeds/             # Parsed feed caches
│   └── indexes/           # Indexed search structures
└── exports/               # Generated reports and deliverables (git-ignored)
    ├── reports/           # Human-readable analysis reports
    └── metrics/           # Performance and data statistics
```



## Data Sources

### Official & Public

| Data Source | Coverage | Format | Volume | Freshness |
|------------|----------|--------|--------|-----------|
| **GTFS** | NYC MTA public transit | Archive (ZIP) | ~100 MB | Weekly |
| **GTFS Realtime** | NYC MTA delays and alerts | Protobuf feed | Live | 30–60 second updates |
| **OpenStreetMap** | Global pedestrian network | XML/JSON | ~50 MB (nyc extract) | Community-maintained |
| **NYC TLC** | Taxi and FHV trip records | CSV | ~50 GB / month | Monthly publication |

### Data Provenance

Every downloaded file records:
- **Source URL:** Exact endpoint (for future retrieval)
- **Acquisition Timestamp:** Unix epoch (for versioning)
- **SHA-256 Digest:** Content hash (for integrity verification)
- **Runtime Environment:** Python version, system info
- **Processing Log:** Any transformations applied

Example manifest entry:

```json
{
  "source_id": "gtfs_nyc_2026_04",
  "url": "https://new.mta.info/sites/default/files/2026-04/gtfs.zip",
  "acquired_at_utc": "2026-04-05T14:32:00Z",
  "sha256": "a1b2c3d4e5f6...",
  "file_size_bytes": 104857600,
  "retention_policy": "permanent"
}
```



## Data Preparation Workflows

### 1. Quick Start (Development)

For fast local iteration without full downloads:

```bash
# 1. Download test-mode subset
python scripts/download_official_data.py --test-mode

# 2. Build minimal graph
python scripts/build_graph_nyc.py --sample-size 0.1

# 3. Prepare splits (optional)
python scripts/prepare_data_for_training.py

# ✓ Ready to develop
```

**Time:** ~3–5 minutes
**Disk:** ~100 MB

### 2. Full Data Refresh (Production)

For complete, reproducible data:

```bash
# 1. Download all official sources
python scripts/download_official_data.py

# 2. Validate feed integrity
python scripts/check_feed_freshness.py

# 3. Build production graph
python scripts/build_graph_nyc.py --export-stats

# 4. Optional: prepare ML splits
python scripts/prepare_data_for_training.py
```

**Time:** ~30–50 minutes (network-dependent)
**Disk:** ~2 GB

### 3. Reproducible Evaluation

To reproduce exact experimental conditions:

```bash
# Use pinned manifest from prior run
python scripts/download_official_data.py \
  --manifest data/manifests/runs/2026-04-05_baseline.json

# Ensures byte-for-byte identical data across machines/times
```



## Data Format Reference

### GTFS Files

| File | Records | Purpose |
|------|---------|---------|
| `stops.txt` | ~500 | Station and stop definitions |
| `routes.txt` | ~20 | Route (line) definitions |
| `trips.txt` | ~50k | Individual service runs |
| `stop_times.txt` | ~2M | Schedule entries (stop + arrival/departure) |
| `calendar.txt` | ~30 | Service day patterns (Mon–Sun) |
| `calendar_dates.txt` | ~1k | Service exceptions (holidays, etc.) |
| `shapes.txt` | ~1M | Route shape coordinates |

**Location:** `data/raw/gtfs/` (extracted from archive)

### Graph Artifact

| Component | Format | Size |
|-----------|--------|------|
| **Nodes** | NetworkX pickle + JSON | ~1 MB |
| **Edges** | Ad jacency matrix + metadata | ~50 MB |
| **Metadata** | YAML manifest | ~1 KB |

**Location:** `data/processed/graph/nyc_latest.pkl`

### Split Manifests

For reproducible dataset splits:

```yaml
# data/processed/training/split_2026-04-05.yaml
split_date: 2026-04-05
base_data_manifest: data/manifests/runs/2026-04-05_baseline.json
ratios:
  train: 0.7
  validation: 0.15
  test: 0.15
seed: 42
splits:
  train:
    record_count: 350000
    file_references: [...]
  validation:
    record_count: 75000
    file_references: [...]
  test:
    record_count: 75000
    file_references: [...]
```

**Location:** `data/processed/training/`



## Cache & Temporary Data

### Overpass API Cache

Parsed OpenStreetMap query results cached to prevent re-fetching:

```bash
# Location: data/cache/feeds/
# Retained for: 30 days
# Cleared with: python scripts/maintenance.py --clear-cache
```

### Indexed Search

Pre-computed indexes for fast lookups:

```bash
# Location: data/cache/indexes/
# Generated by: prepare_data_for_training.py
# Format: SQLite3 database
```



## Disk Space Management

| Component | Size | Retention | Notes |
|-----------|------|-----------|-------|
| **raw/** | ~2 GB | Permanent | Don't delete; re-download is slower |
| **processed/** | ~1 GB | Until rebuilt | Safe to delete; scripts will regenerate |
| **cache/** | ~500 MB | 30 days | Auto-cleaned by maintenance task |
| **exports/** | ~100 MB | Until archived | For reports; can be regenerated |

**Total Required:** ~3.5 GB (single city)

### Cleanup

```bash
# Remove stale cache (>30 days)
python scripts/maintenance.py --cleanup-cache

# Remove all processed data (requires rebuild)
rm -rf data/processed/

# Remove cache manually
rm -rf data/cache/
```



## Data Quality & Validation

### Integrity Checks

All data passes validation:
- ✓ SHA-256 verification on download
- ✓ Schema validation against GTFS spec
- ✓ Logical constraint checks (e.g., arrival < departure)
- ✓ Cross-file referential integrity

### Freshness Monitoring

```bash
# Check age of current data
python scripts/check_feed_freshness.py

# Output: Days since acquisition + recommendations
```

### Known Limitations

| Limitation | Impact | Workaround |
|-----------|--------|-----------|
| **GTFS Realtime 60-sec lag** | Routing decisions slightly delayed | Use historical data for predictions |
| **TLC data 30-day publication delay** | No same-day feedback | Use GTFS-RT for real-time decisions |
| **OSM coverage gaps** | Some walkable paths missing | Manual data augmentation if needed |



## Related

- [Source Registry](/data/manifests/source_registry.yaml) — Complete data source catalog
- [Data Refresh Procedures](/docs/operations/data_refresh.md) — Feed update workflows
- [Reproducibility Guide](/docs/operations/reproducibility.md) — Deterministic execution
- [Scripts Directory](/scripts/README.md) — Data preparation scripts
- [Ingest Pipeline](/src/ingest/pipeline.py) — Data processing code

---

Document Control

- Owner: Data Engineering Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
