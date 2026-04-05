# Architecture Overview

| Field | Value |
|---|---|
| Owner | Architecture Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

High-level design of Stochastic Transit Router, explaining how data ingestion, graph construction, routing algorithms, risk evaluation, and service delivery components interact to produce reproducible route computations.

**Audience:** Algorithm researchers, software engineers, architects
**Prerequisite Knowledge:** Graph algorithms, REST APIs, configuration management



## Summary

Stochastic Transit Router is organized as a **service-oriented architecture** where a shared core business logic layer is exposed through both REST API and CLI interfaces. The system acquires data from official public sources, constructs a time-aware multigraph, and computes routes deterministically under controllable conditions for reproducibility.

**Key Insight:** API and CLI interfaces share an identical routing engine, ensuring behavior parity across deployment modes.



## System Context

| Dimension | Description |
|-----------|-------------|
| **Problem Domain** | Transit routing under travel-time uncertainty with reproducible provenance |
| **Primary Users** | Algorithm researchers, travel app developers, transportation analysts |
| **Data Ingestion** | Official GTFS feeds, real-time updates, pedestrian network data |
| **Deployment Models** | Development (CLI), production (REST API), research (batch evaluation) |
| **Reproducibility** | Deterministic seeds, versioned configurations, immutable manifests |



## Core Principles

1. **Shared Logic:** API and CLI do not duplicate routing logic; both invoke shared `RoutingService`
2. **Data Provenance:** Every data artifact records source URL, acquisition timestamp, SHA-256 hash
3. **Reproducibility:** Deterministic random seeds, configuration versioning, environment snapshots
4. **Modular Design:** Clear module boundaries with defined responsibilities and dependencies
5. **Type Safety:** Strict type hints and validation at all system boundaries



## Module Organization

### Top-Level Modules

| Module | Path | Responsibility | Key Dependencies |
|--------|------|-----------------|------------------|
| **Ingestion Pipeline** | `src/ingest` | Download, parse, validate, normalize official data feeds with provenance tracking | `src/feeds`, `src/validation`, `src/utils` |
| **GTFS Processing** | `src/gtfs` | Parse GTFS archive, build static schedule entities, validate service calendars | `src/models`, `src/graph`, `src/telemetry` |
| **GTFS Realtime** | `src/gtfs_realtime` | Apply real-time delay and alert updates to static schedule, manage feed freshness | `src/models`, `src/graph`, `src/telemetry` |
| **Graph Construction** | `src/graph` | Build time-aware multigraph, serialize/deserialize, manage dynamic updates | `src/stats`, `src/risk`, `src/optimization` |
| **Algorithms** | `src/algorithms` | Implement routing algorithms: Dijkstra, A*, Yen's K-shortest, time-dependent variants | `src/graph`, `src/optimization` |
| **Risk Evaluation** | `src/risk` | Compute risk metrics, confidence intervals, stochastic route evaluation | `src/stats` |
| **Statistics** | `src/stats` | Bootstrap inference, covariance estimation, empirical CDF, calibration | (standalone) |
| **REST API** | `src/api` | FastAPI application, route endpoints, health checks, rate limiting | `src/service`, `src/config`, `src/telemetry` |
| **CLI** | `src/cli` | Command-line interface, graph building, data acquisition, debugging tools | `src/service`, `src/config`, `src/telemetry` |
| **Core Service** | `src/service` | Routing business logic shared by API and CLI consumers | `src/graph`, `src/algorithms`, `src/risk` |
| **Configuration** | `src/config` | Hierarchical configuration: feeds, graph, risk, API, CLI settings | `src/utils` |
| **Data Models** | `src/models` | Entity definitions: Stop, Route, Trip, Edge, Node, etc. | (foundational) |



## Data Flow

### Acquisition & Preparation

```
Official Data Sources
  ├─ GTFS archive
  ├─ GTFS Realtime feed
  ├─ OpenStreetMap (Overpass API)
  └─ NYC TLC trip records
           ↓
   [Ingestion Pipeline]
   (download, parse, validate)
           ↓
   data/raw/  (original files)
       +
   data/manifests/  (provenance)
           ↓
   [Graph Construction]
   (static schedule + pedestrian network)
           ↓
   Transit Graph (in-memory)
```

