# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : benchmarks/algorithms/bench_time_dependent.py
# Module          : benchmarks.algorithms.bench_time_dependent
# Domain          : Benchmarks
# Layer           : Performance Testing
# Responsibility  : Performance benchmarks for time-dependent shortest path
# Public Surface  : run_case function
# Primary Inputs  : Graph, source, target, and departure time
# Primary Outputs : Path cost as float
# Primary Consumers: Benchmark runner, performance CI
# Owner           : Performance Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Benchmark adapter for time dependent routing."""

from __future__ import annotations

from src.algorithms.time_dependent import time_dependent_shortest_path


def run_case(graph: object, source: str, target: str, departure_time: int) -> float:
    """Run a benchmark case and return path cost."""

    result = time_dependent_shortest_path(graph, source, target, departure_time)
    return result.cost
