# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : scripts/build_graph_nyc.py
# Module          : build_graph_nyc
# Domain          : Data Processing
# Layer           : Automation
# Responsibility  : Construct transit graph from NYC datasets
# Public Surface  : Script entry point
# Primary Inputs  : GTFS and OSM data
# Primary Outputs : Serialized graph structures
# Primary Consumers: Manual execution, experimentation
# Owner           : Data Engineering Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Build lightweight graph seed artifacts from ingested official raw data."""

from __future__ import annotations

from collections import Counter
import csv
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import zipfile


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_GTFS_DIR = PROJECT_ROOT / "data" / "raw" / "gtfs"
RAW_OSM_LATEST = PROJECT_ROOT / "data" / "raw" / "osm" / "osm_overpass_nyc_latest.json"
OUT_GRAPH_DIR = PROJECT_ROOT / "data" / "processed" / "graph"

REQUIRED_GTFS_FILES = {"agency.txt", "stops.txt", "routes.txt", "trips.txt", "stop_times.txt"}
COUNTED_GTFS_TABLES = ["stops.txt", "routes.txt", "trips.txt", "stop_times.txt"]


def _count_rows_in_zip_csv(archive: zipfile.ZipFile, member_name: str) -> int:
    with archive.open(member_name) as binary_handle:
        text_handle = io.TextIOWrapper(binary_handle, encoding="utf-8", newline="")
        reader = csv.reader(text_handle)
        next(reader, None)
        return sum(1 for _ in reader)


def _build_gtfs_summary() -> tuple[list[dict[str, object]], dict[str, int]]:
    summaries: list[dict[str, object]] = []
    aggregate = Counter()

    for archive_path in sorted(RAW_GTFS_DIR.glob("*.zip")):
        with zipfile.ZipFile(archive_path, "r") as archive:
            member_names = set(archive.namelist())
            table_counts: dict[str, int] = {}
            for table_name in COUNTED_GTFS_TABLES:
                if table_name in member_names:
                    table_key = table_name.replace(".txt", "")
                    row_count = _count_rows_in_zip_csv(archive, table_name)
                    table_counts[table_key] = row_count
                    aggregate[table_key] += row_count

            summaries.append(
                {
                    "archive_name": archive_path.name,
                    "archive_size_bytes": archive_path.stat().st_size,
                    "member_count": len(member_names),
                    "contains_required_files": REQUIRED_GTFS_FILES.issubset(member_names),
                    "table_row_counts": table_counts,
                }
            )

    return summaries, dict(aggregate)


def _build_osm_summary() -> dict[str, object]:
    if not RAW_OSM_LATEST.exists():
        return {
            "available": False,
            "source_file": RAW_OSM_LATEST.as_posix(),
            "element_counts": {},
        }

    payload = json.loads(RAW_OSM_LATEST.read_text(encoding="utf-8"))
    elements = payload.get("elements", []) if isinstance(payload, dict) else []
    type_counter = Counter()

    for element in elements:
        if isinstance(element, dict):
            type_counter[str(element.get("type", "unknown"))] += 1

    return {
        "available": True,
        "source_file": RAW_OSM_LATEST.as_posix(),
        "source_size_bytes": RAW_OSM_LATEST.stat().st_size,
        "element_counts": dict(type_counter),
        "total_elements": sum(type_counter.values()),
    }


def _write_gtfs_inventory_csv(summaries: list[dict[str, object]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "archive_name",
                "archive_size_bytes",
                "member_count",
                "contains_required_files",
                "stops",
                "routes",
                "trips",
                "stop_times",
            ]
        )
        for summary in summaries:
            table_counts = summary.get("table_row_counts", {})
            writer.writerow(
                [
                    summary.get("archive_name", ""),
                    summary.get("archive_size_bytes", 0),
                    summary.get("member_count", 0),
                    summary.get("contains_required_files", False),
                    table_counts.get("stops", 0),
                    table_counts.get("routes", 0),
                    table_counts.get("trips", 0),
                    table_counts.get("stop_times", 0),
                ]
            )


def main() -> int:
    """Build graph-ready seed summaries from current raw data snapshots."""

    OUT_GRAPH_DIR.mkdir(parents=True, exist_ok=True)

    gtfs_summaries, gtfs_aggregate = _build_gtfs_summary()
    osm_summary = _build_osm_summary()

    graph_seed_manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "raw_inputs": {
            "gtfs_archive_count": len(gtfs_summaries),
            "osm_available": bool(osm_summary.get("available", False)),
        },
        "gtfs": {
            "archives": gtfs_summaries,
            "aggregate_table_row_counts": gtfs_aggregate,
        },
        "osm": osm_summary,
    }

    manifest_path = OUT_GRAPH_DIR / "graph_seed_manifest.json"
    manifest_path.write_text(json.dumps(graph_seed_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    inventory_csv_path = OUT_GRAPH_DIR / "gtfs_inventory.csv"
    _write_gtfs_inventory_csv(gtfs_summaries, inventory_csv_path)

    return 0 if gtfs_summaries else 1


if __name__ == "__main__":
    raise SystemExit(main())
