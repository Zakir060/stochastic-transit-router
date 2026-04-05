# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : benchmarks/algorithms/bench_dijkstra.py
# Module          : benchmarks.algorithms.bench_dijkstra
# Domain          : Benchmarks
# Layer           : Performance Testing
# Responsibility  : Performance benchmarks for Dijkstra shortest path algorithm
# Public Surface  : run_case function
# Primary Inputs  : Graph object, source, and target nodes
# Primary Outputs : Path cost as float
# Primary Consumers: Benchmark runner, performance CI
# Owner           : Performance Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Benchmark adapter for Dijkstra routing."""

from __future__ import annotations

from src.algorithms.dijkstra import dijkstra_shortest_path


def run_case(graph: object, source: str, target: str) -> float:
    """Run a benchmark case and return path cost."""

    result = dijkstra_shortest_path(graph, source, target)
    return result.cost
