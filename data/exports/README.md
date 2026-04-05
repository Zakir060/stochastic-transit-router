# Exports Directory

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Data |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Generated reports, metrics, and deliverables for stakeholders, operational teams, and analysis.

**Policy:** Exports are derived from processed data; automatically generated on demand; all outputs are reproducible

---

## Core Principles

| Principle | Implementation |
|-----------|-----------------|
| **Derived State** | All exports generated from processed data and manifests |
| **Reproducibility** | Export scripts linked to specific data versions |
| **Automation** | No manual intervention; all exports scriptable |
| **Versioning** | Exports timestamped; multiple versions retained for comparison |
| **Accessibility** | Formats support wide audience (CSV, JSON, HTML, PDF) |

---

## Subdirectories

### reports/

Human-readable analysis reports and insights for stakeholders.

**Purpose:** Communicate data status, quality metrics, and operational insights to non-technical audiences

**Typical Report Types:**

```
reports/
├── feed_freshness_20260405.html    # Interactive feed status report
├── data_quality_20260405.pdf       # Quality metrics and anomalies
├── pipeline_metrics_202604.csv     # Monthly performance summary
└── coverage_analysis_nyc.json      # Geographic coverage analysis
```

**Report Formats:**

- **HTML Reports:** Interactive dashboards with charts and filters
- **CSV Reports:** Tabular data for spreadsheet analysis
- **JSON Reports:** Structured output for automated systems
- **PDF Reports:** Print-friendly summaries for distribution

**Feed Freshness Report (`feed_freshness_*.html`, `feed_freshness_*.csv`):**

**Purpose:** Track data source acquisition status, staleness, and health

**Contents:**

```
Source          | Last Acquired      | Age        | Status | File Size
GTFS            | 2026-04-05 14:32   | 8 hours    | ✓      | 104 MB
GTFS Realtime   | 2026-04-05 14:32   | <1 minute  | ✓      | 2 MB
OpenStreetMap   | 2026-04-04 03:00   | 35 hours   | ⚠      | 52 MB
NYC TLC         | 2026-03-15 10:00   | 21 days    | ✓      | 4.2 GB
```

**Columns:**

| Column | Description |
|--------|-------------|
| Source | Data source identifier |
| Last Acquired | ISO 8601 timestamp of latest download |
| Age | Human-readable time since acquisition |
| Status | ✓ Fresh, ⚠ Stale, ✗ Missing |
| File Size | Size of latest download |

**Generation:**

```bash
python -m src.reports.feed_freshness \
  --manifest-dir data/manifests/runs/ \
  --output data/exports/reports/ \
  --format html,csv,json
```

**Data Quality Report (`data_quality_*.pdf`):**

**Purpose:** Quality metrics, anomalies, and recommendations

**Sections:**

1. **Data Completeness:** % of required fields populated
2. **Data Consistency:** Referential integrity checks
3. **Data Accuracy:** Outlier detection and anomaly flags
4. **Data Timeliness:** Freshness metrics
5. **Recommendations:** Suggested actions for issues

**Pipeline Metrics Report (`pipeline_metrics_*.csv`):**

**Purpose:** Track pipeline performance over time

**Columns:**

```
date,total_runs,successful_runs,failed_runs,avg_duration_seconds,data_volume_gb,errors_count
2026-04-04,24,23,1,127.5,2847.3,2
2026-04-03,24,24,0,128.2,2856.1,0
2026-04-02,24,23,1,129.8,2841.7,1
```

**Coverage Analysis Report (`coverage_analysis_*.json`):**

**Purpose:** Geographic coverage of transit network

**Structure:**

```json
{
  "report_date": "2026-04-05T14:32:00Z",
  "coverage_area": {
    "bbox": [40.5, -74.3, 40.9, -73.7],
    "cities": ["New York", "Jersey City"],
    "area_km2": 1234
  },
  "network_stats": {
    "stops": 2547,
    "routes": 351,
    "connections": 58932,
    "walkable_distance_km": 4521
  },
  "coverage_metrics": {
    "population_within_400m": 8500000,
    "employment_within_400m": 3200000,
    "school_coverage": 0.95,
    "hospital_coverage": 0.92
  }
}
```

