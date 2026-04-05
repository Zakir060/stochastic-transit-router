# Notebooks Directory

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Research |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Reproducible Jupyter notebooks for exploratory analysis, algorithm development, and research evaluation.

**Purpose:** Distribute analysis, visualization, and experiment results with full provenance tracking



## Overview

Notebooks in this directory:
- ✓ Are aligned with experiment configurations and provenance manifests
- ✓ Can be reproduced deterministically (seeded, versioned data)
- ✓ Include explanation, code, and visualizations
- ✓ Reference data via manifests (not hardcoded paths)
- ✓ Document methodology and limitations



## Usage

### Prerequisites

Install notebook dependencies:

```bash
pip install jupyterlab notebook jupyter-lab ipykernel
```

### Running Notebooks

```bash
# Start Jupyter server
jupyter lab notebooks/

# Or with direct notebook opening
jupyter notebook notebooks/exploration/graph_analysis.ipynb
```

### Environment Setup

Each notebook imports and validates the reproducibility environment:

```python
# Cell 1: Setup and validation
import os
from pathlib import Path
from src.reproducibility import load_manifest, set_seed

# Load experiment manifest for reproducibility
manifest = load_manifest("data/manifests/runs/experiment_2026-04-05.json")

# Set deterministic seed
set_seed(manifest["seed"])

print(f"Graph Version: {manifest['graph_version']}")
print(f"Data Snapshot: {manifest['data_date']}")
```



## Organization

### Exploratory Notebooks

Quick investigations and algorithm development:

```
notebooks/exploration/
├── graph_visualization.ipynb      # Visualize NYC transit graph
├── data_statistics.ipynb          # Data histograms and summaries
├── algorithm_comparison.ipynb     # Performance profiles (non-reproducible)
└── route_sampling.ipynb           # Sample routes for manual inspection
```

### Evaluation Notebooks

Formal results for research papers and reports:

```
notebooks/evaluation/
├── benchmark_results_v0.1.ipynb   # Reproducible benchmark analysis
├── risk_metric_validation.ipynb   # Stochastic routing results
└── baseline_comparison.ipynb      # Comparison against baselines
```

### Data Preparation Notebooks

Dataset preparation and quality checks:

```
notebooks/data_preparation/
├── gtfs_validation.ipynb          # GTFS schema validation
├── osm_coverage_analysis.ipynb    # Pedestrian network coverage
└── outlier_detection.ipynb        # Anomaly detection in trip data
```



## Reproducibility Standards

### Notebook Reproducibility Checklist

- [ ] First cell loads and validates experiment manifest
- [ ] Deterministic seed set via `set_seed()` call
- [ ] Data paths reference manifests, not hardcoded paths
- [ ] All dependencies listed in first "Setup" cell
- [ ] Cell execution order does not matter (if restarted)
- [ ] Random number generation uses fixed seed
- [ ] Output saved to `data/exports/notebooks/` with manifest entry

### Example Template

```python
# notebooks/templates/reproducible_template.ipynb

# Cell 1: Setup
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.reproducibility import load_manifest, set_seed
import json

# Cell 2: Load manifest
manifest = load_manifest("data/manifests/runs/baseline_2026-04.json")
set_seed(manifest["seed"])

# Cell 3: Analysis
# ... your code ...

# Cell 4: Export results
results = {...}
export_path = Path("data/exports/notebooks/results_20260405.json")
export_path.parent.mkdir(parents=True, exist_ok=True)
with open(export_path, 'w') as f:
    json.dump(results, f)
```



## Working with Data

### Load Graph from Manifest

```python
from src.graph import load_graph
from src.reproducibility import load_manifest

manifest = load_manifest("data/manifests/runs/2026-04-05.json")
graph = load_graph(manifest["graph_path"])

print(f"Loaded graph with {len(graph.nodes())} nodes")
```

### Load Query Set

