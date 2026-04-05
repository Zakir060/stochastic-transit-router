# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : tests\unit\ingest\test_manifest.py
# Module          : unit.ingest.test_manifest
# Domain          : Testing
# Layer           : Testing
# Responsibility  : Unit and integration tests for manifest module
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: CI/CD pipeline
# Owner           : QA Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Unit tests for ingest manifest models and I/O."""

from __future__ import annotations

from pathlib import Path

from src.ingest.manifest import (
    ArtifactRecord,
    build_ingest_manifest,
    read_ingest_manifest,
    write_ingest_manifest,
)


def test_build_manifest_with_artifacts() -> None:
    artifact = ArtifactRecord(
        artifact_path="data/processed/graph/nyc_graph.arrow",
        artifact_sha256="f" * 64,
        artifact_size_bytes=1024,
    )

    manifest = build_ingest_manifest(
        dataset_id="mta_gtfs",
        source_url="https://www.mta.info/developers",
        input_files=["data/raw/gtfs/agency.txt"],
        artifacts=[artifact],
        ingest_run_id="run-001",
    )

    assert manifest.ingest_run_id == "run-001"
    assert manifest.artifacts[0].artifact_size_bytes == 1024


def test_manifest_roundtrip_on_disk(tmp_path: Path) -> None:
    manifest = build_ingest_manifest(
        dataset_id="nyc_tlc",
        source_url="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
        input_files=["data/raw/tlc/yellow_tripdata_2026-01.parquet"],
        errors=["none"],
        ingest_run_id="run-002",
    )

    manifest_path = tmp_path / "manifest.json"
    write_ingest_manifest(manifest_path, manifest)
    loaded = read_ingest_manifest(manifest_path)

    assert loaded.ingest_run_id == "run-002"
    assert loaded.dataset_id == "nyc_tlc"
    assert loaded.input_files == manifest.input_files
    assert loaded.errors == ["none"]
