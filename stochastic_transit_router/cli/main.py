"""Compatibility CLI wrapper that forwards to the implementation in src.cli.main."""

from __future__ import annotations

from src.cli.main import app, main

__all__ = ["app", "main"]
