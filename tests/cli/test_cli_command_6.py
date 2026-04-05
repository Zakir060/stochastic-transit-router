# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\cli\test_cli_command_6.py
# Module          : cli.test_cli_command_6
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for cli_command_6 module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""CLI test for fit-distributions command."""

from __future__ import annotations

from typer.testing import CliRunner

from src.cli.main import app


runner = CliRunner()


def test_6__help() -> None:
    result = runner.invoke(app, ["fit-distributions", "--help"])
    assert result.exit_code == 0
    assert "fit-distributions" in result.stdout
