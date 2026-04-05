# Cache Directory

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Data |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Temporary reusable outputs for optimizing data pipeline performance, including parsed feed caches and indexed search structures.

**Policy:** Cached data is ephemeral; automatically regenerated when invalidated; safe to delete without data loss

---

## Core Principles

| Principle | Implementation |
|-----------|-----------------|
| **Ephemeral Nature** | Cache assumed invalid after source update; regenerates automatically |
| **Not Version-Controlled** | Excluded from git; treated as volatile intermediate state |
| **Performance Optimization** | Caches serialized parsed structures to avoid repeated parsing |
| **Automatic Cleanup** | Old cache entries removed when cache exceeds size limits |
| **Invalidation Tracking** | Manifest linked to source versions; invalidates on fresh downloads |

---

## Subdirectories

### indexes/

Pre-computed search structures and lookup tables for rapid queries.

**Contents:**

```
indexes/
├── raw_inventory.csv           # Index of all raw files in data/raw/
├── realtime_latest_per_feed.json  # Latest snapshot per real-time feed
└── stop_lookup.pkl             # Cached KD-Tree for stop nearest-neighbor
```

**File Descriptions:**

- **raw_inventory.csv:** CSV index listing all raw data files with metadata
  - Columns: `source`, `filepath`, `size_bytes`, `acquired_at_utc`, `sha256`
  - Updated on each raw data acquisition
  - Enables quick directory traversal without filesystem scan

- **realtime_latest_per_feed.json:** JSON snapshot of most recent real-time feed state
  - Keys: feed identifiers (e.g., "gtfs_rt_trip_updates", "gtfs_rt_alerts")
  - Values: timestamp, file path, content hash, record count
  - Auto-updated by real-time ingestion pipeline

- **stop_lookup.pkl:** Serialized spatial index (KD-Tree or QuadTree)
  - Enables O(log n) nearest-stop queries
  - Regenerated after GTFS updates
  - Lookups: nearest stops within distance radius to (lat, lon)

**Generation:**

```bash
# Refresh raw inventory
python scripts/inventory_raw_data.py

# Update real-time feed snapshots
python -m src.ingest.gtfs_realtime --cache-snapshot

# Build spatial lookup index
python scripts/build_stop_indexes.py
```

**Usage:**

```python
import pandas as pd
import pickle

# Query raw inventory
inventory = pd.read_csv("data/cache/indexes/raw_inventory.csv")
gtfs_files = inventory[inventory['source'] == 'gtfs']

# Load spatial index
with open("data/cache/indexes/stop_lookup.pkl", 'rb') as f:
    stop_tree = pickle.load(f)

# Find nearest 5 stops to coordinate
distances, indices = stop_tree.query([(lat, lon)], k=5)
```

**Size:** Typically <100 MB total

**Refresh Policy:**
- `raw_inventory.csv`: After each raw data download
- `realtime_latest_per_feed.json`: Continuous (real-time pipeline)
- `stop_lookup.pkl`: Weekly or after GTFS updates

---

## Cache Invalidation Strategy

### Automatic Invalidation Triggers

1. **Raw Data Update:** Cache cleared if source file SHA-256 changes
2. **Age-Based Expiry:** Entries older than 7 days auto-removed
3. **Size-Based Eviction:** If cache >1 GB, oldest entries deleted first

### Manual Cache Invalidation

```bash
# Clear all caches
rm -rf data/cache/indexes/*
rm -rf data/cache/feeds/*

# Clear specific cache
rm data/cache/indexes/stop_lookup.pkl

# Verify cache consistency
python scripts/validate_cache_integrity.py
```

---

## Performance Impact

| Cache Type | Hit Rate | Speedup |
|-----------|----------|---------|
| raw_inventory.csv | 95%+ | 100x (vs. filesystem scan) |
| realtime_latest_per_feed.json | 80%+ | 50x (vs. re-fetching) |
| stop_lookup.pkl | 90%+ | 1000x (vs. brute-force search) |

---

## Troubleshooting

### Cache Hit Rate Low

```bash
# Check cache age
ls -la data/cache/indexes/

# Verify source data hasn't changed
python scripts/check_data_staleness.py

# Regenerate caches
python scripts/rebuild_cache.py --force
```

### Cache Disk Usage Growing

```bash
# Find largest cache files
du -sh data/cache/indexes/* data/cache/feeds/*

# Clean old entries
python scripts/cleanup_old_caches.py --older-than 30days
```

### Stale Cache Causing Issues

```bash
# Check manifest linkage
python scripts/validate_cache_against_manifests.py

# Invalidate and rebuild
python scripts/rebuild_cache.py --force --verbose
```

---

## Related Documentation

- [Raw Data Directory](/data/raw/README.md)
- [Data Manifests](/data/manifests/README.md)
- [Reproducibility Guide](/docs/operations/reproducibility.md)
- [Performance Tuning](/docs/operations/performance.md)

---

Document Control

- Owner: Data Engineering Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
