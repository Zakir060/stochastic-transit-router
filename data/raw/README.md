# Raw Data Directory

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Data |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Exclusive location for original, unmodified official source files downloaded from public data providers.

**Policy:** Original files preserved as-is; transformation happens in data/processed/



## Core Rules

| Rule | Rationale |
|------|-----------|
| **Keep originals unchanged** | Enables auditing and re-processing without re-downloading |
| **Record SHA-256 hash** | Verifies content integrity; detects corruption |
| **Log acquisition timestamp** | Enables version control; identifies stale data |
| **Do not commit large files** | Unnecessary in git; provenance manifest sufficient |
| **One source per subdirectory** | Clear organization and responsibility separation |



## Subdirectories

### gtfs/

Static transit schedule archives from official MTA sources.

**Source:** https://www.mta.info/developers

**File Format:** ZIP archives containing GTFS text files

**Contents:**
- `stops.txt` - Station and stop definitions
- `routes.txt` - Route (line) definitions
- `trips.txt` - Service run instances
- `stop_times.txt` - Schedule entries
- `calendar.txt` - Service day patterns
- `calendar_dates.txt` - Service exceptions
- `shapes.txt` - Route geometry

**Typical File:**
```
gtfs_20260405.zip    (~100 MB)
```

**Download:**
```bash
python scripts/download_official_data.py --feeds gtfs
```

### gtfs_realtime/

Real-time feed snapshots from ongoing MTA services.

**Source:** Configured in configs/feeds.yaml

**Format:** Protocol Buffer (text or binary representation)

**Types:**
- `trip_updates.pb` - Delay and cancellation alerts
- `alerts.pb` - Service notifications
- `vehicle_positions.pb` - Vehicle location updates

**Note:** Real-time feeds continuously update; snapshots are point-in-time captures

**Capture:**
```bash
python scripts/download_official_data.py --feeds gtfs_realtime
```

### tlc/

NYC Taxi and Limousine Commission trip records.

**Source:** https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

**Format:** Parquet (columnar, compressed)

**Coverage:**
- Yellow taxi trips (all medallion cabs)
- For-hire vehicle (FHV) trips (e.g., Uber, Lyft)
- High-volume FHV trips (Uber/Lyft aggregates)

**Typical File:**
```
yellow_tripdata_202604.parquet    (~650 MB / month)
fhv_tripdata_202604.parquet       (~400 MB / month)
```

**Volume:** ~50 GB per month for all types

**Retention:** 12 months rolling

**Download:**
```bash
python scripts/download_official_data.py --feeds tlc --months 12
```

### osm/

OpenStreetMap pedestrian network data for NYC.

**Source:** Overpass API (https://overpass-api.de/)

**Format:** JSON (OSM node/way/relation structure)

**Query:** Bounding box extraction for NYC metro area

**Typical File:**
```
osm_nyc_pedestrian_20260405.json (~150 MB)
```

**Contents:**
- Street network (ways)
- Intersection nodes
- Metadata (names, types, access restrictions)

**Query Example:**
```
[bbox:40.5,-74.3,40.9,-73.7];
(
  way["highway"~"residential|tertiary|secondary|primary"];
  way["type"="multipolygon"];
);
out geom;
```

**Download:**
```bash
python scripts/download_official_data.py --feeds osm
```



## Provenance Tracking

### Capture Method

Each download records:

```json
{
  "source_id": "gtfs_20260405",
  "url": "https://www.mta.info/sites/default/files/2026-04/gtfs.zip",
  "acquired_at_utc": "2026-04-05T14:32:00Z",
  "sha256": "a1b2c3d4e5f6...",
  "file_size_bytes": 104857600,
  "content_type": "application/zip",
  "http_status": 200,
  "etag": "\"abc123def456\"",
  "retention_policy": "permanent"
}
```

**Stored in:** `data/manifests/runs/acquisition_TIMESTAMP.jsonl`

### Verification

Verify file integrity:

```bash
# Check against known hash
sha256sum data/raw/gtfs/gtfs_20260405.zip

# Compare to provenance
grep "a1b2c3d4e5f6" data/manifests/runs/acquisition_*.jsonl
```



## Disk Space Management

### Current Usage

```
data/raw/
├── gtfs/               ~100 MB   (1-2 GTFS archives)
├── gtfs_realtime/     ~10 MB    (snapshots, regularly cleaned)
├── tlc/               ~500 MB   (12 months rolling)
└── osm/               ~150 MB   (1-2 extracts)

Total: ~750 MB - 1 GB
```

### Retention Policy

| Folder | Retention | Refresh Cadence |
|--------|-----------|-----------------|
| gtfs/ | Permanent | Weekly (MTA updates) |
| gtfs_realtime/ | 30 days | Continuous (live feed) |
| tlc/ | 12 months | Monthly (1-30 day lag) |
| osm/ | Latest only | Quarterly (OSM changes) |

### Cleanup

```bash
# Remove old GTFS Realtime snapshots (>30 days)
find data/raw/gtfs_realtime/ -mtime +30 -delete

# Remove outdated OSM extracts
find data/raw/osm/ -name "*_*.json" -mtime +90 -delete

# Check disk usage
du -sh data/raw/*/
```



## Access & Scripts

### Download All Data

```bash
# Full download (all feeds, all available history)
python scripts/download_official_data.py

# Specific feeds only
python scripts/download_official_data.py --feeds gtfs,osm

# Test mode (small samples)
python scripts/download_official_data.py --test-mode

# Dry run (no download, show plan)
python scripts/download_official_data.py --dry-run
```

### Validate Data

```bash
# After download, validate against schemas
python scripts/validate_raw_data.py

# Check file sizes and formats
python scripts/audit_raw_data.py
```

### Inspect Files

```bash
# List GTFS contents
unzip -l data/raw/gtfs/gtfs_*.zip | head -20

# Peek at CSV structure
head -5 data/raw/gtfs/*.txt

# Check Parquet schema
python -c "import pandas as pd; print(pd.read_parquet('data/raw/tlc/yellow_*.parquet').dtypes)"

# Parse OSM JSON
python -c "import json; d=json.load(open('data/raw/osm/osm_*.json')); print(f'{len(d[\"elements\"])} OSM elements')"
```



## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Download fails** | Check network; verify source URL is accessible; see configs/feeds.yaml |
| **SHA-256 mismatch** | File may be corrupted; delete and re-download |
| **Disk full** | Remove old snapshots; check du -sh for space hogs |
| **File locked** | Another process reading; wait or restart Python |
| **Out of date** | Re-run download script; check last acquisition timestamp |



## Related

- [Parent Data Directory](/data/README.md)
- [Provenance Tracking](/src/ingest/provenance.py)
- [Data Manifests](/data/manifests/README.md)
- [Dataset Documentation](/docs/datasets/gtfs.md)
- [GTFS Realtime](/docs/datasets/gtfs_realtime.md)
- [Scripts Directory](/scripts/README.md)

---

Document Control

- Owner: Data Engineering Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
