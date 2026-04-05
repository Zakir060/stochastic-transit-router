# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : benchmarks/algorithms/bench_stochastic.py
# Module          : benchmarks.algorithms.bench_stochastic
# Domain          : Benchmarks
# Layer           : Performance Testing
# Responsibility  : Performance benchmarks for stochastic shortest path algorithm
# Public Surface  : run_case function
# Primary Inputs  : Graph object, source, and target nodes
# Primary Outputs : Expected path cost as float
# Primary Consumers: Benchmark runner, performance CI
# Owner           : Performance Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Benchmark adapter for stochastic shortest path."""

from __future__ import annotations

from src.algorithms.stochastic_shortest_path import stochastic_shortest_path


def run_case(graph: object, source: str, target: str) -> float:
    """Run a benchmark case and return expected cost."""

    result = stochastic_shortest_path(graph, source, target)
    return result.expected_cost