### Computation & Delivery

```
Client Request
  (origin, destination, time)
           ↓
   [API/CLI Adapter]
           ↓
   [Routing Service]
   (shared logic)
           ↓
   [Algorithm Selection]
   (Dijkstra / A* / Yen's)
           ↓
   [Risk Evaluation]
   (optional stochastic metrics)
           ↓
   Response
  (path, time, alternatives, risk)
```



## Runtime Modes

The system operates in four distinct modes, each with different stability, latency, and data freshness requirements:

| Mode | Entry Point | Description | Use Case | Data Requirements |
|------|-------------|-------------|----------|-------------------|
| **Development** | CLI command group, local API | Fast iteration with debug logging, strict assertions, local artifact writing | Software development, debugging | Config files, small official data slices, local cache |
| **Production** | API service (systemd/container) | Stable low-latency routing with controlled rate limits, monitored feed freshness, error recovery | End-user applications, routing APIs | Full official feeds, validated graph artifact, real-time polling credentials |
| **Benchmark** | `benchmarks/run_all.py` | Controlled algorithm comparison with repeatable seeds, environment snapshots, memory/timing profiles | Algorithm evaluation, performance regression testing | Benchmark config, graph fixture, provenance manifest, fixed input dataset |
| **Evaluation** | `src/evaluation/experiment_runner.py` | Formal experiment execution for research questions with reproducibility evidence, statistical tests | Research publishable results, peer review | Experiment config, immutable input manifests, baseline metrics, statistical summaries |



## Cross-Cutting Quality Constraints

### Provenance & Auditability

- **Data Source Tracking:** All ingestion stages record source URL, acquisition timestamp, SHA-256 hash
- **Configuration Versioning:** Configuration artifacts include version identifier and modification history
- **Manifest Files:** Machine-readable provenance at `data/manifests/` with source lineage

### Reproducibility

- **Deterministic Seeding:** All random operations use fixed seeds during evaluation/benchmark modes
- **Graph Immutability:** Constructed graphs can be serialized and checksummed for cross-run verification
- **Environment Snapshots:** Python version, package versions, hardware specs recorded with experiment runs

### Feed Resilience

- **Dynamic Updates:** Real-time feed disruptions applied through explicit graph update policies
- **Graceful Degradation:** Missing real-time data falls back to static schedule
- **Timeout Protection:** 30-second timeout per feed fetch with bounded retry logic

### Statistical Rigor

- **Deterministic Interfaces:** Statistical modules expose deterministic interfaces (fixed seeds)
- **Uncertainty Quantification:** Risk metrics include confidence intervals and bootstrap-derived bounds
- **Bootstrap Reproducibility:** Bootstrap samples generated deterministically from immutable seed



## Service Architecture

### Shared Routing Engine

```python
class RoutingService:
    """Shared business logic for both API and CLI."""

    def compute_route(
        self,
        origin: NodeID,
        destination: NodeID,
        departure_time: int,
        algorithm: str = "dijkstra",
        include_risk: bool = False,
    ) -> RouteResult:
        """Central routing method shared by API and CLI."""
        # Validate inputs
        # Select algorithm
        # Execute routing
        # (Optionally) evaluate risk
        # Return result
```

### API Layer (FastAPI)

```
GET   /api/routes           → RoutingService.compute_route()
GET   /api/routes/topk      → RoutingService.compute_topk_routes()
GET   /api/feeds/status     → FeedManager.get_status()
GET   /api/health           → HealthCheck.perform()
```

### CLI Layer

```
python -m src.cli.main routes          → RoutingService.compute_route()
python -m src.cli.main topk-routes     → RoutingService.compute_topk_routes()
python -m src.cli.main download-data   → IngestPipeline.run()
python -m src.cli.main build-graph     → GraphBuilder.construct()
```

Both layers integrate with:
- **Configuration Manager** (loads environment-specific settings)
- **Telemetry** (logging, metrics, tracing)
- **Error Handling** (validation exceptions, timeout recovery)



## Module Boundaries & Dependencies

### Dependency Hierarchy (Low to High)

