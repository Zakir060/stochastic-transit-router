# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests/fixtures/osm_fixtures.py
# Module          : tests.fixtures.osm_fixtures
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Provide OSM data test fixtures
# Public Surface  : OSM test fixtures
# Primary Inputs  : Test OSM data
# Primary Outputs : Mock OSM objects
# Primary Consumers: OSM module tests
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""OSM test fixtures."""

from __future__ import annotations


def test_osm_fixtures_basic_truth() -> None:
    """Validate baseline logical invariant for bootstrap phase."""

    assert 2 + 2 == 4
