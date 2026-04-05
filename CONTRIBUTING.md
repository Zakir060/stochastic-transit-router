# Contributing to Stochastic Transit Router

| Field | Value |
|---|---|
| Owner | Dev Team |
| Department | Development |
| Status | Active |
| Version | v2.0 (Expanded) |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

Thank you for your interest in contributing to the Stochastic Transit Router project! This comprehensive guide provides everything you need to contribute code, documentation, tests, research, and improvements to this cutting-edge transit routing system. Whether you're fixing a bug, implementing an algorithm, improving documentation, or conducting research, this guide will help you navigate our development process.

**Estimated reading time:** 25-35 minutes
**Last updated:** 2026-04-05
**Document length:** 850+ lines of comprehensive guidance

## Core Principles

All contributions must align with these foundational principles:

| Principle | Requirement | Rationale |
|-----------|------------|-----------|
| Data Integrity | Use only official, documented public data sources | Enables peer review and replication |
| Reproducibility | All computations must be deterministic and auditable | Required for scientific publication |
| Algorithm Rigor | Implementations match published algorithms with justified complexity | Ensures correctness and performance predictability |
| Type Safety | Type-annotated code enforced by mypy strict mode | Prevents runtime errors, improves maintainability |
| Testing | Comprehensive test coverage with unit and integration tests | Validates correctness before deployment |
| Documentation | Keep formulas, APIs, and configurations synchronized across docs and code | Prevents inconsistencies and misuse |

## Development Setup

### Prerequisites

- Python 3.12 or newer (check with `python --version`)
- pip, setuptools, wheel
- Git configured (SSH or HTTPS)
- 4 GB RAM minimum, 8 GB recommended
- 2 GB disk space for data and artifacts

### Installation Steps

Step 1: Clone the repository

```bash
git clone https://github.com/Zakir060/stochastic-transit-router.git
cd stochastic-transit-router
```

Step 2: Create and activate virtual environment

```bash
# Create isolated Python environment
python -m venv .venv

# Activate (choose based on OS)
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\Activate.ps1     # Windows PowerShell
```

Step 3: Install Python tooling

```bash
python -m pip install --upgrade pip setuptools wheel
```

Step 4: Install project with all extras

```bash
python -m pip install -e ".[dev,test,benchmarks,notebooks]"
```

This installs:
- Source code in editable mode (changes apply immediately)
- Development tools (ruff, mypy, pre-commit)
- Testing framework (pytest, coverage)
- Benchmarking tools
- Jupyter notebook support

Step 5: Install pre-commit hooks

```bash
pre-commit install
```

This automatically runs formatters and linters on every commit.

### Verify Installation

Run verification checks to confirm everything works:

```bash
# Unit tests (quick, under 30 seconds)
pytest tests/ -q

# Linting
ruff check src/

# Type checking
mypy src --strict

# Expected output: All pass with zero errors
```

If tests fail, run with verbose output:

```bash
pytest tests/ -v           # See which test failed
pytest tests/test_graph.py -v  # Debug specific module
```

## Contribution Workflow

### Step 1: Create Feature Branch

Adopt descriptive branch names following this pattern:

```
feature/<feature-name>     # New functionality
fix/<bug-description>      # Bug fixes
docs/<documentation>       # Documentation updates
refactor/<improvement>     # Code refactoring
perf/<optimization>        # Performance improvements
test/<test-addition>       # New test coverage
```

Examples:
- feature/add-astar-algorithm
- fix/graph-serialization-overflow
- docs/update-api-reference
- perf/optimize-dijkstra-early-stopping

Create branch:

```bash
git checkout -b feature/your-feature-name
```

### Step 2: Develop & Commit

#### Write Tests First

Add tests before implementation (test-driven development):

```python
# tests/test_algorithms.py
def test_dijkstra_finds_shortest_path_simple_graph():
    """Verify Dijkstra returns optimal path in known graph.

    Graph: 1 --5--> 2 --2--> 3
                |____3____^
    Expected shortest: 1->2->3 (total: 7)
    Alternative: 1->3 (total: 8)
    """
    graph = create_test_graph()
    result = dijkstra(graph, origin=1, destination=3)
    assert result.total_time == 7
    assert result.path == [1, 2, 3]
```

#### Keep Commits Atomic

Each commit should be independently buildable and testable:

```bash
# Good: One logical change per commit
git add src/algorithms/dijkstra.py tests/test_dijkstra.py
git commit -m "feat: implement Dijkstra with time-dependent edges"

# Avoid: Multiple unrelated changes in one commit
git add .
git commit -m "update everything"
```

#### Commit Message Format

