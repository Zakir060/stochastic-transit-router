# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\e2e\test_topk_nyc_sample.py
# Module          : e2e.test_topk_nyc_sample
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for topk_nyc_sample module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""End to end top-k sample route test."""

from __future__ import annotations

from src.algorithms.yens import yens_k_shortest_paths
from src.api.deps import get_graph


def test_topk_returns_paths() -> None:
    graph = get_graph()
    paths = yens_k_shortest_paths(graph, "A", "D", 2)
    assert len(paths) >= 1
    assert all(path.cost > 0 for path in paths)
