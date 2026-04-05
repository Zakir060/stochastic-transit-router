# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\gtfs\errors.py
# Module          : gtfs.errors
# Domain          : GTFS Processing
# Layer           : Data Processing
# Responsibility  : Implementation of errors
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Ingest pipeline
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Error types for src/gtfs/errors.py."""

from __future__ import annotations


class RouterError(Exception):
    """Base domain error for stochastic-transit-router."""


class DataSourceUnavailableError(RouterError):
    """Raised when an official feed cannot be accessed."""
