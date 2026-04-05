# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\utils\test_hashing.py
# Module          : unit.utils.test_hashing
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for hashing module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for file and payload hashing utilities."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from src.utils.hashing import sha256_bytes, sha256_file


def test_sha256_bytes_matches_known_digest() -> None:
    payload = b"abc"
    assert sha256_bytes(payload) == hashlib.sha256(payload).hexdigest()


def test_sha256_file_matches_content_digest(tmp_path: Path) -> None:
    data_file = tmp_path / "payload.bin"
    payload = b"transit-data"
    data_file.write_bytes(payload)
    assert sha256_file(data_file) == hashlib.sha256(payload).hexdigest()


def test_sha256_file_missing_path_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        sha256_file(tmp_path / "missing.bin")