```
Level 0 (Core utilities, no project dependencies):
  - src/utils/     (helpers, caching)
  - src/models/    (Pydantic dataclasses, schemas)

Level 1 (Data and infrastructure):
  - src/feeds/     (feed definitions)
  - src/validation/ (schema validators)
  - src/stats/     (statistical modules, self-contained)

Level 2 (Domain models):
  - src/graph/     (depends on models, stats)
  - src/algorithms/ (depends on graph, stats)
  - src/risk/      (depends on algorithms, stats)

Level 3 (Data ingestion):
  - src/ingest/    (depends on models, feeds, validation)
  - src/gtfs/      (depends on models, ingest, graph)
  - src/gtfs_realtime/ (depends on models, graph)

Level 4 (Business logic):
  - src/service/   (depends on graph, algorithms, risk)

Level 5 (Interface adapters):
  - src/api/       (FastAPI, depends on service, config)
  - src/cli/       (Click, depends on service, config)
  - src/config/    (depends on models)
  - src/telemetry/ (logging, observability)
```

### No Circular Dependencies

- API and CLI depend ON service; service does NOT depend on them
- Algorithms depend ON graph; graph does NOT depend on algorithms
- Ingestion modules are pure data transformers; do NOT depend on service or API



## Configuration Management

Configuration follows a **hierarchical, environment-sensitive** approach:

```
1. defaults.yaml
   ↓
2. configs/environment-specific.yaml (dev/prod/benchmark)
   ↓
3. ~/.stochastic-transit-router/config.yaml (user overrides)
   ↓
4. Environment variables (STR_* prefix)
   ↓
5. CLI arguments (highest priority)
```

Each configuration layer merges with the previous, with later layers overriding earlier ones.



## Extensibility Points

| Extension | Mechanism | Example |
|-----------|-----------|---------|
| **New Algorithm** | Implement `RoutingAlgorithm` interface in `src/algorithms/` | Time-dependent A* variant |
| **New Risk Metric** | Add method to `RiskEvaluator` in `src/risk/` | VaR (Value at Risk) |
| **New Data Source** | Extend `DataSource` in `src/ingest/` | Real-time taxi positions |
| **Optimization** | Add configuration option in `configs/` and implement in relevant module | Graph caching strategy |



## Error Handling Strategy

| Error Type | Handling | Impact |
|-----------|----------|--------|
| **Data validation** | Pipeline stops, logs with full context | Data not loaded; service unavailable |
| **Feed timeout** | Retry with exponential backoff (max 3 attempts) | Uses stale data; latency increase |
| **Route not found** | Return empty result with reason | Client notified; suggest alternatives |
| **Configuration error** | Fail at startup with clear message | Service refuses to start |
| **API rate limit** | Queue request or return 429 | Client retries |



## Performance Considerations

| Component | Optimization Strategy | Target |
|-----------|----------------------|--------|
| **Graph Construction** | Serialize to disk after building; deserialize on startup | < 5 seconds startup |
| **Route Computation** | Early stopping in Dijkstra when destination reached | < 100ms for NYC |
| **Real-time Updates** | In-memory delay overlays, not full graph reconstruction | < 30ms per update |
| **API Response** | Async request handling with connection pooling | < 50ms p95 latency |



## Security Boundaries

| Boundary | Protection |
|----------|-----------|
| **Input validation** | Pydantic schema enforcement on all API/CLI inputs |
| **Credentials** | Environment variables only; never logged or returned in responses |
| **Rate limiting** | Per-IP token bucket on API endpoints |
| **Feed parsing** | Strict GTFS schema validation; malformed data rejected |
| **Graph state** | Immutable during routing; no race conditions in single-threaded computation |



## Related

- [Data Flow Diagram](/docs/architecture/data_flow.md) — Detailed data pipeline
- [Module Boundaries](/docs/architecture/module_boundaries.md) — Responsibility matrix
- [Runtime Modes](/docs/architecture/runtime_modes.md) — Development, production, benchmark, evaluation
- [Graph Model](/docs/math/graph_model.md) — Formal graph definition
- [Service Architecture ADR](/docs/adr/0006_service_architecture.md) — Design rationale

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
