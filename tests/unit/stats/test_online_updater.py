# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\stats\test_online_updater.py
# Module          : unit.stats.test_online_updater
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for online_updater module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for online updater."""

from __future__ import annotations

from src.stats.online_updater import OnlineMoments


def test_online_updater_updates_mean_variance() -> None:
    moments = OnlineMoments(alpha=0.5)
    moments.update(10)
    moments.update(14)
    assert moments.mean > 0
    assert moments.variance >= 0
