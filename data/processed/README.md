# Processed Data Directory

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Data |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Generated artifacts derived from raw data sources, including graphs, distributions, and evaluation outputs.

**Policy:** All artifacts reproducible from raw inputs; outputs excluded from version control



## Core Principles

| Principle | Implementation |
|-----------|-----------------|
| **Reproducibility** | Every artifact traceable to specific raw input manifests |
| **Automation** | Scripts generate outputs; no manual processing |
| **Versioning** | Manifest entries link artifacts to input data versions |
| **Cleanup** | Outputs safely deleted and regenerated when needed |



## Subdirectories

### graph/

Constructed transit graphs serialized for fast loading.

**Contents:**

```
graph/
├── nyc_20260405.pkl           # Pickled NetworkX graph
├── nyc_20260405_metadata.json # Graph metadata
└── nyc_20260405_stats.json    # Statistics and summaries
```

**File Descriptions:**

- **Graph Artifact (.pkl):** Serialized NetworkX multigraph with edge annotations
- **Metadata (.json):** Graph version, construction date, coverage area, node/edge counts
- **Statistics (.json):** Degree distribution, connectivity metrics, component sizes

**Generation:**

```bash
python scripts/build_graph_nyc.py
python scripts/build_graph_nyc.py --export-stats
```

**Usage:**

```python
import pickle
from pathlib import Path

# Load graph
graph_path = Path("data/processed/graph/nyc_20260405.pkl")
with open(graph_path, 'rb') as f:
    G = pickle.load(f)

print(f"Nodes: {len(G.nodes())} | Edges: {len(G.edges())}")
```

**Size:** ~500 MB for NYC (varies with walking radius)

**Retention:** Latest 3 versions kept (older ones safely deleted)

### distributions/

Statistical distributions fitted to historical data.

**Contents:**

```
distributions/
├── travel_time_distribution.json    # Travel time model
├── delay_model_by_line.json         # Line-specific delays
└── walking_time_model.json          # Pedestrian speed model
```

**File Format:**

```json
{
  "model_type": "empirical_cdf",
  "source_manifest": "data/manifests/runs/2026-04-05.json",
  "built_at": "2026-04-05T14:32:00Z",
  "data_points": 250000,
  "distribution": {
    "quantiles": [0.0, 0.05, 0.25, 0.50, 0.75, 0.95, 1.0],
    "values": [45, 52, 65, 78, 95, 120, 450]
  }
}
```

**Generation:**

```bash
python scripts/estimate_distributions.py --data-manifest data/manifests/runs/2026-04-05.json
```

**Usage:**

```python
import json

with open("data/processed/distributions/travel_time_distribution.json") as f:
    dist = json.load(f)

# Get median travel time
median_idx = dist["distribution"]["quantiles"].index(0.50)
median_time = dist["distribution"]["values"][median_idx]
```

### calibration/

Fitted model parameters for stochastic routing.

**Contents:**

```
calibration/
├── covariance_matrix_nyc.npy       # Numpy array
├── correlation_structure.json      # Correlation metadata
└── bootstrap_samples.pkl           # Bootstrapped estimates
```

**Purpose:** Capture travel time uncertainty for stochastic routing

**Generation:**

```bash
python scripts/calibrate_stochastic_model.py
```

### evaluation/

Pre-experiment data quality checks and reports.

**Contents:**

```
evaluation/
├── data_readiness_report.json      # Validation results
├── coverage_analysis.json          # Geographic coverage
└── feed_freshness_timeline.json    # Historical updates
```

**Example Report:**

```json
{
  "checked_at": "2026-04-05T14:32:00Z",
  "gtfs_completeness": 0.98,
  "gtfs_valid_dates": ["2026-04-05", "2026-04-06"],
  "osm_coverage_miles": 8234,
  "tlc_records_available": 12000000,
  "ready_for_evaluation": true
}
```

**Generation:**

```bash
python scripts/check_data_readiness.py
```

