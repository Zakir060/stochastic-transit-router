# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\benchmarks\runner.py
# Module          : benchmarks.runner
# Domain          : Benchmarking
# Layer           : Testing
# Responsibility  : Implementation of runner
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Benchmark suite execution helpers."""

from __future__ import annotations

import time

from src.api.deps import get_graph
from src.algorithms.astar import astar_shortest_path
from src.algorithms.dijkstra import dijkstra_shortest_path


def run_benchmark_suite(config_path: str) -> dict[str, float]:
    """Run small benchmark suite and return latency metrics."""

    graph = get_graph()
    start = time.perf_counter()
    dijkstra_shortest_path(graph, "A", "D")
    dijkstra_ms = (time.perf_counter() - start) * 1000

    start = time.perf_counter()
    astar_shortest_path(graph, "A", "D")
    astar_ms = (time.perf_counter() - start) * 1000

    return {
        "config_path": 0.0 if not config_path else 1.0,
        "dijkstra_ms": dijkstra_ms,
        "astar_ms": astar_ms,
    }
