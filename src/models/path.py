# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\models\path.py
# Module          : models.path
# Domain          : Data Models
# Layer           : Data Structure
# Responsibility  : Implementation of path
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: All modules using these types
# Owner           : Data Modeling Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Path result structures used across routing modules."""

from __future__ import annotations

from dataclasses import dataclass, field
import math


@dataclass(slots=True)
class PathResult:
    """Path level metrics produced by routing algorithms."""

    nodes: list[str]
    cost: float
    edges: list[str] = field(default_factory=list)
    expected_cost: float | None = None
    variance: float | None = None
    reliability: float | None = None
    cvar: float | None = None

    @property
    def sigma(self) -> float:
        """Return standard deviation from variance if available."""

        if self.variance is None or self.variance < 0:
            return 0.0
        return math.sqrt(self.variance)