### training/

Dataset splits for machine learning or statistical analysis.

**Contents:**

```
training/
├── train/
│   ├── dataset_manifest.json       # Split specification
│   └── record_references.txt       # File paths
├── validation/
│   ├── dataset_manifest.json
│   └── record_references.txt
└── test/
    ├── dataset_manifest.json
    └── record_references.txt
```

**Manifest Content:**

```json
{
  "split_type": "train",
  "ratio": 0.7,
  "record_count": 350000,
  "seed": 42,
  "base_data_manifest": "data/manifests/runs/2026-04-05.json",
  "source_files": ["data/raw/tlc/yellow_*.parquet"],
  "created_at": "2026-04-05T14:32:00Z"
}
```

**Note:** Manifests reference original files by hash; no data duplication

**Generation:**

```bash
python scripts/prepare_data_for_training.py --seed 42
```



## Lifecycle

### Generation

```bash
# 1. Download raw data
python scripts/download_official_data.py

# 2. Validate raw data
python scripts/validate_raw_data.py

# 3. Generate all processed artifacts
python scripts/build_graph_nyc.py
python scripts/estimate_distributions.py
python scripts/calibrate_stochastic_model.py
python scripts/check_data_readiness.py
python scripts/prepare_data_for_training.py
```

### Verification

```bash
# Check artifacts exist and are valid
ls -lh data/processed/*/*.json data/processed/*/*.pkl

# Verify against manifest
python scripts/verify_artifacts.py
```

### Cleanup (Safe)

All processed files can be safely deleted and regenerated:

```bash
# Remove old graph versions
rm data/processed/graph/nyc_20260401.pkl
rm data/processed/graph/nyc_20260402.pkl

# Regenerate on demand
python scripts/build_graph_nyc.py
```



## Disk Space

### Current Usage

```
data/processed/
├── graph/              ~500 MB  (latest 3 versions)
├── distributions/      ~5 MB
├── calibration/        ~50 MB   (covariance matrix)
├── evaluation/         ~10 MB
└── training/           ~1 MB    (manifests only, no data)

Total: ~600 MB (can be deleted and regenerated)
```

### Retention Rules

| Folder | Keep | Delete |
|--------|------|--------|
| graph/ | Latest 3 | Older versions |
| distributions/ | Latest 2 | Pre-dated versions |
| calibration/ | Latest 1 | All others (recompute if needed) |
| evaluation/ | Latest | Older reports |
| training/ | Latest splits | Deprecated splits |

### Reclaim Space

```bash
# Remove all processed data (safe; regenerates quickly)
rm -rf data/processed/*

# Or selective cleanup
find data/processed -name "*.pkl" -mtime +30 -delete
find data/processed -name "*.npy" -mtime +60 -delete
```



## Manifest Linking

Every processed artifact links to source data:

**Example:**

```bash
# Graph artifact created from this raw snapshot
grep -l "nyc_20260405" data/manifests/runs/*.json

# Shows:
# data/manifests/runs/acquisition_2026-04-05T14.json
# {
#   "graph_version": "nyc_20260405.pkl",
#   "created_from": "gtfs_20260405.zip, osm_20260405.json",
#   "source_hashes": ["a1b2c3...", "d4e5f6..."]
# }
```



## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Artifact missing** | Regenerate: `python scripts/build_graph_nyc.py` |
| **Stale data** | Re-download raw data; regenerate processed outputs |
| **Reproduction fails** | Verify raw data manifest matches expected version |
| **Disk full** | Safe to delete processed/; recompute as needed |
| **Artifact corrupted** | Delete and regenerate from raw source |



## Related

- [Parent Data Directory](/data/README.md)
- [Raw Data Directory](/data/raw/README.md)
- [Manifests Directory](/data/manifests/README.md)
- [Scripts for Generation](/scripts/README.md)
- [Reproducibility Guide](/docs/operations/reproducibility.md)

---

Document Control

- Owner: Data Engineering Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
