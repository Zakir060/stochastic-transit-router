# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\e2e\test_route_nyc_sample.py
# Module          : e2e.test_route_nyc_sample
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for route_nyc_sample module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""End to end sample route test."""

from __future__ import annotations

from src.algorithms.dijkstra import dijkstra_shortest_path
from src.api.deps import get_graph


def test_route_exists_and_cost_positive() -> None:
    graph = get_graph()
    result = dijkstra_shortest_path(graph, "A", "D")
    assert result.nodes[0] == "A"
    assert result.nodes[-1] == "D"
    assert result.cost > 0
