# Stochastic Transit Router — Documentation Index

| Field | Value |
|---|---|
| Owner | Product Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

Complete documentation for system architecture, mathematical formulations, data specifications, evaluation protocols, and operational procedures.

**Intended Audiences:** Algorithm researchers, software engineers, transportation researchers, operations teams

**Estimated Total Reading Time:** 3–4 hours (for core documentation)



## Quick Navigation

### 🚀 Getting Started

- [Project README](/README.md) — Overview, quick start, data workflow
- [Contributing Guide](/CONTRIBUTING.md) — Development setup, PR workflow
- [Development Setup](/docs/contributing/development_setup.md) — Step-by-step environment configuration
- [Code Style Guide](/docs/contributing/code_style.md) — Formatting and conventions

### 🏛️ Architecture & Design

- [Architecture Overview](/docs/architecture/overview.md) — High-level system design and module organization
- [Module Boundaries](/docs/architecture/module_boundaries.md) — Responsibility matrix for each component
- [Data Flow Diagram](/docs/architecture/data_flow.md) — How data moves through the system
- [Runtime Modes](/docs/architecture/runtime_modes.md) — Development, production, benchmark, evaluation modes

### 📐 Mathematics & Algorithms

- [Graph Model](/docs/math/graph_model.md) — Formal problem definition and graph representation
- [Stochastic Routing](/docs/math/stochastic_routing.md) — Routing under uncertainty
- [Risk Metrics](/docs/math/risk_metrics.md) — Risk evaluation frameworks
- [Estimation Methods](/docs/math/estimation.md) — Statistical parameter estimation

### 📊 Datasets & Data Sources

- [GTFS (Static Schedules)](/docs/datasets/gtfs.md) — General Transit Feed Specification
- [GTFS Realtime](/docs/datasets/gtfs_realtime.md) — Real-time delays and alerts
- [OpenStreetMap (Pedestrian Network)](/docs/datasets/osm_overpass.md) — Walking edges and connectivity
- [NYC TLC (Trip Records)](/docs/datasets/nyc_tlc.md) — Taxi and for-hire vehicle data

### 🔍 Evaluation & Benchmarking

- [Evaluation Plan](/docs/evaluation/evaluation_plan.md) — Research methodology and protocols
- [Benchmark Protocol](/docs/evaluation/benchmark_protocol.md) — Performance testing and comparison

###  Operations & Reproducibility

- [Reproducibility Guide](/docs/operations/reproducibility.md) — Ensuring deterministic results across runs
- [Data Refresh Procedures](/docs/operations/data_refresh.md) — Feed update workflows and versioning

### 📚 API & CLI Reference

