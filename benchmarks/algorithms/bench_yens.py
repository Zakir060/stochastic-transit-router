# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : benchmarks/algorithms/bench_yens.py
# Module          : benchmarks.algorithms.bench_yens
# Domain          : Benchmarks
# Layer           : Performance Testing
# Responsibility  : Performance benchmarks for Yen k-shortest paths algorithm
# Public Surface  : run_case function
# Primary Inputs  : Graph, source, target, and k parameter
# Primary Outputs : Number of discovered paths as int
# Primary Consumers: Benchmark runner, performance CI
# Owner           : Performance Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Benchmark adapter for Yen top k routing."""

from __future__ import annotations

from src.algorithms.yens import yens_k_shortest_paths


def run_case(graph: object, source: str, target: str, k: int = 5) -> int:
    """Run a benchmark case and return number of discovered paths."""

    result = yens_k_shortest_paths(graph, source, target, k)
    return len(result)
