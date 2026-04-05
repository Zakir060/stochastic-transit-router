# Experiments Directory

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Research |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Formal experiment definitions and configurations for evaluating routing behavior on official data sources.

**Purpose:** Track reproducible research experiments with explicit provenance and version control



## Overview

This directory contains:
- **Experiment Configurations:** Defined hypotheses, parameters, and evaluation metrics
- **Metadata:** Experiment index, execution logs, run status
- **City-Specific Studies:** NYC baseline experiments, multi-city comparisons
- **Results:** Analysis outputs with provenance manifests



## Policies

All experiments must follow these standards:

| Policy | Details |
|--------|---------|
| **Execution Tracking** | Execution status explicitly recorded (pending, in-progress, completed, failed) |
| **Random Seeds** | All stochastic procedures log seeds for reproducibility |
| **Provenance** | Outputs linked to immutable data manifests and configuration versions |
| **Version Control** | Configurations committed to git; outputs stored in data/exports/ |
| **Documentation** | Experiment purpose, methodology, and limitations documented clearly |
| **Reproducibility** | Any researcher can execute experiment given configuration and seed |



## Experiment Structure

Standard directory structure for each experiment:

```
experiments/city_name/
├── configs/
│   ├── experiment_baseline.yaml      # Experiment definition
│   ├── experiment_disruption.yaml    # Disruption scenario
│   └── query_set_standard.json       # Shared query set
├── outputs/
│   └── results_TIMESTAMP.json        # Results (git-ignored)
├── notebooks/
│   └── analysis_baseline.ipynb       # Analysis notebook
└── README.md                          # Experiment documentation
```



## Core Experiment Types

### 1. Baseline Comparison

Compare deterministic vs stochastic routing:

**Configuration:**

```yaml
# experiments/nyc/configs/experiment_baseline.yaml
name: "Baseline Deterministic vs Stochastic"
description: "Compare non-stochastic routes to stochastic alternatives"
dataset:
  graph_manifest: "data/manifests/runs/2026-04-05.json"
  query_set: "experiments/nyc/configs/query_set_standard.json"
algorithms:
  - name: "dijkstra"
    params: {}
  - name: "dijkstra_stochastic"
    params:
      bootstrap_samples: 1000
      confidence_level: 0.95
queries:
  count: 100
  seed: 42
evaluation:
  metrics:
    - "path_length"
    - "computation_time"
    - "confidence_interval_width"
  timeout_seconds: 300
```

**Run experiment:**

```bash
python -m src.evaluation.experiment_runner \
  --config experiments/nyc/configs/experiment_baseline.yaml \
  --output data/exports/results_baseline_2026.json
```

### 2. Disruption Scenarios

Evaluate impact of real-time feed delays:

```yaml
# experiments/nyc/configs/experiment_disruption.yaml
name: "Real-time Feed Disruption Impact"
description: "Measure route quality degradation under feed outages"
disruptions:
  - scenario: "partial_outage"
    feeds: ["L_line", "4_5_6_lines"]
    duration_minutes: 15
  - scenario: "full_outage"
    feeds: ["all"]
    duration_minutes: 30
query_set: "experiments/nyc/configs/query_set_standard.json"
algorithms: ["dijkstra"]
evaluation:
  metrics:
    - "route_validity"
    - "detour_percentage"
    - "time_to_recovery"
```

### 3. Parameter Sensitivity

Analyze algorithm performance across parameter ranges:

```yaml
# experiments/nyc/configs/experiment_sensitivity.yaml
name: "Time-of-Day Routing Sensitivity"
description: "Evaluate route stability across departure times"
time_windows:
  - "morning_peak"        # 7-10 AM
  - "midday"              # 11 AM-2 PM
  - "evening_peak"        # 3-7 PM
  - "night"               # 7 PM-6 AM
query_set: "experiments/nyc/configs/query_set_standard.json"
algorithms: ["dijkstra"]
evaluation:
  metrics:
    - "average_travel_time"
    - "variance_by_time"
    - "service_reliability"
```



## Experiment Execution

### Single Experiment

```bash
# Run baseline experiment
python -m src.evaluation.experiment_runner \
  --config experiments/nyc/configs/experiment_baseline.yaml

# Output: data/exports/results_baseline_TIMESTAMP.json
```

### Experiment Suite

Run all experiments in a study:

```bash
# Run all NYC experiments
python -m src.evaluation.experiment_runner \
  --suite experiments/nyc/configs/suite_full.yaml

# Generates provenance manifest linking all results
```

### With Specific Data Version

Use pinned data manifest for reproducibility:

