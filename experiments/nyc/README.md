# NYC Experiments

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Research |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Baseline research experiments for New York City transit routing, evaluating deterministic routing, stochastic alternatives, and real-time disruption resilience.

**Study Lead:** Zakir Bayramov
**Period:** 2026-Q1
**City:** New York City (MTA)
**Data Version:** GTFS 2026-04-05



## Overview

This directory contains formal experiments comparing:
- Deterministic shortest path routing
- Stochastic risk-aware routing
- Real-time feed disruption handling
- Walking connector impact
- Time-of-day sensitivity

All experiments use official GTFS data for reproducible, peer-reviewable results.



## Experiments

### Experiment 1: Baseline Deterministic vs Stochastic

**Objective:** Establish baseline performance comparison between deterministic (Dijkstra) and stochastic (uncertainty-aware) routing.

**Configuration:** `configs/experiment_baseline.yaml`

**Status:** Pending

**Parameters:**
- Algorithm: Dijkstra vs Dijkstra with bootstrap uncertainty
- Query Set: 100 randomly selected origin-destination pairs
- Time Window: All times (uniform across day)
- Bootstrap Samples: 1000 (for stochastic variant)
- Confidence Level: 95%

**Hypotheses:**
1. Stochastic routes have slightly longer expected times but lower worst-case risk
2. Computation time increase is within acceptable bounds (<200 ms)
3. Path alternatives provide meaningful choice at low computation cost

**Metrics:**
- Path length (stops, distance)
- Computation time (ms)
- Confidence interval width
- Risk score distribution

**Expected Outcome:** Determine if stochastic routing overhead justifies uncertainty reduction.

### Experiment 2: Real-time Feed Disruption Resilience

**Objective:** Measure route quality degradation and recovery speed under feed delays.

**Configuration:** `configs/experiment_disruption.yaml`

**Status:** Pending

**Scenarios:**
1. Partial Outage: L Line + 4/5/6 Lines unavailable for 15 min
2. Full Service: All feeds unavailable for 30 min
3. Staggered Recovery: Feeds return one-by-one over 10 min

**Metrics:**
- Route validity (percentage of returned paths still valid)
- Detour percentage (excess travel time vs optimal)
- Time to recovery (minutes until service restoration)
- Alternative route quality

**Expected Outcome:** Quantify operational resilience and identify critical feed dependencies.

### Experiment 3: Walking Connector Impact

**Objective:** Evaluate impact of pedestrian network connectivity on route quality and computation speed.

**Configuration:** `configs/experiment_walking_impact.yaml`

**Status:** Pending

**Variants:**
1. No Walking: Transit-only edges
2. Walking 500m: Walking edges for stops <500m apart
3. Walking 1000m: Walking edges for stops <1000m apart
4. Full Walking: Historical empirical walking patterns

**Metrics:**
- Average path time
- Walking percentage of total time
- Computation time (with walking overhead)
- Route diversity (alternatives available)

**Expected Outcome:** Justify walking radius threshold choice; quantify speed/quality trade-off.

### Experiment 4: Time-of-Day Sensitivity

**Objective:** Evaluate route stability and travel time variance across peak and off-peak periods.

**Configuration:** `configs/experiment_time_sensitivity.yaml`

**Status:** Pending

**Time Windows:**
- Morning Peak: 7-10 AM (weekday)
- Midday: 11 AM-2 PM (weekday)
- Evening Peak: 3-7 PM (weekday)
- Evening: 7-10 PM (weekday)
- Night: 10 PM-6 AM (all times)

**Metrics:**
- Average travel time by period
- Variance of travel times
- Service reliability (percentage of edges available)
- Peak/off-peak ratio

**Expected Outcome:** Identify most challenging operating conditions; validate time-dependent edge models.



## Data Sources

| Source | Format | Coverage | Used In |
|--------|--------|----------|---------|
| **GTFS** | ZIP archive | All experiments | Schedule baseline |
| **GTFS Realtime** | Protobuf feed | Disruption (exp 2) | Feed delays/alerts |
| **OSM Pedestrian** | Extracted from Overpass | Experiments 1,3,4 | Walking edges |
| **Baseline Queries** | JSON | All experiments | Shared test set |

**Manifest Location:** `data/manifests/runs/2026-04-05_nyc_baseline.json`

All data pinned to explicit hash for reproducibility across sites and time periods.



## Configuration Files

### Standard Query Set

```
configs/query_set_standard.json
```

100 diverse origin-destination pairs covering:
- Peak vs off-peak times
- Geographic distribution (outer boroughs, manhattan core)
- Short vs long trips
- Different network traversal patterns

**Query structure:**

```json
[
  {
    "origin_stop_id": "123",
    "destination_stop_id": "456",
    "departure_time": 1711900000,
    "description": "Morning rush: outer Brooklyn to Manhattan"
  }
]
```



## Execution

### Run single experiment

```bash
python -m src.evaluation.experiment_runner \
  --config experiments/nyc/configs/experiment_baseline.yaml \
  --output data/exports/nyc_baseline_TIMESTAMP.json
```

### Run all NYC experiments

```bash
python -m src.evaluation.experiment_runner \
  --suite experiments/nyc/configs/suite_all.yaml
```

### With custom seed for re-execution

```bash
python -m src.evaluation.experiment_runner \
  --config experiments/nyc/configs/experiment_baseline.yaml \
  --seed 42 \
  --reproducible-mode
```



## Results & Analysis

Results are stored in: `data/exports/`

Analysis notebooks:

```
notebooks/
├── analysis_baseline.ipynb         # Deterministic vs stochastic
├── analysis_disruption.ipynb       # Feed resilience
├── analysis_walking.ipynb          # Walking impact
└── analysis_time_sensitivity.ipynb # Time-of-day patterns
```

**Generate report:**

```bash
python scripts/generate_experiment_report.py \
  --results data/exports/nyc_baseline_*.json \
  --output data/exports/reports/nyc_baseline_report.md
```



## Reproducibility

To reproduce these experiments on different machine/time:

```bash
# 1. Download exact data version
python scripts/download_official_data.py \
  --manifest data/manifests/runs/2026-04-05_nyc_baseline.json

# 2. Set seeds
export STR_SEED=42

# 3. Run with explicit configuration
python -m src.evaluation.experiment_runner \
  --config experiments/nyc/configs/experiment_baseline.yaml \
  --data-manifest data/manifests/runs/2026-04-05_nyc_baseline.json \
  --seed 42

# 4. Compare output
python scripts/compare_experiment_outputs.py \
  --baseline data/exports/nyc_baseline_2026-04-05.json \
  --verification data/exports/nyc_baseline_verification.json
```

Expected: Results identical except for execution timestamps.



## Status

| Experiment | Status | Completion | Notes |
|------------|--------|-----------|-------|
| Baseline | Pending | 2026-04-30 | Requires graph seed |
| Disruption | Pending | 2026-05-15 | Complex feed scenarios |
| Walking Impact | Pending | 2026-04-15 | Quick analysis |
| Time Sensitivity | Pending | 2026-05-01 | Calendar work |



## Publication

Intended venue: IEEE Transactions on Intelligent Transportation Systems (TITS)

Working title: "Stochastic Routing with Provenance: A Reproducible Framework for Transit Network Uncertainty"



## Related

- [Evaluation Plan](/docs/evaluation/evaluation_plan.md)
- [Experiment Root](/experiments/README.md)
- [GTFS Dataset](/docs/datasets/gtfs.md)
- [GTFS Realtime](/docs/datasets/gtfs_realtime.md)
- [Reproducibility Guide](/docs/operations/reproducibility.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: zakirbayramov942@gmail.com
