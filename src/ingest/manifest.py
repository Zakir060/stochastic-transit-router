# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\ingest\manifest.py
# Module          : ingest.manifest
# Domain          : Data Ingestion
# Layer           : Data Processing
# Responsibility  : Implementation of manifest
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Data pipeline, scripts
# Owner           : Data Engineering Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Ingest manifest models and serialization helpers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from uuid import uuid4


@dataclass(slots=True, frozen=True)
class ArtifactRecord:
    """A produced artifact tied to an ingest run."""

    artifact_path: str
    artifact_sha256: str
    artifact_size_bytes: int

    def to_dict(self) -> dict[str, object]:
        """Return JSON-serializable artifact representation."""

        return {
            "artifact_path": self.artifact_path,
            "artifact_sha256": self.artifact_sha256,
            "artifact_size_bytes": self.artifact_size_bytes,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, object]) -> "ArtifactRecord":
        """Build artifact from dictionary payload."""

        return cls(
            artifact_path=str(payload["artifact_path"]),
            artifact_sha256=str(payload["artifact_sha256"]),
            artifact_size_bytes=int(payload["artifact_size_bytes"]),
        )


@dataclass(slots=True, frozen=True)
class IngestManifest:
    """Manifest describing one data ingest run."""

    ingest_run_id: str
    dataset_id: str
    source_url: str
    started_at_utc: str
    completed_at_utc: str
    input_files: list[str]
    artifacts: list[ArtifactRecord]
    status: str
    errors: list[str]

    def to_dict(self) -> dict[str, object]:
        """Return JSON-serializable ingest manifest."""

        return {
            "ingest_run_id": self.ingest_run_id,
            "dataset_id": self.dataset_id,
            "source_url": self.source_url,
            "started_at_utc": self.started_at_utc,
            "completed_at_utc": self.completed_at_utc,
            "input_files": self.input_files,
            "artifacts": [artifact.to_dict() for artifact in self.artifacts],
            "status": self.status,
            "errors": self.errors,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, object]) -> "IngestManifest":
        """Build ingest manifest from dictionary payload."""

        artifacts_payload = payload.get("artifacts", [])
        artifacts = [ArtifactRecord.from_dict(item) for item in artifacts_payload if isinstance(item, dict)]
        errors_payload = payload.get("errors", [])
        errors = [str(item) for item in errors_payload] if isinstance(errors_payload, list) else []
        input_payload = payload.get("input_files", [])
        input_files = [str(item) for item in input_payload] if isinstance(input_payload, list) else []

        return cls(
            ingest_run_id=str(payload["ingest_run_id"]),
            dataset_id=str(payload["dataset_id"]),
            source_url=str(payload["source_url"]),
            started_at_utc=str(payload["started_at_utc"]),
            completed_at_utc=str(payload["completed_at_utc"]),
            input_files=input_files,
            artifacts=artifacts,
            status=str(payload["status"]),
            errors=errors,
        )


def build_ingest_manifest(
    dataset_id: str,
    source_url: str,
    input_files: list[str],
    artifacts: list[ArtifactRecord] | None = None,
    errors: list[str] | None = None,
    status: str = "completed",
    started_at: datetime | None = None,
    completed_at: datetime | None = None,
    ingest_run_id: str | None = None,
) -> IngestManifest:
    """Construct a normalized ingest manifest object."""

    started_value = (started_at or datetime.now(timezone.utc)).astimezone(timezone.utc).isoformat()
    completed_value = (completed_at or datetime.now(timezone.utc)).astimezone(timezone.utc).isoformat()

    return IngestManifest(
        ingest_run_id=ingest_run_id or uuid4().hex,
        dataset_id=dataset_id,
        source_url=source_url,
        started_at_utc=started_value,
        completed_at_utc=completed_value,
        input_files=input_files,
        artifacts=artifacts or [],
        status=status,
        errors=errors or [],
    )


def write_ingest_manifest(manifest_path: Path, manifest: IngestManifest) -> None:
    """Write ingest manifest JSON file with stable formatting."""

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(manifest.to_dict(), handle, indent=2, sort_keys=True)
        handle.write("\n")


def read_ingest_manifest(manifest_path: Path) -> IngestManifest:
    """Read ingest manifest from disk."""

    with manifest_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("Ingest manifest content must be a JSON object")
    return IngestManifest.from_dict(payload)


def module_healthcheck() -> bool:
    """Return True when manifest construction is deterministic."""

    manifest = build_ingest_manifest(
        dataset_id="healthcheck",
        source_url="https://example.invalid",
        input_files=[],
        ingest_run_id="run",
    )
    return manifest.dataset_id == "healthcheck" and manifest.ingest_run_id == "run"
