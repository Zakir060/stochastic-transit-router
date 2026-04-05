# Data Manifests Directory

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Data |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Machine-readable provenance logs and contracts for reproducible data workflows.

**Purpose:** Enable auditability and reproducibility through explicit data versioning and source tracking



## Core Files

### source_registry.yaml

Central catalog of all official data sources with access specifications.

**Structure:**

```yaml
sources:
  gtfs:
    name: "MTA Static GTFS"
    description: "General Transit Feed Specification for NYC transit"
    url: "https://www.mta.info/developers"
    format: "zip"
    refresh_cadence: "weekly"
    contact: "GTFS@new.mta.info"

  gtfs_realtime:
    name: "MTA GTFS Realtime"
    description: "Real-time delays, alerts, vehicle positions"
    feeds:
      - name: "Trip Updates"
        url: "https://api-endpoint.mta.info/trip_updates"
        format: "protobuf"
      - name: "Alerts"
        url: "https://api-endpoint.mta.info/alerts"
        format: "protobuf"
    refresh_cadence: "live"
    requires_api_key: true
    api_key_env_var: "GTFS_RT_API_KEY"

  osm_overpass:
    name: "OpenStreetMap Pedestrian Network"
    description: "Street network and walking paths"
    url: "https://overpass-api.de/api/interpreter"
    format: "json"
    query: "[bbox:40.5,-74.3,40.9,-73.7];(...)"
    refresh_cadence: "monthly"

  tlc:
    name: "NYC TLC Trip Records"
    description: "Taxi and for-hire vehicle trips"
    url: "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
    format: "parquet"
    refresh_cadence: "monthly"
    lag_days: 30
```

**Usage:**

```python
import yaml

with open("data/manifests/source_registry.yaml") as f:
    registry = yaml.safe_load(f)

gtfs_url = registry["sources"]["gtfs"]["url"]
refresh_cadence = registry["sources"]["gtfs_realtime"]["refresh_cadence"]
```

### refresh_plan.yaml

Data update schedule and fallback strategies.

**Structure:**

```yaml
refresh_schedule:
  gtfs:
    day_of_week: [0, 3, 6]      # Mon, Wed, Sun
    time_utc: "02:00"            # 2 AM UTC (9 PM EST)
    max_age_days: 7
    critical: true               # Fail if >7 days old

  gtfs_realtime:
    interval: "continuous"
    max_age_minutes: 5           # Warn if >5 min old
    critical: true

  osm:
    day_of_week: [0]             # Weekly on Monday
    time_utc: "03:00"
    max_age_days: 90
    critical: false

  tlc:
    day_of_month: 15             # Mid-month
    time_utc: "10:00"
    max_age_days: 45
    critical: false

fallback_behavior:
  gtfs:
    stale_tolerance_days: 14     # Warn at 7 days, error at 14 days
    retry_strategy: "exponential_backoff"
    retry_max_attempts: 3

  gtfs_realtime:
    missing_tolerance_minutes: 10  # Switch to static schedule if >10 min outage
    use_static_fallback: true
```

**Usage:**

```python
import yaml
from datetime import datetime, timedelta

with open("data/manifests/refresh_plan.yaml") as f:
    plan = yaml.safe_load(f)

# Check if GTFS needs refresh
gtfs_max_age = plan["refresh_schedule"]["gtfs"]["max_age_days"]
# ... compare with last acquisition date
```

### provenance_schema.json

JSON Schema for raw data acquisition records.

**Structure:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Data Acquisition Provenance Record",
  "type": "object",
  "properties": {
    "source_id": { "type": "string" },
    "url": { "type": "string", "format": "uri" },
    "acquired_at_utc": { "type": "string", "format": "date-time" },
    "sha256": { "type": "string" },
    "file_size_bytes": { "type": "integer" },
    "content_type": { "type": "string" },
    "http_status": { "type": "integer" },
    "etag": { "type": "string" },
    "retention_policy": { "enum": ["permanent", "30_days", "90_days"] }
  },
  "required": ["source_id", "url", "acquired_at_utc", "sha256"]
}
```

### manifest_schema.json

JSON Schema for ingest run manifests (high-level data workflow records).

**Structure:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Ingest Run Manifest",
  "type": "object",
  "properties": {
    "run_id": { "type": "string" },
    "started_at": { "type": "string", "format": "date-time" },
    "completed_at": { "type": "string", "format": "date-time" },
    "status": { "enum": ["success", "partial", "failed"] },
    "data_sources": {
      "type": "array",
      "items": { "type": "string" }  # References to provenance records
    },
    "outputs": {
      "type": "object",
      "properties": {
        "graph_path": { "type": "string" },
        "graph_stats": { "type": "object" }
      }
    }
  }
}
```