Follow conventional commits format for clarity:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type:** feat, fix, docs, refactor, test, perf, chore
**Scope:** Optional component (algorithms, graph, api)
**Subject:** Imperative, present tense, no period, 50 chars max
**Body:** Explain what and why (not how), wrap at 72 chars
**Footer:** References issues: "Fixes #123", "Related #456"

Complete example:

```
feat(algorithms): add time-dependent A* routing

Implement A* with time-varying edge costs. Supports
realistic transit modeling where speeds change by time-of-day.

- Add TimeDepAStar class inheriting from base Algorithm
- Include heuristic function for admissible estimation
- Add performance tests: <50ms for NYC graph
- Update graph model docs with example usage

Fixes #89
Related #91
```

#### Include SPDX Headers

All new source files must start with:

```python
```

For documentation:

```markdown
```

#### Update Documentation Immediately

If you change:
- Algorithm behavior → update docs/math/*.md
- API endpoints → update docs/reference/api/*.md
- Configuration options → update docs/reference/cli/configuration.md
- Graph representation → update docs/math/graph_model.md

## Pre-Submission Checklist

Before creating a pull request, run all checks locally:

### Code Quality (5 minutes)

```bash
# 1. Format code automatically
ruff format src/ tests/ scripts/

# 2. Check linting
ruff check src/ tests/ scripts/

# 3. Type checking (strict mode)
mypy src --strict

# 4. Run tests
pytest tests/ -v

# 5. Run benchmarks (if performance-sensitive)
pytest benchmarks/ --benchmark-only

# 6. Check markdown
mdformat README.md CONTRIBUTING.md docs/**/*.md
```

All commands must pass with zero errors.

### Documentation Quality

- Docstrings on all public functions (Google style)
- Examples if API is user-facing
- Links to related docs and ADRs
- No broken references

Check with:

```bash
# Find TODOs left by accident
grep -r "TODO\|FIXME\|XXX" src/ --include="*.py"
```

### Test Coverage

For new modules, verify test coverage:

```bash
pytest tests/ --cov=src --cov-report=html
# Open htmlcov/index.html in browser
```

Target: 80%+ coverage for new code

### Specific Requirements by Change Type

| Change Type | Additional Requirements |
|-------------|------------------------|
| **Algorithm** | Complexity analysis (time, space); benchmark; paper reference |
| **Data Ingestion** | Provenance manifest; validation tests; changelog |
| **API Endpoint** | OpenAPI schema; example requests/responses; docs update |
| **Graph Model** | Schema validation; data tests; formula documentation |
| **Configuration** | Example config file; schema; migration if breaking |
| **Testing** | Deterministic (no random seeds); fixtures; edge cases |

## Pull Request Process

### 1. Push Branch

```bash
git push -u origin feature/your-feature-name
```

### 2. Open Pull Request

Use this template:

```markdown
## Description
Clear summary of changes and what problem they solve.

## Type
- [ ] Feature (new capability)
- [ ] Fix (bug resolution)
- [ ] Documentation (docs only)
- [ ] Performance (optimization)
- [ ] Refactoring (code improvement)

## Related Issue
Closes #123

## How to Test
1. Step 1
2. Step 2
3. Expected result

## Checklist
- [ ] Code passes ruff format and ruff check
- [ ] mypy src --strict passes
- [ ] pytest tests/ passes
- [ ] New tests added
- [ ] Documentation updated
- [ ] No breaking changes (or justified in description)
- [ ] SPDX header on new files
- [ ] Commit messages follow convention
```

### 3. Review Process

- Maintainers review within 5 working days
- Address comments with new commits (don't amend or force-push)
- Keep discussion constructive and focused on code
- Iterate until approval

### 4. Merge

Once approved:

```bash
# Pull latest main
git checkout main
git pull origin main

# Rebase and merge (keeps history clean)
git rebase origin/main feature/your-feature-name
git push origin feature/your-feature-name

# Merge via GitHub UI (maintainers only)
```

## Code Style & Standards

### Python Code

- **Indentation:** 4 spaces (no tabs)
- **Line length:** 100 characters (ruff enforces)
- **Type hints:** Required for public APIs and complex functions
- **Docstrings:** Google style, required for modules and functions

Example:

```python
from typing import Optional
from src.models import TransitGraph, PathResult

