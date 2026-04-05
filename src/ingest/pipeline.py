# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\ingest\pipeline.py
# Module          : ingest.pipeline
# Domain          : Data Ingestion
# Layer           : Data Processing
# Responsibility  : Implementation of pipeline
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Data pipeline, scripts
# Owner           : Data Engineering Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Data ingest pipeline helpers for raw file indexing and manifest writing."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from src.ingest.manifest import IngestManifest, build_ingest_manifest, write_ingest_manifest
from src.ingest.provenance import append_provenance_event, build_provenance_event


def discover_raw_files(raw_root: Path, allowed_suffixes: set[str] | None = None) -> list[Path]:
    """Discover raw files recursively, skipping marker files.

    Args:
        raw_root: Root directory that contains raw data files.
        allowed_suffixes: Optional suffix whitelist such as {".txt", ".parquet"}.

    Returns:
        Sorted list of discovered files.
    """

    if not raw_root.exists():
        return []

    discovered = [
        path
        for path in raw_root.rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    ]

    if allowed_suffixes is not None:
        normalized = {suffix.lower() for suffix in allowed_suffixes}
        discovered = [path for path in discovered if path.suffix.lower() in normalized]

    return sorted(discovered)


def _to_posix_paths(paths: Iterable[Path]) -> list[str]:
    """Convert paths to stable POSIX-style strings."""

    return [path.resolve().as_posix() for path in paths]


def index_raw_dataset(
    dataset_id: str,
    source_url: str,
    access_method: str,
    raw_root: Path,
    provenance_log_path: Path,
    manifest_output_dir: Path,
    allowed_suffixes: set[str] | None = None,
) -> Path:
    """Index raw files and persist provenance plus ingest manifest records.

    Returns:
        Path to the manifest JSON file for this indexing run.
    """

    run_started = datetime.now(timezone.utc)
    files = discover_raw_files(raw_root, allowed_suffixes)

    for file_path in files:
        event = build_provenance_event(
            file_path=file_path,
            dataset_id=dataset_id,
            source_url=source_url,
            access_method=access_method,
            acquired_at=run_started,
            status="indexed",
        )
        append_provenance_event(provenance_log_path, event)

    status = "completed" if files else "completed_no_files"
    manifest: IngestManifest = build_ingest_manifest(
        dataset_id=dataset_id,
        source_url=source_url,
        input_files=_to_posix_paths(files),
        artifacts=[],
        errors=[],
        status=status,
        started_at=run_started,
        completed_at=datetime.now(timezone.utc),
    )

    manifest_output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = manifest_output_dir / f"{dataset_id}_{manifest.ingest_run_id}.json"
    write_ingest_manifest(manifest_path, manifest)
    return manifest_path


def module_healthcheck() -> bool:
    """Return True when discovery behaves deterministically on missing roots."""

    return discover_raw_files(Path("does-not-exist")) == []