| Component | Resource |
|-----------|----------|
| **REST API Endpoints** | [Routes API](/docs/reference/api/routes.md), [Top-K API](/docs/reference/api/topk.md), [Feeds API](/docs/reference/api/feeds.md), [Health API](/docs/reference/api/health.md) |
| **CLI Commands** | [Commands Reference](/docs/reference/cli/commands.md), [Configuration](/docs/reference/cli/configuration.md) |
| **Graph Reference** | [Core Graph API](/docs/reference/graph/core.md), [Temporal Extensions](/docs/reference/graph/temporal.md), [Dynamic Updates](/docs/reference/graph/dynamic_updates.md), [Serialization](/docs/reference/graph/serialization.md) |
| **Ingestion** | [GTFS Ingestion](/docs/reference/ingest/gtfs.md), [Real-time Feeds](/docs/reference/ingest/realtime.md) |
| **Algorithms** | [Dijkstra](/docs/reference/algorithms/dijkstra.md), [A*](/docs/reference/algorithms/astar.md), [Time-Dependent](/docs/reference/algorithms/time_dependent.md), [Yen's K-shortest](/docs/reference/algorithms/yens.md) |
| **Statistics** | [Bootstrap Methods](/docs/reference/stats/bootstrap.md), [Covariance Estimation](/docs/reference/stats/covariance.md), [Calibration](/docs/reference/stats/calibration.md), [Empirical CDF](/docs/reference/stats/empirical_cdf.md) |

### 📋 Architecture Decision Records (ADRs)

Record of architectural decisions, including context, rationale, and consequences:

| Decision | Status | Topic |
|----------|--------|-------|
| [ADR-0001](/docs/adr/0001_why_nyc_first.md) | ✓ Accepted | Why NYC is the first deployment target |
| [ADR-0002](/docs/adr/0002_graph_representation.md) | ✓ Accepted | Graph representation choice (multigraph) |
| [ADR-0003](/docs/adr/0003_data_model.md) | ✓ Accepted | Entity data model and schema |
| [ADR-0004](/docs/adr/0004_stochastic_approximation.md) | ✓ Accepted | Stochastic approximation approach |
| [ADR-0005](/docs/adr/0005_risk_metric_choice.md) | ✓ Accepted | Risk metric selection |
| [ADR-0006](/docs/adr/0006_service_architecture.md) | ✓ Accepted | Service layer architecture (API/CLI sharing) |
| [ADR-0007](/docs/adr/0007_storage_approach.md) | ✓ Accepted | Data storage strategy |
| [ADR-0008](/docs/adr/0008_benchmark_protocol.md) | ✓ Accepted | Benchmark protocol and methodology |
| [ADR-0009](/docs/adr/0009_algorithm_selection.md) | ✓ Accepted | Algorithm selection for routing |
| [ADR-0010](/docs/adr/0010_realtime_feed_strategy.md) | ✓ Accepted | Real-time feed strategy |
| [ADR-0011](/docs/adr/0011_walking_edge_model.md) | ✓ Accepted | Walking edge connectivity model |
| [ADR-0012](/docs/adr/0012_covariance_approximation.md) | ✓ Accepted | Covariance matrix approximation |
| [ADR-0013](/docs/adr/0013_online_update_policy.md) | ✓ Accepted | Online graph update policy |
| [ADR-0014](/docs/adr/0014_city_generalization.md) | ✓ Accepted | Multi-city generalization strategy |
| [ADR-0015](/docs/adr/0015_license_choice.md) | ✓ Accepted | Open-source license choice (EUPL-1.2) |



## Documentation by Role

### 👨‍💼 Project Managers & Stakeholders
- [Project README](/README.md) — Overview and capabilities
- [Contributing Guide](/CONTRIBUTING.md) — Development process
- [Security Policy](/SECURITY.md) — Risk management

### 👨‍💻 Software Engineers

**Essential:**
1. [Architecture Overview](/docs/architecture/overview.md)
2. [Development Setup](/docs/contributing/development_setup.md)
3. [Code Style Guide](/docs/contributing/code_style.md)
4. [API Reference](/docs/reference/api/routes.md)
5. [CLI Reference](/docs/reference/cli/commands.md)

**Advanced:**
- [Data Flow Diagram](/docs/architecture/data_flow.md)
- [Graph Core API](/docs/reference/graph/core.md)
- [Database Schema Design](/docs/architecture/module_boundaries.md)

### 🔬 Algorithm & Data Scientists

**Essential:**
1. [Graph Model](/docs/math/graph_model.md)
2. [Stochastic Routing](/docs/math/stochastic_routing.md)
3. [Evaluation Plan](/docs/evaluation/evaluation_plan.md)
4. [Benchmark Protocol](/docs/evaluation/benchmark_protocol.md)

**Advanced:**
- [Risk Metrics](/docs/math/risk_metrics.md)
- [Estimation Methods](/docs/math/estimation.md)
- [Algorithm Reference](/docs/reference/algorithms/dijkstra.md)

### 🌐 Transportation & Operations Researchers

**Essential:**
1. [Evaluation Plan](/docs/evaluation/evaluation_plan.md)
2. [Dataset Documentation](/docs/datasets/gtfs.md)
3. [Reproducibility Guide](/docs/operations/reproducibility.md)
4. [Architecture Overview](/docs/architecture/overview.md)

**Advanced:**
- [Mathematical Formulations](/docs/math/graph_model.md)
- [Data Refresh Procedures](/docs/operations/data_refresh.md)



## Common Tasks

| Task | Resources |
|------|-----------|
| **Set up development environment** | [Development Setup](/docs/contributing/development_setup.md) + [README Quick Start](/README.md) |
| **Contribute code** | [Contributing Guide](/CONTRIBUTING.md) + [Code Style](/docs/contributing/code_style.md) |
| **Use the routing API** | [Routes API Reference](/docs/reference/api/routes.md) + [Getting Started](/README.md#getting-started) |
| **Understand system architecture** | [Architecture Overview](/docs/architecture/overview.md) + [Data Flow](/docs/architecture/data_flow.md) |
| **Run evaluation experiments** | [Evaluation Plan](/docs/evaluation/evaluation_plan.md) + [Reproducibility Guide](/docs/operations/reproducibility.md) |
| **Understand the graph model** | [Graph Model](/docs/math/graph_model.md) + [Algorithm Reference](/docs/reference/algorithms/dijkstra.md) |
| **Add to data processing** | [Dataset Documentation](/docs/datasets/gtfs.md) + [Data Flow](/docs/architecture/data_flow.md) |
| **Deploy in production** | [Architecture Overview](/docs/architecture/runtime_modes.md) + [Security Policy](/SECURITY.md) |



## Documentation Structure

```
docs/
├── index.md                          ← You are here
├── architecture/
│   ├── overview.md                   (system design)
│   ├── module_boundaries.md          (responsibility matrix)
│   ├── data_flow.md                  (data pipeline)
│   └── runtime_modes.md              (development/production/benchmark)
├── math/
│   ├── graph_model.md                (graph formulation)
│   ├── stochastic_routing.md         (routing under uncertainty)
│   ├── risk_metrics.md               (risk evaluation)
│   └── estimation.md                 (statistical methods)
├── datasets/
│   ├── gtfs.md                       (static transit schedules)
│   ├── gtfs_realtime.md              (real-time feeds)
│   ├── osm_overpass.md               (pedestrian network)
│   └── nyc_tlc.md                    (taxi trip data)
├── evaluation/
│   ├── evaluation_plan.md            (research protocols)
│   └── benchmark_protocol.md         (performance testing)
├── operations/
│   ├── reproducibility.md            (deterministic execution)
│   └── data_refresh.md               (feed updates)
├── contributing/
│   ├── development_setup.md          (environment setup)
│   └── code_style.md                 (formatting rules)
├── reference/
│   ├── api/                          (REST endpoints)
│   ├── cli/                          (command-line interface)
│   ├── graph/                        (graph algorithms)
│   ├── ingest/                       (data ingestion)
│   ├── algorithms/                   (routing algorithms)
│   └── stats/                        (statistical modules)
└── adr/                              (architecture decisions)
```



## Conventions

### Links

- **Internal links:** Use relative paths: `/docs/directory/file.md`
- **Code references:** Format as `` `src/module/file.py` ``
- **Functions/classes:** Format as `` `ClassName.method()` `` or `` `function_name()` ``

### Code Blocks

Use syntax highlighting with language tags:

````markdown
```python
# Python code example
```

```yaml
# Configuration example
```
````

### Notation

- **Graph:** G = (V, E) where V = nodes, E = edges
- **Time:** t = seconds since Unix epoch
- **Routes:** Path P = (v₁, v₂, ..., vₙ)
- **Risk:** R or R(P) for path risk



## Frequently Asked Questions

### Q: Where do I start?

**A:** Start with [README](/README.md) for overview, then [Development Setup](/docs/contributing/development_setup.md) for environment configuration.

### Q: How is the code organized?

**A:** See [Architecture Overview](/docs/architecture/overview.md) and [Module Boundaries](/docs/architecture/module_boundaries.md).

### Q: What data sources are used?

**A:** See [Datasets](/docs/datasets/gtfs.md) documentation for full specifications and download procedures.

### Q: How do I contribute?

**A:** Follow [Contributing Guide](/CONTRIBUTING.md) and [Code Style](/docs/contributing/code_style.md).

### Q: Is there a roadmap?

**A:** See [GitHub Issues](https://github.com/Zakir060/stochastic-transit-router/) and [Current Capabilities](/README.md#current-capabilities).

### Q: How do I report bugs?

**A:** Use [GitHub Issues](https://github.com/Zakir060/stochastic-transit-router/issues) with `[bug]` label.

### Q: How do I handle security issues?

**A:** Follow [Security Policy](/SECURITY.md) for private vulnerability reporting.



## Search Tips

When looking for information, search by:

- **Component:** e.g., "graph", "API", "CLI", "GTFS"
- **Concept:** e.g., "routing", "risk", "reproducibility", "benchmark"
- **Task:** e.g., "setup", "contribute", "deploy", "evaluate"



## Version History

| Version | Release Date | Key Changes |
|---------|--------------|-------------|
| **0.1.0** | 2026-04-05 | Initial foundational release |

See [CHANGELOG](/CHANGELOG.md) for details.



## Related

- [Project README](/README.md)
- [Contributing Guide](/CONTRIBUTING.md)
- [Security Policy](/SECURITY.md)
- [Authors](/AUTHORS.md)
- [License](/LICENSE)

---

Document Control

- Owner: Documentation Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