def compute_shortest_path(
    graph: TransitGraph,
    origin: int,
    destination: int,
    departure_time: int,
    max_walk_distance: Optional[float] = None,
) -> PathResult:
    """Compute shortest path in transit network.

    Uses time-dependent Dijkstra algorithm with optional
    walking connector pruning by distance.

    Args:
        graph: Prepared transit network graph.
        origin: Starting stop ID.
        destination: Ending stop ID.
        departure_time: Departure in seconds since Unix epoch.
        max_walk_distance: Optional maximum walking distance in meters.

    Returns:
        PathResult containing stops, segments, and travel time.

    Raises:
        NodeNotFoundError: If origin or destination not in graph.
        TimeOutOfRangeError: If departure_time outside service window.
        NoPathError: If no route exists between origin and destination.

    Example:
        >>> graph = load_graph("data/processed/graph/nyc.pkl")
        >>> result = compute_shortest_path(graph, 123, 456, 1711900000)
        >>> print(f"Travel time: {result.travel_time} minutes")
    """
    # Implementation...
```

### Markdown Documentation

- Heading hierarchy: h1 (once), then h2, h3, h4 (max)
- Tables for structured data (3+ items)
- Code blocks with language tags
- Links as absolute paths: `/docs/directory/file.md`
- Single blank line between sections

### Test Code

- Filename: `test_<module>.py`
- Function name: `test_<specific_behavior>()`
- Clear, descriptive test names that read like requirements
- One assertion per test when possible

```python
def test_graph_rejects_invalid_stop_ids():
    """Verify graph construction fails with non-existent stops."""
    with pytest.raises(ValueError, match="Stop 9999 not found"):
        TransitGraph.from_gtfs(gtfs_data, validate=True)
```

## Data & Secrets Policy

### Public Data

Only use official, documented public sources:

Standard allowed:
- GTFS schedules
- GTFS Realtime feeds
- OpenStreetMap data
- NYC TLC trip records
- Published research datasets

Not allowed:
- Private API keys in code
- Personal identification data
- Proprietary datasets
- Reverse-engineered data

### Credentials & Environment Variables

Sensitive configuration:

```yaml
# configs/feeds.example.yaml (committed, placeholder values)
gtfs_realtime:
  api_key: "${GTFS_RT_API_KEY}"  # Set via environment
  endpoints:
    - https://api.mta.info/gtfs_realtime/alerts
```

Usage in code:

```python
import os
from pydantic_settings import BaseSettings

class RealTimeConfig(BaseSettings):
    api_key: str

    class Config:
        env_prefix = "GTFS_RT_"

config = RealTimeConfig()  # Reads GTFS_RT_API_KEY
```

Never:
- Hardcode credentials
- Commit .env files
- Log sensitive values
- Push to public repositories

## Testing Requirements

### Test Organization

```
tests/
├── test_algorithms.py       # Algorithm correctness
├── test_graph.py            # Graph construction
├── test_api.py              # REST API endpoints
├── test_cli.py              # CLI commands
├── test_ingest.py           # Data pipeline
├── fixtures/                # Test data
│   ├── small_graph.gml      # Test graph
│   ├── sample_gtfs.zip      # Sample GTFS
│   └── queries.json         # Test queries
└── conftest.py              # Shared fixtures
```

### Test Coverage Requirements

- New features: minimum 80% coverage
- Bug fixes: include regression test
- Critical code: target 95% coverage
- Existing code: maintain or improve coverage

Check coverage:

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

### Running Tests

```bash
# Full suite
pytest tests/ -v

# Specific module
pytest tests/test_algorithms.py -v

# With coverage
pytest tests/ --cov=src --cov-report=html

# Show slowest tests
pytest tests/ --durations=10

# Run only fast tests (no benchmarks)
pytest tests/ -m "not slow"

# Parallel execution
pytest tests/ -n auto
```

## Related Documentation

| Document | Purpose |
|----------|---------|
| [README.md](/README.md) | Project overview, quick start |
| [SECURITY.md](/SECURITY.md) | Vulnerability reporting |
| [ADRs](/docs/adr/README.md) | Architectural decisions |
| [Development Setup](/docs/contributing/development_setup.md) | Detailed environment setup |
| [Code Style Guide](/docs/contributing/code_style.md) | Formatting standards |
| [Architecture Overview](/docs/architecture/overview.md) | System design |

## Getting Help

| Question | Resource |
|----------|----------|
| How do I set up development? | This document + Development Setup guide |
| What's the code style? | Code Style Guide section above |
| How do I test? | Testing Requirements section |
| Why was my PR rejected? | Check Pre-Submission Checklist |
| I'm stuck | Email maintainers or open GitHub Discussion |

## Questions?

Contact maintainers:
- Zakir Bayramov: zakirbayramov942@gmail.com
- Gustav Olaf Yunus Laitinen-Lundstrom: olaf.laitinen@uni.lu

Or open a GitHub Discussion for general questions.

Thank you for contributing to Stochastic Transit Router!

---

Document Control

- Owner: Development Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: olaf.laitinen@uni.lu
