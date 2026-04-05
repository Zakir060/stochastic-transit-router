# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : benchmarks/algorithms/bench_reliability.py
# Module          : benchmarks.algorithms.bench_reliability
# Domain          : Benchmarks
# Layer           : Performance Testing
# Responsibility  : Performance benchmarks for reliability path ranking
# Public Surface  : run_case function
# Primary Inputs  : Candidate paths and tau parameter
# Primary Outputs : Reliability metric as float
# Primary Consumers: Benchmark runner, performance CI
# Owner           : Performance Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Benchmark adapter for reliability ranking."""

from __future__ import annotations

from src.algorithms.reliability_router import rank_by_reliability


def run_case(candidates: list[object], tau: int = 3600) -> float:
    """Run a benchmark case and return reliability of best candidate."""

    ranked = rank_by_reliability(candidates, tau)
    return ranked[0].reliability if ranked else 0.0