```bash
python -m src.evaluation.experiment_runner \
  --config experiments/nyc/configs/experiment_baseline.yaml \
  --data-manifest data/manifests/runs/2026-04-05_baseline.json
```



## Results & Analysis

### Output Format

```json
{
  "experiment": {
    "name": "Baseline Deterministic vs Stochastic",
    "config_hash": "a1b2c3d4e5f6...",
    "executed_at": "2026-04-05T14:32:00Z"
  },
  "environment": {
    "python_version": "3.12.0",
    "platform": "Linux-5.15.0-x86_64",
    "seed": 42
  },
  "data": {
    "graph_manifest": "data/manifests/runs/2026-04-05.json",
    "query_count": 100
  },
  "results": {
    "dijkstra": {
      "mean_time_ms": 45.2,
      "median_time_ms": 42.1,
      "max_time_ms": 156.3
    },
    "dijkstra_stochastic": {
      "mean_time_ms": 82.5,
      "confidence_intervals": [...]
    }
  },
  "artifacts": {
    "notebook": "notebooks/analysis_baseline.ipynb",
    "report": "data/exports/reports/baseline_2026.md"
  }
}
```

### Analysis Notebooks

Analysis notebooks are stored alongside experiments:

```bash
# Open analysis notebook
jupyter notebook experiments/nyc/notebooks/analysis_baseline.ipynb
```

Notebooks include:
- Descriptive statistics
- Visualization (histograms, CDFs, maps)
- Statistical tests
- Interpretation and limitations

### Publishing Results

To publish experiment results:

```bash
# 1. Complete all analyses
# 2. Commit configurations and notebooks
git add experiments/
git commit -m "Add baseline routing experiments for v0.1.0"

# 3. Export results report
python scripts/generate_experiment_report.py \
  --results data/exports/results_baseline_2026.json \
  --output data/exports/reports/baseline_report.md

# 4. Update experiment index
python scripts/update_experiment_index.py
```



## Experiment Index

Central registry of all experiments:

```yaml
# experiments/metadata/experiment_index.yaml
experiments:
  - id: "baseline_v0.1"
    name: "Baseline Deterministic vs Stochastic"
    status: "completed"
    city: "NYC"
    executed_at: "2026-04-05T14:32:00Z"
    config_file: "experiments/nyc/configs/experiment_baseline.yaml"
    results_file: "data/exports/results_baseline_2026.json"
    publication: "IEEE TITS (under review)"

  - id: "disruption_v0.1"
    name: "Real-time Feed Disruption Impact"
    status: "in-progress"
    city: "NYC"
    config_file: "experiments/nyc/configs/experiment_disruption.yaml"
    expected_completion: "2026-04-15"
```

**Query index:**

```bash
# Find all completed experiments
grep -A2 'status: "completed"' experiments/metadata/experiment_index.yaml

# Check experiment status
grep "baseline_v0.1" experiments/metadata/experiment_index.yaml
```



## Reproducibility Verification

Verify experiment reproducibility:

```bash
# Re-execute with same configuration
python -m src.evaluation.experiment_runner \
  --config experiments/nyc/configs/experiment_baseline.yaml \
  --data-manifest data/manifests/runs/2026-04-05_baseline.json \
  --seed 42

# Compare output
python scripts/compare_experiment_outputs.py \
  --baseline data/exports/results_baseline_2026.json \
  --verification data/exports/results_baseline_verification.json

# Expected: Results identical (except timestamps)
```



## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Experiment fails** | Check log for data manifest existence; verify seed logging |
| **Non-deterministic results** | Ensure seed is set; check for parallel processing |
| **Results don't match prior run** | Verify data manifest SHA-256; compare environment specs |
| **Out of memory** | Reduce query count or use smaller graph sample |
| **Stale results** | Verify timestamps match intended execution date |



## Contributing Experiments

To add a new experiment:

1. Create configuration file in `experiments/city/configs/`
2. Document methodology in `README.md`
3. Add entry to `experiments/metadata/experiment_index.yaml`
4. Run experiment and store outputs in `data/exports/`
5. Create analysis notebook in `experiments/city/notebooks/`
6. Commit configuration and notebook, NOT outputs



## Related

- [Evaluation Plan](/docs/evaluation/evaluation_plan.md)
- [Benchmark Protocol](/docs/evaluation/benchmark_protocol.md)
- [Reproducibility Guide](/docs/operations/reproducibility.md)
- [Experiment Index](/experiments/metadata/experiment_index.yaml)
- [NYC Experiments](/experiments/nyc/README.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: zakirbayramov942@gmail.com
