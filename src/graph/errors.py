# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\graph\errors.py
# Module          : graph.errors
# Domain          : Graph
# Layer           : Data Structure
# Responsibility  : Implementation of errors
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Routing algorithms, API
# Owner           : Graph Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src/graph/errors.py
# Module          : graph.errors
# Domain          : Graph
# Layer           : Data Structure
# Responsibility  : Define graph-specific exceptions
# Public Surface  : Custom exception classes
# Primary Inputs  : Error conditions in graph processing
# Primary Outputs : Typed exceptions for error handling
# Primary Consumers: All graph modules
# Owner           : Graph Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""errors module."""

from __future__ import annotations


class RouterError(Exception):
    """Base domain error for stochastic-transit-router."""


class DataSourceUnavailableError(RouterError):
    """Raised when an official feed cannot be accessed."""
