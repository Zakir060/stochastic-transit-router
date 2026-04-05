# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\cli\test_cli_command_4.py
# Module          : cli.test_cli_command_4
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for cli_command_4 module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""CLI test for ingest-osm command."""

from __future__ import annotations

from typer.testing import CliRunner

from src.cli.main import app


runner = CliRunner()


def test_4__help() -> None:
    result = runner.invoke(app, ["ingest-osm", "--help"])
    assert result.exit_code == 0
    assert "ingest-osm" in result.stdout
