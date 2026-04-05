# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\gtfs_realtime\errors.py
# Module          : gtfs_realtime.errors
# Domain          : GTFS-Realtime
# Layer           : Data Processing
# Responsibility  : Implementation of errors
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Realtime updates, API
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src/gtfs_realtime/errors.py
# Module          : gtfs_realtime.errors
# Domain          : GTFS-Realtime
# Layer           : Data Processing
# Responsibility  : Define GTFS-Realtime-specific exceptions
# Public Surface  : Custom exception classes
# Primary Inputs  : Error conditions in realtime processing
# Primary Outputs : Typed exceptions for error handling
# Primary Consumers: All realtime processing modules
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Error types for src/gtfs_realtime/errors.py."""

from __future__ import annotations


class RouterError(Exception):
    """Base domain error for stochastic-transit-router."""


class DataSourceUnavailableError(RouterError):
    """Raised when an official feed cannot be accessed."""
