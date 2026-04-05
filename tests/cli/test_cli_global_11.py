# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\cli\test_cli_global_11.py
# Module          : cli.test_cli_global_11
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for cli_global_11 module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Global CLI behavior test 11."""

from __future__ import annotations

from typer.testing import CliRunner

from src.cli.main import app


runner = CliRunner()


def test_global_cli_behavior_11() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Stochastic transit routing CLI" in result.stdout
