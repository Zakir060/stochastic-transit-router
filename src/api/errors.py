# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\api\errors.py
# Module          : api.errors
# Domain          : API
# Layer           : Interface
# Responsibility  : Implementation of errors
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: HTTP clients, REST consumers
# Owner           : API Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Error types for src/api/errors.py."""

from __future__ import annotations


class RouterError(Exception):
    """Base domain error for stochastic-transit-router."""


class DataSourceUnavailableError(RouterError):
    """Raised when an official feed cannot be accessed."""
