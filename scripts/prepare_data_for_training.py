# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : scripts/prepare_data_for_training.py
# Module          : prepare_data_for_training
# Domain          : Data Processing
# Layer           : Automation
# Responsibility  : Prepare data for machine learning workflows
# Public Surface  : Script entry point
# Primary Inputs  : Raw data files
# Primary Outputs : Prepared dataset folders
# Primary Consumers: Manual execution, ML pipelines
# Owner           : Data Engineering Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Prepare data folder layout for train/validation/test workflows.

This script does not synthesize data. It organizes references to already-downloaded
official raw artifacts and emits split manifests plus inventory reports.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_GTFS_DIR = PROJECT_ROOT / "data" / "raw" / "gtfs"
RAW_GTFS_RT_DIR = PROJECT_ROOT / "data" / "raw" / "gtfs_realtime"
RAW_TLC_DIR = PROJECT_ROOT / "data" / "raw" / "tlc"
RAW_OSM_DIR = PROJECT_ROOT / "data" / "raw" / "osm"

TRAINING_ROOT = PROJECT_ROOT / "data" / "processed" / "training"
CACHE_INDEX_ROOT = PROJECT_ROOT / "data" / "cache" / "indexes"
EXPORT_REPORT_ROOT = PROJECT_ROOT / "data" / "exports" / "reports"
EVALUATION_ROOT = PROJECT_ROOT / "data" / "processed" / "evaluation"

SPLITS = ("train", "validation", "test")
REALTIME_TS_PATTERN = re.compile(r"^(?P<feed>.+)_(?P<timestamp>\d{8}T\d{6}Z)\.(?P<ext>pb|json|xml)$")
TLC_PERIOD_PATTERN = re.compile(r"^[a-z0-9_]+_tripdata_(?P<period>\d{4}-\d{2})\.parquet$")


@dataclass(frozen=True)
class RawFileRecord:
    dataset_id: str
    path: Path
    file_size_bytes: int
    modified_at_utc: str
    key: str


@dataclass(frozen=True)
class SplitBundle:
    train_keys: list[str]
    validation_keys: list[str]
    test_keys: list[str]


def _iso_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat()


def _list_files(root: Path, suffixes: set[str] | None = None) -> list[Path]:
    if not root.exists():
        return []

    files = [path for path in root.iterdir() if path.is_file()]
    if suffixes is not None:
        normalized = {value.lower() for value in suffixes}
        files = [path for path in files if path.suffix.lower() in normalized]
    return sorted(files)


def _split_keys(keys: list[str]) -> SplitBundle:
    n_items = len(keys)
    if n_items == 0:
        return SplitBundle([], [], [])
    if n_items == 1:
        return SplitBundle(keys[:], [], [])
    if n_items == 2:
        return SplitBundle(keys[:1], [], keys[1:])
    if n_items == 3:
        return SplitBundle(keys[:1], keys[1:2], keys[2:])

    train_count = max(1, int(n_items * 0.7))
    validation_count = max(1, int(n_items * 0.15))
    test_count = n_items - train_count - validation_count

    if test_count < 1:
        test_count = 1
        if train_count > validation_count and train_count > 1:
            train_count -= 1
        elif validation_count > 1:
            validation_count -= 1
        elif train_count > 1:
            train_count -= 1

    while train_count + validation_count + test_count < n_items:
        train_count += 1

    while train_count + validation_count + test_count > n_items:
        if train_count > 1:
            train_count -= 1
        elif validation_count > 1:
            validation_count -= 1
        else:
            test_count -= 1

    train_keys = keys[:train_count]
    validation_keys = keys[train_count : train_count + validation_count]
    test_keys = keys[train_count + validation_count : train_count + validation_count + test_count]
    return SplitBundle(train_keys, validation_keys, test_keys)


def _collect_gtfs_records() -> list[RawFileRecord]:
    records: list[RawFileRecord] = []
    for path in _list_files(RAW_GTFS_DIR, suffixes={".zip"}):
        records.append(
            RawFileRecord(
                dataset_id="mta_gtfs",
                path=path,
                file_size_bytes=path.stat().st_size,
                modified_at_utc=_iso_mtime(path),
                key=path.name,
            )
        )
    return records


def _collect_tlc_records() -> list[RawFileRecord]:
    records: list[RawFileRecord] = []
    for path in _list_files(RAW_TLC_DIR, suffixes={".parquet"}):
        match = TLC_PERIOD_PATTERN.match(path.name)
        period_key = match.group("period") if match else path.name
        records.append(
            RawFileRecord(
                dataset_id="nyc_tlc",
                path=path,
                file_size_bytes=path.stat().st_size,
                modified_at_utc=_iso_mtime(path),
                key=period_key,
            )
        )
    return records


