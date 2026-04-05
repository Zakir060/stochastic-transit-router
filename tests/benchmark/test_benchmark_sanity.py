# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\benchmark\test_benchmark_sanity.py
# Module          : benchmark.test_benchmark_sanity
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for benchmark_sanity module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Benchmark sanity tests."""

from __future__ import annotations

from src.benchmarks.runner import run_benchmark_suite


def test_benchmark_runner_returns_non_negative_timings() -> None:
    result = run_benchmark_suite("benchmarks/configs/small.yaml")
    assert result["dijkstra_ms"] >= 0
    assert result["astar_ms"] >= 0
