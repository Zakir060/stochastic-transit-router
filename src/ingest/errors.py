# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src/ingest/errors.py
# Module          : ingest.errors
# Domain          : Data Ingestion
# Layer           : Data Processing
# Responsibility  : Define ingest-specific exceptions
# Public Surface  : Custom exception classes
# Primary Inputs  : Error conditions in ingest processing
# Primary Outputs : Typed exceptions for error handling
# Primary Consumers: All ingest modules
# Owner           : Data Engineering Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Error types for src/ingest/errors.py."""

from __future__ import annotations


class RouterError(Exception):
    """Base domain error for stochastic-transit-router."""


class DataSourceUnavailableError(RouterError):
    """Raised when an official feed cannot be accessed."""