```python
import json

# From benchmark configuration
with open("benchmarks/data/standard_queries.json") as f:
    queries = json.load(f)

for q in queries[:10]:
    print(f"{q['origin']} -> {q['destination']} @ {q['departure_time']}")
```

### Generate Route Statistics

```python
from src.evaluation import compute_route_stats
from src.algorithms import dijkstra

# Compute routes for all queries
results = []
for q in queries:
    route = dijkstra(graph, q['origin'], q['destination'], q['departure_time'])
    results.append(compute_route_stats(route))

# Analyze
import pandas as pd
df = pd.DataFrame(results)
print(df.describe())
```



## Visualization

### Common Plots

#### Route on Map

```python
import folium
from src.graph import get_node_coordinates

# Create map centered on origin
coords = get_node_coordinates(graph, route.path[0])
m = folium.Map(location=[coords.lat, coords.long], zoom_start=12)

# Add route polyline
route_coords = [
    (get_node_coordinates(graph, n).lat, get_node_coordinates(graph, n).long)
    for n in route.path
]
folium.PolyLine(route_coords, color='blue', weight=2).add_to(m)
m.save('route_map.html')
```

#### Algorithm Performance Comparison

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Histogram of times
axes[0].hist(dijkstra_times, bins=50, alpha=0.7, label='Dijkstra')
axes[0].hist(astar_times, bins=50, alpha=0.7, label='A*')
axes[0].set_xlabel('Time (ms)')
axes[0].set_ylabel('Frequency')
axes[0].legend()

# CDF plot
axes[1].plot(sorted(dijkstra_times), label='Dijkstra')
axes[1].plot(sorted(astar_times), label='A*')
axes[1].set_xlabel('Rank')
axes[1].set_ylabel('Time (ms)')
axes[1].legend()

plt.tight_layout()
plt.savefig('performance_comparison.png', dpi=150)
```



## Sharing & Publishing

### Export for Reports

```bash
# Convert notebook to HTML for sharing
jupyter nbconvert --to html \
  notebooks/evaluation/benchmark_results_v0.1.ipynb \
  --output benchmark_report.html

# Or PDF
jupyter nbconvert --to pdf --PDFExporter.preprocessors=[...] notebook.ipynb
```

### Include in Documentation

```markdown
<!-- In docs/ -->
## See Also

- [Algorithm Performance Analysis](../../notebooks/evaluation/benchmark_results_v0.1.ipynb)
- [Data Quality Report](../../notebooks/data_preparation/gtfs_validation.ipynb)
```



## Kernel & Environment

### Recommended Kernel

Use project virtual environment:

```bash
# Install kernel in venv
python -m ipykernel install --user --name stochastic-router \
  --display-name "Stochastic Router"

# Select kernel in Jupyter:
# Kernel → Change Kernel → stochastic-router
```

### Check Environment

In first cell:

```python
import sys
import platform
print(f"Python: {sys.version}")
print(f"Platform: {platform.platform()}")

# Verify imports work
import src
from src.graph import TransitGraph
print("✓ All imports successful")
```



## Version Control

### Include in Git

```bash
# Add notebooks
git add notebooks/**/*.ipynb
git commit -m "Add analysis notebooks for v0.1.0"
```

### Clean Before Commit

```bash
# Remove execution outputs (keeps code, removes large outputs)
jupyter nbconvert --clear-output --inplace notebooks/**/*.ipynb

# Or use nbstripout
nbstripout notebooks/**/*.ipynb
```



## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Import errors** | Ensure kernel is set to project venv; restart kernel |
| **Stale data** | Re-run `load_manifest()` cell and restart kernel |
| **Non-reproducible results** | Check that `set_seed()` is called early; no parallel processing |
| **Slow execution** | Use smaller query set; profile with `%prun` magic |



## Related

- [Experiment Index](/experiments/metadata/experiment_index.yaml)
- [Reproducibility Guide](/docs/operations/reproducibility.md)
- [Evaluation Plan](/docs/evaluation/evaluation_plan.md)
- [Data Directory](/data/README.md)
- [Project README](/README.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