**Generation Workflow:**

```bash
# Generate all standard reports
python scripts/generate_reports.py

# Generate specific report
python scripts/generate_reports.py --report feed_freshness

# Generate with custom date range
python scripts/generate_reports.py --start 2026-03-01 --end 2026-04-05
```

**Usage:**

```python
import json
import pandas as pd

# Load freshness report
freshness = pd.read_csv("data/exports/reports/feed_freshness_latest.csv")
stale_sources = freshness[freshness['Age (days)'] > 7]

# Load JSON report
with open("data/exports/reports/coverage_analysis_latest.json") as f:
    coverage = json.load(f)
    print(f"Population covered: {coverage['coverage_metrics']['population_within_400m']}")
```

**Archival:**

```bash
# Reports older than 90 days archived to storage
find data/exports/reports -name "*.csv" -mtime +90 | tar -czf reports_archive_Q1.tar.gz ...

# Recent reports available for quick access
ls -lt data/exports/reports/ | head -20
```

### metrics/

Machine-readable performance metrics and statistics for operational dashboards.

**Purpose:** Feed real-time and historical metrics to monitoring systems

**Contents:**

```
metrics/
├── pipeline_metrics.json         # Current pipeline status
├── data_freshness_timeline.json  # Historical freshness tracking
├── performance_benchmarks.json   # Speed and efficiency metrics
└── data_volume_trends.csv        # Storage usage over time
```

**Pipeline Metrics (`pipeline_metrics.json`):**

**Structure:**

```json
{
  "timestamp": "2026-04-05T14:32:00Z",
  "last_run": {
    "start": "2026-04-05T14:00:00Z",
    "end": "2026-04-05T14:32:00Z",
    "duration_seconds": 1920,
    "status": "success",
    "records_processed": 1250000,
    "throughput_records_per_second": 651
  },
  "cumulative": {
    "total_runs_today": 12,
    "successful": 12,
    "failed": 0,
    "success_rate": 1.0,
    "avg_duration_seconds": 1895,
    "total_records_processed_today": 15000000
  },
  "sources": {
    "gtfs": {
      "last_acquired": "2026-04-05T14:00:00Z",
      "age_seconds": 1920,
      "status": "fresh",
      "file_size_bytes": 104857600
    },
    "gtfs_realtime": {
      "last_acquired": "2026-04-05T14:32:00Z",
      "age_seconds": 0,
      "status": "live",
      "records": 12547
    }
  }
}
```

**Data Freshness Timeline (`data_freshness_timeline.json`):**

**Purpose:** Historical tracking of data staleness

**Structure:**

```json
{
  "timeline": [
    {
      "timestamp": "2026-04-05T14:00:00Z",
      "sources": {
        "gtfs": {"age_seconds": 3600, "status": "fresh"},
        "osm": {"age_seconds": 86400, "status": "fresh"},
        "tlc": {"age_seconds": 1814400, "status": "acceptable"}
      }
    },
    {
      "timestamp": "2026-04-05T15:00:00Z",
      "sources": {
        "gtfs": {"age_seconds": 7200, "status": "fresh"},
        "osm": {"age_seconds": 90000, "status": "fresh"},
        "tlc": {"age_seconds": 1818000, "status": "acceptable"}
      }
    }
  ]
}
```

**Update Frequency:** Hourly or on-demand

**Performance Benchmarks (`performance_benchmarks.json`):**

**Purpose:** Track query and pipeline performance metrics

**Structure:**

```json
{
  "benchmarks": {
    "graph_build": {
      "last_run_seconds": 45.2,
      "avg_10_runs_seconds": 44.8,
      "p95_seconds": 47.1,
      "nodes_per_second": 278000
    },
    "nearest_stop_query": {
      "last_query_ms": 0.8,
      "avg_1000_queries_ms": 0.9,
      "p95_ms": 1.2
    },
    "stop_index_build": {
      "last_run_seconds": 0.23,
      "stop_count": 2547
    }
  }
}
```

