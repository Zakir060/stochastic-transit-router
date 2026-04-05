# Benchmarks Directory

| Field | Value |
|---|---|
| Owner | Performance Team |
| Department | Operations |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Benchmark orchestration code and configuration bundles for deterministic and stochastic routing algorithms.

**Purpose:** Measure, compare, and report performance across algorithm implementations with reproducible conditions



## Overview

This directory contains:
- **Benchmark Runner:** Main orchestration script (`run_all.py`)
- **Configuration Bundles:** Algorithm configs, graph fixtures, and test queries
- **Report Templates:** Markdown and JSON output formats
- **Sanity Tests:** Validation that benchmarks are correctly implemented



## Policy

| Policy | Details |
|--------|---------|
| **Single Query Set** | All algorithms evaluated on identical input queries (ensures fair comparison) |
| **Environment Metadata** | Record Python version, hardware specs, seed, environment at test time |
| **Artifact Management** | Outputs stored outside versioned source except templates and metadata |
| **Deterministic Execution** | Fixed random seed for reproducible results across runs |
| **Fail-Safe** | Timeout and memory limits prevent runaway processes |



## Running Benchmarks

### Standard Benchmark Suite

```bash
# Run all benchmarks (default configuration)
python benchmarks/run_all.py

# Output: benchmarks/reports/benchmark_TIMESTAMP.md
```

**Typical Duration:** 10–30 minutes (depending on algorithm complexity)

### Selective Benchmarking

```bash
# Benchmark specific algorithm
python benchmarks/run_all.py --algorithms dijkstra,astar

# Small dataset (10 queries instead of 100)
python benchmarks/run_all.py --queries small

# Verbose output
python benchmarks/run_all.py --verbose
```

### Custom Configuration

```bash
# Use custom config file
python benchmarks/run_all.py --config benchmarks/custom_config.yaml

# Override specific settings
python benchmarks/run_all.py --timeout 300 --iterations 5
```



## Benchmark Structure

### Configuration

```yaml
# benchmarks/standard_config.yaml
graph:
  source: "data/processed/graph/nyc_latest.pkl"
  snapshot_date: "2026-04-05"

queries:
  file: "benchmarks/data/standard_queries.json"
  count: 100  # Query count

algorithms:
  - name: "dijkstra"
    timeout: 60  # seconds
    params: {}

  - name: "astar"
    timeout: 60
    params:
      heuristic: "euclidean"

  - name: "yens"
    timeout: 120
    params:
      k: 5

environment:
  python_version: "3.12"
  seed: 42
  threads: 1  # Single-threaded for reproducibility
```

### Query Set

Queries are stored as JSON with departure times and origin/destination pairs:

```json
[
  {"origin": 123, "destination": 456, "departure_time": 1711900000},
  {"origin": 789, "destination": 234, "departure_time": 1711903600},
  ...
]
```

### Report Output

Generated reports include:

```markdown
# Benchmark Report – 2026-04-05 14:35:22

## Summary
- Total Queries: 100
- Environment: Python 3.12, Mac M3, 16GB RAM
- Seed: 42

## Results

### Dijkstra
- **Mean Time:** 45.2 ms
- **Median Time:** 42.1 ms
- **Max Time:** 156.3 ms
- **Total Time:** 4.52 s

### A*
- **Mean Time:** 23.5 ms
- ...
```



## Common Tasks

### Add New Algorithm to Benchmarks

1. Implement algorithm in `src/algorithms/`
2. Add configuration in `benchmarks/standard_config.yaml`
3. Add integration test in `tests/benchmark/test_algorithms.py`
4. Run: `python benchmarks/run_all.py`

### Compare Algorithm Performance

```bash
# Run baseline
python benchmarks/run_all.py --config benchmarks/baseline.yaml > baseline.txt

# Run optimized version
python benchmarks/run_all.py --config benchmarks/optimized.yaml > optimized.txt

# Compare
diff baseline.txt optimized.txt
```

### Regression Testing

Detect performance regressions in CI:

```bash
# Store baseline metrics
python benchmarks/run_all.py --export-json metrics_baseline.json

# Later: check if performance degraded
python benchmarks/run_all.py --export-json metrics_latest.json
python scripts/compare_benchmarks.py metrics_baseline.json metrics_latest.json
```



## Benchmark Validation

### Sanity Tests

Before relying on benchmark results, run sanity tests:

```bash
# Validates:
# - All algorithms return valid paths
# - Results are deterministic across runs
# - Performance is within expected ranges
python -m pytest tests/benchmark/test_benchmark_sanity.py -v
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| **Algorithm timeout** | Increase `--timeout` or simplify query set |
| **Memory exhaustion** | Use smaller graph or reduce query count |
| **Non-deterministic results** | Ensure `seed` is fixed; check for race conditions |
| **Unexpected slowdown** | Profile with `--profile` flag; check system load |



## Report Generation

### Markdown Report (Human-Readable)

```bash
python benchmarks/run_all.py --output-format markdown
# Output: benchmarks/reports/report_TIMESTAMP.md
```

### JSON Report (Machine-Parseable)

```bash
python benchmarks/run_all.py --output-format json
# Output: benchmarks/reports/report_TIMESTAMP.json
```

### Export to External Systems

```bash
# Upload to monitoring system
python benchmarks/run_all.py --export-csv metrics.csv
# Share with team
cat metrics.csv | gzip > metrics.csv.gz
```



## Performance Expectations

Typical performance ranges on NYC data (1000+ nodes and edges):

| Algorithm | Mean Time | Max Time | Notes |
|-----------|-----------|----------|-------|
| Dijkstra | 40–60 ms | 200–300 ms | Baseline; deterministic |
| A* | 20–40 ms | 150–250 ms | With euclidean heuristic |
| Yen's (K=5) | 100–150 ms | 400–600 ms | Includes path enumeration |

**Note:** Times vary by machine specs and query difficulty.



## Reproducibility Across Systems

To ensure identical benchmark results across different machines:

```bash
# 1. Use committed graph artifact
git checkout benchmarks/data/graph_seed.pkl

# 2. Fix seed
python benchmarks/run_all.py --seed 42

# 3. Document environment
python -V  # Python version
python -c "import platform; print(platform.platform())"

# Results should be identical (±1% due to system noise)
```



## Related

- [Benchmark Protocol](/docs/evaluation/benchmark_protocol.md) — Methodology and standards
- [Benchmark Runner Code](/src/benchmarks/runner.py) — Implementation details
- [Sanity Tests](/tests/benchmark/test_benchmark_sanity.py) — Validation suite
- [Standard Report Template](/benchmarks/reports/report_template.md) — Output format
- [Evaluation Plan](/docs/evaluation/evaluation_plan.md) — Research methodology

---

Document Control

- Owner: Performance Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: zakirbayramov942@gmail.com
