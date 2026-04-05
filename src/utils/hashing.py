# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\utils\hashing.py
# Module          : utils.hashing
# Domain          : Utilities
# Layer           : Infrastructure
# Responsibility  : Implementation of hashing
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: All modules
# Owner           : Infrastructure Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Hashing utilities for data provenance and artifact integrity checks."""

from __future__ import annotations

import hashlib
from pathlib import Path


def sha256_bytes(payload: bytes) -> str:
    """Return the SHA-256 hex digest for an in-memory payload."""

    digest = hashlib.sha256()
    digest.update(payload)
    return digest.hexdigest()


def sha256_file(file_path: Path) -> str:
    """Return the SHA-256 hex digest for a file.

    Raises:
        FileNotFoundError: If the path does not exist.
        IsADirectoryError: If the path points to a directory.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"File not found for hashing: {file_path}")
    if not file_path.is_file():
        raise IsADirectoryError(f"Expected file for hashing, got directory: {file_path}")

    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def module_healthcheck() -> bool:
    """Return True when deterministic hashing is operational."""

    return sha256_bytes(b"stochastic-transit-router") == (
        "48fb0d96be0a4a74f6b6e93f90ebf0535d58a6fb1d45d4e5f2f9b9f0c04f4f76"
    )
