# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\ingest\test_provenance.py
# Module          : unit.ingest.test_provenance
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for provenance module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for provenance event utilities."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
from pathlib import Path

import pytest

from src.ingest.provenance import (
    append_provenance_event,
    build_provenance_event,
    read_provenance_events,
)


def test_build_provenance_event_computes_hash_and_size(tmp_path: Path) -> None:
    data_file = tmp_path / "sample.bin"
    payload = b"gtfs-snapshot"
    data_file.write_bytes(payload)

    event = build_provenance_event(
        file_path=data_file,
        dataset_id="mta_gtfs",
        source_url="https://www.mta.info/developers",
        access_method="http_download",
        acquired_at=datetime(2026, 4, 5, tzinfo=timezone.utc),
    )

    assert event.dataset_id == "mta_gtfs"
    assert event.size_bytes == len(payload)
    assert event.sha256 == hashlib.sha256(payload).hexdigest()
    assert event.local_path.endswith("sample.bin")


def test_append_and_read_provenance_events_roundtrip(tmp_path: Path) -> None:
    data_file = tmp_path / "sample.parquet"
    data_file.write_bytes(b"parquet-content")
    log_file = tmp_path / "provenance.jsonl"

    event = build_provenance_event(
        file_path=data_file,
        dataset_id="nyc_tlc",
        source_url="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
        access_method="html_listing_then_parquet_download",
    )
    append_provenance_event(log_file, event)

    events = read_provenance_events(log_file)
    assert len(events) == 1
    assert events[0].dataset_id == "nyc_tlc"
    assert events[0].sha256 == event.sha256


def test_build_provenance_event_missing_file_raises(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        build_provenance_event(
            file_path=missing_file,
            dataset_id="missing",
            source_url="https://example.invalid",
            access_method="none",
        )
