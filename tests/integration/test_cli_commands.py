# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\integration\test_cli_commands.py
# Module          : integration.test_cli_commands
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for cli_commands module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Integration tests for CLI commands."""

from __future__ import annotations

from typer.testing import CliRunner

from src.cli.main import app


runner = CliRunner()


def test_route_command_success() -> None:
    result = runner.invoke(app, ["route", "A", "D"])
    assert result.exit_code == 0
    assert "route completed" in result.stdout


def test_route_topk_command_success() -> None:
    result = runner.invoke(app, ["route-topk", "A", "D", "--k", "2"])
    assert result.exit_code == 0
    assert "route-topk completed" in result.stdout