def _collect_osm_records() -> list[RawFileRecord]:
    records: list[RawFileRecord] = []
    for path in _list_files(RAW_OSM_DIR, suffixes={".json"}):
        records.append(
            RawFileRecord(
                dataset_id="osm_overpass",
                path=path,
                file_size_bytes=path.stat().st_size,
                modified_at_utc=_iso_mtime(path),
                key=path.name,
            )
        )
    return records


def _collect_realtime_records() -> tuple[list[RawFileRecord], dict[str, str]]:
    records: list[RawFileRecord] = []
    latest_by_feed: dict[str, tuple[str, Path]] = {}

    for path in _list_files(RAW_GTFS_RT_DIR, suffixes={".pb", ".json", ".xml"}):
        match = REALTIME_TS_PATTERN.match(path.name)
        if match:
            feed_key = match.group("feed")
            timestamp = match.group("timestamp")
            key = timestamp
            latest_entry = latest_by_feed.get(feed_key)
            if latest_entry is None or timestamp > latest_entry[0]:
                latest_by_feed[feed_key] = (timestamp, path)
        else:
            feed_key = path.stem
            key = "no_timestamp"

        records.append(
            RawFileRecord(
                dataset_id="mta_gtfs_realtime",
                path=path,
                file_size_bytes=path.stat().st_size,
                modified_at_utc=_iso_mtime(path),
                key=key,
            )
        )

    latest_output = {feed_key: entry[1].resolve().as_posix() for feed_key, entry in sorted(latest_by_feed.items())}
    return records, latest_output


def _paths_for_keys(records: Iterable[RawFileRecord], selected_keys: set[str]) -> list[str]:
    paths = [record.path.resolve().as_posix() for record in records if record.key in selected_keys]
    return sorted(paths)


def _write_split_manifest(split_name: str, payload: dict[str, object]) -> None:
    split_dir = TRAINING_ROOT / split_name
    split_dir.mkdir(parents=True, exist_ok=True)
    output_path = split_dir / "dataset_manifest.json"
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _rebalance_sparse_splits(split_paths: dict[str, list[str]]) -> dict[str, list[str]]:
    """Rebalance paths so validation and test are non-empty when feasible."""

    train_paths = list(split_paths.get("train", []))
    validation_paths = list(split_paths.get("validation", []))
    test_paths = list(split_paths.get("test", []))

    if not validation_paths:
        if len(test_paths) >= 2:
            move_count = max(1, len(test_paths) // 3)
            validation_paths = test_paths[:move_count]
            test_paths = test_paths[move_count:]
        elif len(train_paths) >= 2:
            move_count = 1
            validation_paths = train_paths[-move_count:]
            train_paths = train_paths[:-move_count]

    if not test_paths:
        if len(validation_paths) >= 2:
            test_paths = [validation_paths[-1]]
            validation_paths = validation_paths[:-1]
        elif len(train_paths) >= 2:
            test_paths = [train_paths[-1]]
            train_paths = train_paths[:-1]

    return {
        "train": sorted(train_paths),
        "validation": sorted(validation_paths),
        "test": sorted(test_paths),
    }


def _write_inventory_csv(all_records: list[RawFileRecord], split_lookup: dict[str, str]) -> None:
    CACHE_INDEX_ROOT.mkdir(parents=True, exist_ok=True)
    output_path = CACHE_INDEX_ROOT / "raw_inventory.csv"
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "dataset_id",
                "file_name",
                "absolute_path",
                "size_bytes",
                "modified_at_utc",
                "split",
                "key",
            ]
        )
        for record in sorted(all_records, key=lambda value: (value.dataset_id, value.path.name)):
            split_name = split_lookup.get(record.path.resolve().as_posix(), "shared")
            writer.writerow(
                [
                    record.dataset_id,
                    record.path.name,
                    record.path.resolve().as_posix(),
                    record.file_size_bytes,
                    record.modified_at_utc,
                    split_name,
                    record.key,
                ]
            )


