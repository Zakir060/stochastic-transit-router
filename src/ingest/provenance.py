# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\ingest\provenance.py
# Module          : ingest.provenance
# Domain          : Data Ingestion
# Layer           : Data Processing
# Responsibility  : Implementation of provenance
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Data pipeline, scripts
# Owner           : Data Engineering Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Provenance event utilities for raw data acquisition tracking."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path

from src.utils.hashing import sha256_file


@dataclass(slots=True, frozen=True)
class ProvenanceEvent:
    """A single immutable provenance entry for one acquired file."""

    dataset_id: str
    source_url: str
    access_method: str
    acquired_at_utc: str
    local_path: str
    sha256: str
    size_bytes: int
    status: str
    note: str | None = None

    def to_dict(self) -> dict[str, object]:
        """Return JSON-serializable event representation."""

        return {
            "dataset_id": self.dataset_id,
            "source_url": self.source_url,
            "access_method": self.access_method,
            "acquired_at_utc": self.acquired_at_utc,
            "local_path": self.local_path,
            "sha256": self.sha256,
            "size_bytes": self.size_bytes,
            "status": self.status,
            "note": self.note,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, object]) -> "ProvenanceEvent":
        """Build event from a dictionary payload."""

        return cls(
            dataset_id=str(payload["dataset_id"]),
            source_url=str(payload["source_url"]),
            access_method=str(payload["access_method"]),
            acquired_at_utc=str(payload["acquired_at_utc"]),
            local_path=str(payload["local_path"]),
            sha256=str(payload["sha256"]),
            size_bytes=int(payload["size_bytes"]),
            status=str(payload["status"]),
            note=str(payload["note"]) if payload.get("note") is not None else None,
        )


def build_provenance_event(
    file_path: Path,
    dataset_id: str,
    source_url: str,
    access_method: str,
    acquired_at: datetime | None = None,
    status: str = "downloaded",
    note: str | None = None,
) -> ProvenanceEvent:
    """Construct a provenance event from an on-disk file."""

    resolved = file_path.resolve()
    timestamp = (acquired_at or datetime.now(timezone.utc)).astimezone(timezone.utc).isoformat()
    return ProvenanceEvent(
        dataset_id=dataset_id,
        source_url=source_url,
        access_method=access_method,
        acquired_at_utc=timestamp,
        local_path=resolved.as_posix(),
        sha256=sha256_file(resolved),
        size_bytes=resolved.stat().st_size,
        status=status,
        note=note,
    )


def append_provenance_event(log_path: Path, event: ProvenanceEvent) -> None:
    """Append one provenance event to a JSONL log file."""

    log_path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(event.to_dict(), sort_keys=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"{line}\n")


def read_provenance_events(log_path: Path) -> list[ProvenanceEvent]:
    """Read all provenance events from a JSONL log file."""

    if not log_path.exists():
        return []

    events: list[ProvenanceEvent] = []
    with log_path.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue
            events.append(ProvenanceEvent.from_dict(json.loads(line)))
    return events


def module_healthcheck() -> bool:
    """Return True when baseline provenance serialization works."""

    event = ProvenanceEvent(
        dataset_id="healthcheck",
        source_url="https://example.invalid",
        access_method="none",
        acquired_at_utc="2026-04-05T00:00:00+00:00",
        local_path="/tmp/healthcheck",
        sha256="0" * 64,
        size_bytes=0,
        status="ok",
        note=None,
    )
    return event.to_dict()["dataset_id"] == "healthcheck"
