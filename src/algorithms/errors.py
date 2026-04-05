# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\algorithms\errors.py
# Module          : algorithms.errors
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Implementation of errors
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing service
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src/algorithms/errors.py
# Module          : algorithms.errors
# Domain          : Algorithms
# Layer           : Computation
# Responsibility  : Define algorithm-specific exceptions
# Public Surface  : Custom exception classes
# Primary Inputs  : Error conditions in algorithm execution
# Primary Outputs : Typed exceptions for error handling
# Primary Consumers: All algorithm modules
# Owner           : Algorithm Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Module errors.
"""Error types for src/algorithms/errors.py."""

from __future__ import annotations


class RouterError(Exception):
    """Base domain error for stochastic-transit-router."""


class DataSourceUnavailableError(RouterError):
    """Raised when an official feed cannot be accessed."""
