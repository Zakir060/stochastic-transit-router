# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests/conftest.py
# Module          : tests.conftest
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Pytest configuration and shared fixtures
# Public Surface  : Test fixtures
# Primary Inputs  : Test requests
# Primary Outputs : Configured test environment
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Pytest configuration and shared fixtures."""

from __future__ import annotations

import random

import pytest


@pytest.fixture(autouse=True)
def deterministic_seed() -> None:
    """Ensure deterministic behavior across tests."""

    random.seed(20260405)
