# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\path_utils.py
# Module          : algorithms.path_utils
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of path utils
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Path reconstruction helpers for shortest path algorithms."""

from __future__ import annotations


def reconstruct_path(predecessor: dict[str, str], source: str, target: str) -> list[str]:
    """Reconstruct path from predecessor mapping."""

    if source == target:
        return [source]
    if target not in predecessor:
        return []
    path: list[str] = [target]
    current = target
    while current != source:
        current = predecessor[current]
        path.append(current)
    path.reverse()
    return path
