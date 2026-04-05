# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : benchmarks/algorithms/bench_cvar.py
# Module          : benchmarks.algorithms.bench_cvar
# Domain          : Benchmarks
# Layer           : Performance Testing
# Responsibility  : Performance benchmarks for CVaR path ranking
# Public Surface  : run_case function
# Primary Inputs  : Candidate paths and alpha parameter
# Primary Outputs : CVaR value as float
# Primary Consumers: Benchmark runner, performance CI
# Owner           : Performance Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Benchmark adapter for CVaR ranking."""

from __future__ import annotations

from src.algorithms.cvar_router import select_min_cvar_path


def run_case(candidates: list[object], alpha: float = 0.95) -> float:
    """Run a benchmark case and return selected CVaR value."""

    selected = select_min_cvar_path(candidates, alpha)
    return selected.cvar if selected is not None else float("inf")