## Subdirectories

### runs/

Timestamped records of each data acquisition or processing run.

**File Naming:** `ingest_YYYY-MM-DDTHH-MM-SSZ.json` or `acquisition_YYYY-MM-DDTHH-MM-SSZ.jsonl`

**Typical Entry:**

```json
{
  "run_id": "ingest_2026-04-05T14-32-00Z",
  "started_at": "2026-04-05T14:30:00Z",
  "completed_at": "2026-04-05T14:45:00Z",
  "status": "success",
  "data_sources": [
    {
      "source_id": "gtfs_20260405",
      "url": "https://www.mta.info/sites/default/files/2026-04/gtfs.zip",
      "acquired_at_utc": "2026-04-05T14:32:00Z",
      "sha256": "a1b2c3d4e5f6g7h8i9j0...",
      "file_size_bytes": 104857600
    },
    {
      "source_id": "osm_nyc",
      "acquired_at_utc": "2026-04-05T14:40:00Z",
      "sha256": "z9y8x7w6v5u4t3s2r1q0..."
    }
  ],
  "outputs": {
    "graph": {
      "path": "data/processed/graph/nyc_20260405.pkl",
      "nodes": 12547,
      "edges": 58932,
      "generation_time_seconds": 45.2
    }
  },
  "environment": {
    "python_version": "3.12.0",
    "platform": "Linux-5.15.0-x86_64",
    "hostname": "research-vm-01"
  }
}
```

**Use Cases:**

```bash
# Find all runs for a specific date
grep -l "2026-04-05" data/manifests/runs/*.json

# List completed runs in order
ls -lt data/manifests/runs/ingest_*.json

# Check most recent run
cat $(ls -t data/manifests/runs/ingest_*.json | head -1)
```

### splits/

Dataset split definitions for reproducible train/test separation.

**File Format:** `split_YYYY-MM-DDTHH-MM-SSZ_SEED.json`

**Typical Entry:**

```json
{
  "split_id": "split_2026-04-05T14-32-00Z_42",
  "created_at": "2026-04-05T14:32:00Z",
  "base_data_manifest": "data/manifests/runs/ingest_2026-04-05T14-32-00Z.json",
  "seed": 42,
  "ratios": {
    "train": 0.7,
    "validation": 0.15,
    "test": 0.15
  },
  "record_counts": {
    "train": 350000,
    "validation": 75000,
    "test": 75000
  },
  "manifests": {
    "train": "data/processed/training/train/dataset_manifest.json",
    "validation": "data/processed/training/validation/dataset_manifest.json",
    "test": "data/processed/training/test/dataset_manifest.json"
  }
}
```



## Workflows

### Single Acquisition

```bash
# Capture raw data provenance
python -m src.ingest.download_gtfs

# Creates: data/manifests/runs/acquisition_TIMESTAMP.jsonl
# Each line: one provenance record

# Verify integrity
python scripts/verify_provenance.py data/manifests/runs/acquisition_*.jsonl
```

### Full Ingest Run

```bash
# Complete workflow with manifest
python scripts/download_official_data.py

# Creates: data/manifests/runs/ingest_TIMESTAMP.json
# Contains: all sources, output artifacts, environment info
```

### Query Provenance

```python
import json
from pathlib import Path

# Find manifest for specific graph version
manifests_dir = Path("data/manifests/runs")
for manifest_file in sorted(manifests_dir.glob("ingest_*.json")):
    with open(manifest_file) as f:
        manifest = json.load(f)

    if "nyc_20260405.pkl" in str(manifest["outputs"]):
        print(f"Graph created by: {manifest_file.name}")
        print(f"Sources: {manifest['data_sources']}")
        break
```



## Validation

### Check Manifest Integrity

```bash
# Validate schema
python -m jsonschema \
  -i data/manifests/runs/ingest_2026-04-05T14-32-00Z.json \
  data/manifests/manifest_schema.json

# Check all manifests
find data/manifests/runs -name "*.json" -exec \
  python -m jsonschema -i {} data/manifests/manifest_schema.json \;
```

### Audit Provenance Chain

```bash
# Trace artifact origin
python scripts/trace_artifact_provenance.py \
  data/processed/graph/nyc_20260405.pkl
```



## Related

- [Data Directory](/data/README.md)
- [Raw Data](/data/raw/README.md)
- [Processed Data](/data/processed/README.md)
- [Provenance Helpers](/src/ingest/provenance.py)
- [Reproducibility Guide](/docs/operations/reproducibility.md)

---

Document Control

- Owner: Data Engineering Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