def _write_report(summary: dict[str, object]) -> None:
    EXPORT_REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    output_path = EXPORT_REPORT_ROOT / "data_layout_report.md"
    lines = [
        "# Data Layout Report",
        "",
        f"Generated at UTC: {summary['generated_at_utc']}",
        "",
        "## Split File Counts",
    ]

    split_counts = summary.get("split_file_counts", {})
    for split_name in SPLITS:
        count_value = split_counts.get(split_name, 0)
        lines.append(f"- {split_name}: {count_value}")

    lines.extend(
        [
            "",
            "## Dataset Coverage",
            f"- mta_gtfs files: {summary.get('mta_gtfs_file_count', 0)}",
            f"- mta_gtfs_realtime files: {summary.get('mta_gtfs_realtime_file_count', 0)}",
            f"- nyc_tlc files: {summary.get('nyc_tlc_file_count', 0)}",
            f"- osm_overpass files: {summary.get('osm_overpass_file_count', 0)}",
            "",
            "## Notes",
            "- Static GTFS and OSM snapshots are shared references across all splits.",
            "- TLC and GTFS-Realtime are split chronologically.",
            "",
        ]
    )

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    """Prepare deterministic train/validation/test manifests and inventory outputs."""

    TRAINING_ROOT.mkdir(parents=True, exist_ok=True)

    gtfs_records = _collect_gtfs_records()
    tlc_records = _collect_tlc_records()
    osm_records = _collect_osm_records()
    realtime_records, latest_realtime = _collect_realtime_records()

    tlc_keys = sorted({record.key for record in tlc_records})
    realtime_keys = sorted({record.key for record in realtime_records if record.key != "no_timestamp"})

    tlc_split = _split_keys(tlc_keys)
    realtime_split = _split_keys(realtime_keys)

    split_key_sets = {
        "train": {
            "tlc": set(tlc_split.train_keys),
            "realtime": set(realtime_split.train_keys),
        },
        "validation": {
            "tlc": set(tlc_split.validation_keys),
            "realtime": set(realtime_split.validation_keys),
        },
        "test": {
            "tlc": set(tlc_split.test_keys),
            "realtime": set(realtime_split.test_keys),
        },
    }

    latest_osm = None
    if osm_records:
        latest_osm = max(osm_records, key=lambda record: record.modified_at_utc)

    tlc_paths_by_split = {
        split_name: _paths_for_keys(tlc_records, split_key_sets[split_name]["tlc"])
        for split_name in SPLITS
    }
    tlc_paths_by_split = _rebalance_sparse_splits(tlc_paths_by_split)

    realtime_paths_by_split = {
        split_name: _paths_for_keys(realtime_records, split_key_sets[split_name]["realtime"])
        for split_name in SPLITS
    }
    # Files without timestamp are considered training-only fallback files.
    fallback_paths = [record.path.resolve().as_posix() for record in realtime_records if record.key == "no_timestamp"]
    realtime_paths_by_split["train"] = sorted(set(realtime_paths_by_split["train"] + fallback_paths))
    realtime_paths_by_split = _rebalance_sparse_splits(realtime_paths_by_split)

    split_lookup: dict[str, str] = {}
    split_counts: dict[str, int] = {name: 0 for name in SPLITS}
    static_gtfs_paths = sorted(record.path.resolve().as_posix() for record in gtfs_records)
    shared_osm_paths = [latest_osm.path.resolve().as_posix()] if latest_osm is not None else []

    for split_name in SPLITS:
        tlc_paths = tlc_paths_by_split[split_name]
        realtime_paths = realtime_paths_by_split[split_name]

        payload = {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "split": split_name,
            "datasets": {
                "mta_gtfs": {
                    "role": "shared_static_reference",
                    "files": static_gtfs_paths,
                },
                "mta_gtfs_realtime": {
                    "role": "chronological_split",
                    "files": realtime_paths,
                },
                "nyc_tlc": {
                    "role": "chronological_split",
                    "files": tlc_paths,
                },
                "osm_overpass": {
                    "role": "shared_latest_snapshot",
                    "files": shared_osm_paths,
                },
            },
        }
        _write_split_manifest(split_name, payload)

        split_file_total = len(static_gtfs_paths) + len(realtime_paths) + len(tlc_paths) + len(shared_osm_paths)
        split_counts[split_name] = split_file_total

        for path in realtime_paths:
            split_lookup[path] = split_name
        for path in tlc_paths:
            split_lookup[path] = split_name

    summary = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "split_file_counts": split_counts,
        "mta_gtfs_file_count": len(gtfs_records),
        "mta_gtfs_realtime_file_count": len(realtime_records),
        "nyc_tlc_file_count": len(tlc_records),
        "osm_overpass_file_count": len(osm_records),
        "latest_realtime_per_feed": latest_realtime,
    }

    summary_path = TRAINING_ROOT / "split_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    CACHE_INDEX_ROOT.mkdir(parents=True, exist_ok=True)
    latest_realtime_path = CACHE_INDEX_ROOT / "realtime_latest_per_feed.json"
    latest_realtime_path.write_text(json.dumps(latest_realtime, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    all_records = gtfs_records + realtime_records + tlc_records + osm_records
    _write_inventory_csv(all_records, split_lookup)
    _write_report(summary)

    EVALUATION_ROOT.mkdir(parents=True, exist_ok=True)
    evaluation_payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "split_file_counts": split_counts,
        "datasets": {
            "mta_gtfs": len(gtfs_records),
            "mta_gtfs_realtime": len(realtime_records),
            "nyc_tlc": len(tlc_records),
            "osm_overpass": len(osm_records),
        },
    }
    evaluation_path = EVALUATION_ROOT / "train_validation_test_layout.json"
    evaluation_path.write_text(json.dumps(evaluation_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    essential_counts_ok = bool(gtfs_records and realtime_records and tlc_records and osm_records)
    return 0 if essential_counts_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
