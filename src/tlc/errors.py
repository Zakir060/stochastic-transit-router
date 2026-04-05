# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\tlc\errors.py
# Module          : tlc.errors
# Domain          : TLC Processing
# Layer           : Data Processing
# Responsibility  : Implementation of errors
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Data pipeline
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src/tlc/errors.py
# Module          : tlc.errors
# Domain          : TLC Processing
# Layer           : Data Processing
# Responsibility  : Define TLC-specific exceptions
# Public Surface  : Custom exception classes
# Primary Inputs  : Error conditions in TLC processing
# Primary Outputs : Typed exceptions for error handling
# Primary Consumers: All TLC processing modules
# Owner           : Data Processing Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Module errors.
"""Error types for src/tlc/errors.py."""

from __future__ import annotations


class RouterError(Exception):
    """Base domain error for stochastic-transit-router."""


class DataSourceUnavailableError(RouterError):
    """Raised when an official feed cannot be accessed."""
