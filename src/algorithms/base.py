# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\base.py
# Module          : algorithms.base
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of base
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Base interfaces for routing algorithms."""

from __future__ import annotations

from dataclasses import dataclass

from src.models.path import PathResult


@dataclass(slots=True)
class RouteQuery:
    """Standardized route query payload."""

    source: str
    destination: str
    departure_time: int


def route_not_implemented(_: RouteQuery) -> PathResult:
    """Raise explicit error for unimplemented algorithm hooks."""

    raise NotImplementedError("Algorithm hook must be implemented in concrete module")
