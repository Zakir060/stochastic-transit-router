# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\ingest\test_pipeline.py
# Module          : unit.ingest.test_pipeline
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for pipeline module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for raw indexing pipeline functions."""

from __future__ import annotations

from pathlib import Path

from src.ingest.manifest import read_ingest_manifest
from src.ingest.pipeline import discover_raw_files, index_raw_dataset
from src.ingest.provenance import read_provenance_events


def test_discover_raw_files_skips_gitkeep(tmp_path: Path) -> None:
    raw_root = tmp_path / "raw"
    raw_root.mkdir()
    (raw_root / ".gitkeep").write_text("", encoding="utf-8")
    (raw_root / "agency.txt").write_text("agency_id,agency_name\n1,MTA\n", encoding="utf-8")

    nested = raw_root / "sub"
    nested.mkdir()
    (nested / "stops.txt").write_text("stop_id,stop_name\n1,Stop\n", encoding="utf-8")

    files = discover_raw_files(raw_root)
    names = {file.name for file in files}
    assert names == {"agency.txt", "stops.txt"}


def test_index_raw_dataset_writes_manifest_and_provenance(tmp_path: Path) -> None:
    raw_root = tmp_path / "raw_gtfs"
    raw_root.mkdir()
    (raw_root / "agency.txt").write_text("agency_id,agency_name\n1,MTA\n", encoding="utf-8")
    (raw_root / "routes.txt").write_text("route_id,route_type\n1,1\n", encoding="utf-8")

    provenance_log = tmp_path / "manifests" / "provenance_gtfs.jsonl"
    manifest_dir = tmp_path / "manifests" / "runs"

    manifest_path = index_raw_dataset(
        dataset_id="mta_gtfs",
        source_url="https://www.mta.info/developers",
        access_method="http_download",
        raw_root=raw_root,
        provenance_log_path=provenance_log,
        manifest_output_dir=manifest_dir,
    )

    assert manifest_path.exists()

    manifest = read_ingest_manifest(manifest_path)
    assert manifest.dataset_id == "mta_gtfs"
    assert manifest.status == "completed"
    assert len(manifest.input_files) == 2

    events = read_provenance_events(provenance_log)
    assert len(events) == 2
    assert {event.dataset_id for event in events} == {"mta_gtfs"}


def test_index_raw_dataset_marks_empty_run(tmp_path: Path) -> None:
    raw_root = tmp_path / "empty_raw"
    raw_root.mkdir()

    provenance_log = tmp_path / "manifests" / "provenance_empty.jsonl"
    manifest_dir = tmp_path / "manifests" / "runs"

    manifest_path = index_raw_dataset(
        dataset_id="empty_dataset",
        source_url="https://example.invalid",
        access_method="none",
        raw_root=raw_root,
        provenance_log_path=provenance_log,
        manifest_output_dir=manifest_dir,
    )

    manifest = read_ingest_manifest(manifest_path)
    assert manifest.status == "completed_no_files"
    assert manifest.input_files == []
    assert read_provenance_events(provenance_log) == []