**Data Volume Trends (`data_volume_trends.csv`):**

**Purpose:** Track storage usage and growth patterns

**Structure:**

```
date,raw_data_gb,processed_data_gb,cache_data_gb,exports_data_gb,total_gb
2026-04-05,4200,500,80,15,4795
2026-04-04,4201,495,75,14,4785
2026-04-03,4197,498,82,13,4790
```

**Generation:**

```bash
# Update all metrics
python -m src.reports.metrics --export-metrics

# Stream metrics to monitoring
python -m src.reports.metrics --stream-prometheus
```

**Consumption:**

```python
import json
import requests

# Query current metrics
metrics = json.load(open("data/exports/metrics/pipeline_metrics.json"))
success_rate = metrics['cumulative']['success_rate']

# Push to Prometheus
for metric_name, value in metrics['benchmarks']['graph_build'].items():
    requests.post('http://prometheus:9091/metrics/job/transit_router',
                  data=f'graph_build_{metric_name} {value}\n')
```

---

## Export Workflow

```bash
#!/bin/bash
# Complete export generation

set -e

echo "Generating exports..."

# 1. Generate reports
echo "  → Creating analysis reports..."
python scripts/generate_reports.py --output data/exports/reports

# 2. Update metrics
echo "  → Updating operational metrics..."
python -m src.reports.metrics --export-metrics --output data/exports/metrics

# 3. Archive old exports (older than 90 days)
echo "  → Archiving historical exports..."
python scripts/archive_old_exports.py --older-than 90days

# 4. Verify exports
echo "  → Validating export integrity..."
python scripts/validate_exports.py

echo "✓ All exports generated successfully"
```

---

## Storage Management

### Retention Policy

| Export Type | Retention | Archival |
|-------------|-----------|----------|
| Reports (daily) | 90 days | Beyond 90 days → compressed archive |
| Metrics (hourly) | 7 days | Aggregated after 7 days |
| Benchmarks | 365 days | Historical performance tracking |

### Cleanup

```bash
# Archive reports older than 90 days
find data/exports/reports -mtime +90 -exec tar -czf archive_{}.tar.gz {} \;

# Remove metrics older than 7 days
find data/exports/metrics -name "*.json" -mtime +7 -delete

# Check current storage usage
du -sh data/exports/
du -sh data/exports/reports/
du -sh data/exports/metrics/
```

---

## Monitoring Integration

### Prometheus Metrics

Expose metrics for real-time monitoring:

```bash
# Start metrics exporter
python -m src.reports.metrics --prometheus-port 9091

# Scrape configuration
# prometheus.yml:
# - job_name: 'transit_router'
#   static_configs:
#     - targets: ['localhost:9091']
```

### Grafana Dashboards

Dashboard queries:

```promql
# Pipeline success rate
increase(pipeline_runs_successful[24h]) / increase(pipeline_runs_total[24h])

# Data freshness
topk(5, data_age_seconds)

# Query performance
histogram_quantile(0.95, graph_query_duration_seconds)
```

---

## Troubleshooting

### Reports Not Generating

```bash
# Check export directory permissions
ls -ld data/exports/reports/

# Verify data availability
python scripts/validate_exports.py

# Run with verbose output
python scripts/generate_reports.py --verbose --debug
```

### Metrics Missing Data

```bash
# Check metrics file age
stat data/exports/metrics/pipeline_metrics.json

# Verify source data
ls -lR data/manifests/runs/ | head -20

# Regenerate metrics
python -m src.reports.metrics --force-regenerate
```

---

## Related Documentation

- [Data Directory](/data/README.md)
- [Processed Data](/data/processed/README.md)
- [Reporting Scripts](/src/reports/)

---

Document Control

- Owner: Data Engineering Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
