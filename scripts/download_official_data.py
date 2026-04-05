# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : scripts/download_official_data.py
# Module          : download_official_data
# Domain          : Data Processing
# Layer           : Automation
# Responsibility  : Download official transit and geographic datasets
# Public Surface  : Script entry point
# Primary Inputs  : Data source URLs
# Primary Outputs : Downloaded dataset files
# Primary Consumers: Data pipeline, manual execution
# Owner           : Data Engineering Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Download official NYC transit datasets into data/raw and write ingest manifests.

This script intentionally downloads only real source data from official URLs.
No synthetic or mock content is generated.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.ingest.errors import DataSourceUnavailableError
from src.ingest.pipeline import index_raw_dataset

USER_AGENT = "stochastic-transit-router/0.1 (+https://github.com/Zakir060/stochastic-transit-router)"
MTA_DEVELOPERS_URL = "https://www.mta.info/developers"
TLC_LISTING_URL = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
OVERPASS_ENDPOINT = "https://overpass-api.de/api/interpreter"

# South, west, north, east for NYC approximate admin bounds.
NYC_BBOX = (40.477399, -74.25909, 40.917577, -73.700272)


def _request_headers(extra: dict[str, str] | None = None) -> dict[str, str]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
    }
    if extra:
        headers.update(extra)
    return headers


def _fetch_text(url: str, timeout_seconds: int = 120) -> str:
    req = Request(url, headers=_request_headers({"Accept": "text/html,application/xhtml+xml"}))
    with urlopen(req, timeout=timeout_seconds) as response:
        return response.read().decode("utf-8", "ignore")


def _stream_download(url: str, output_path: Path, timeout_seconds: int = 180, headers: dict[str, str] | None = None) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    req = Request(url, headers=_request_headers(headers))
    with urlopen(req, timeout=timeout_seconds) as response:
        with output_path.open("wb") as handle:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                handle.write(chunk)


def _post_bytes(url: str, body: bytes, timeout_seconds: int = 180) -> bytes:
    req = Request(
        url,
        data=body,
        method="POST",
        headers=_request_headers({"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"}),
    )
    with urlopen(req, timeout=timeout_seconds) as response:
        return response.read()


def _safe_name_from_url(url: str) -> str:
    return Path(urlparse(url).path).name


def _safe_local_name_from_url(url: str, default_name: str) -> str:
    raw_name = _safe_name_from_url(url)
    decoded = unquote(raw_name) if raw_name else default_name
    sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", decoded).strip("._")
    return sanitized or default_name


def _sanitize_local_token(token: str, default_name: str) -> str:
    decoded = unquote(token)
    sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", decoded).strip("._")
    return sanitized or default_name


def _normalized_realtime_name(path: Path) -> str:
    suffix = path.suffix.lower()
    stem = path.stem
    stem_parts = stem.rsplit("_", 1)

    if len(stem_parts) == 2 and re.fullmatch(r"\d{8}T\d{6}Z", stem_parts[1]):
        base, timestamp = stem_parts
        normalized_base = _sanitize_local_token(base, default_name="feed")
        return f"{normalized_base}_{timestamp}{suffix}"

    normalized_stem = _sanitize_local_token(stem, default_name="feed")
    return f"{normalized_stem}{suffix}"


def normalize_existing_realtime_files(raw_dir: Path) -> dict[str, str]:
    """Normalize previously downloaded realtime filenames to stable local naming."""

    normalized: dict[str, str] = {}
    if not raw_dir.exists():
        return normalized

    for path in sorted(raw_dir.iterdir()):
        if not path.is_file():
            continue

        target_name = _normalized_realtime_name(path)
        if target_name == path.name:
            continue

        target_path = path.with_name(target_name)
        if target_path.exists():
            path.unlink()
            normalized[path.name] = target_path.name
            continue

        path.rename(target_path)
        normalized[path.name] = target_path.name

    return normalized


def _dedupe_sorted(values: Iterable[str]) -> list[str]:
    return sorted(set(values))


def discover_mta_gtfs_urls() -> list[str]:
    html = _fetch_text(MTA_DEVELOPERS_URL)
    urls = re.findall(r"https://rrgtfsfeeds\.s3\.amazonaws\.com/[A-Za-z0-9_.-]+\.zip", html)
    discovered = _dedupe_sorted(urls)
    if not discovered:
        raise DataSourceUnavailableError("No official MTA GTFS zip URLs were discovered on the developers page")
    return discovered


def discover_tlc_parquet_urls() -> list[str]:
    html = _fetch_text(TLC_LISTING_URL)
    urls = re.findall(r"https://d37ci6vzurychx\.cloudfront\.net/trip-data/[A-Za-z0-9_.-]+\.parquet", html)
    discovered = _dedupe_sorted(urls)
    if not discovered:
        raise DataSourceUnavailableError("No official TLC parquet URLs were discovered on the listing page")
    return discovered


def select_latest_tlc_per_feed(urls: list[str]) -> list[str]:
    pattern = re.compile(r"^(?P<prefix>[a-z0-9_]+)_tripdata_(?P<year>\d{4})-(?P<month>\d{2})\.parquet$")
    latest: dict[str, tuple[int, int, str]] = {}
    for url in urls:
        filename = _safe_name_from_url(url)
        match = pattern.match(filename)
        if not match:
            continue
        prefix = match.group("prefix")
        year = int(match.group("year"))
        month = int(match.group("month"))
        current = latest.get(prefix)
        if current is None or (year, month) > (current[0], current[1]):
            latest[prefix] = (year, month, url)

    selected = [value[2] for value in latest.values()]
    if not selected:
        raise DataSourceUnavailableError("TLC listing did not contain parseable tripdata parquet filenames")
    return _dedupe_sorted(selected)


def _extract_realtime_urls_from_config(config_path: Path) -> list[str]:
    if not config_path.exists():
        return []

    lines = config_path.read_text(encoding="utf-8").splitlines()
    in_block = False
    urls: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("realtime_urls:"):
            in_block = True
            continue

        if in_block:
            if stripped and not stripped.startswith("-") and not line.startswith(" " * 4):
                break
            if stripped.startswith("-"):
                candidate = stripped[1:].strip()
                if candidate.startswith("http://") or candidate.startswith("https://"):
                    urls.append(candidate)

    return urls


def resolve_gtfs_realtime_urls() -> list[str]:
    env_value = os.getenv("MTA_GTFS_RT_URLS", "").strip()
    if env_value:
        env_urls = [entry.strip() for entry in env_value.split(",") if entry.strip()]
        return _dedupe_sorted(env_urls)

    config_urls = _extract_realtime_urls_from_config(PROJECT_ROOT / "configs" / "feeds" / "mta_realtime.yaml")
    return _dedupe_sorted(config_urls)


def download_mta_gtfs(raw_dir: Path, overwrite: bool) -> list[Path]:
    downloaded: list[Path] = []
    for url in discover_mta_gtfs_urls():
        filename = _safe_name_from_url(url)
        output_path = raw_dir / filename
        if output_path.exists() and output_path.stat().st_size > 0 and not overwrite:
            downloaded.append(output_path)
            continue
        _stream_download(url, output_path)
        downloaded.append(output_path)
    return downloaded


def download_tlc(raw_dir: Path, all_months: bool, overwrite: bool, max_files: int | None = None) -> list[Path]:
    discovered = discover_tlc_parquet_urls()
    selected = discovered if all_months else select_latest_tlc_per_feed(discovered)
    if max_files is not None:
        selected = selected[:max_files]

    downloaded: list[Path] = []
    for url in selected:
        filename = _safe_name_from_url(url)
        output_path = raw_dir / filename
        if output_path.exists() and output_path.stat().st_size > 0 and not overwrite:
            downloaded.append(output_path)
            continue
        _stream_download(url, output_path)
        downloaded.append(output_path)
    return downloaded


def build_overpass_query() -> str:
    south, west, north, east = NYC_BBOX
    return (
        "[out:json][timeout:120];"
        "("
        f"way['highway'~'footway|pedestrian|path|steps|crossing']({south},{west},{north},{east});"
        ");"
        "(._;>;);"
        "out body;"
    )


def download_osm_overpass(raw_dir: Path, overwrite: bool) -> list[Path]:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_path = raw_dir / f"osm_overpass_nyc_{timestamp}.json"
    latest_marker = raw_dir / "osm_overpass_nyc_latest.json"

    if latest_marker.exists() and latest_marker.stat().st_size > 0 and not overwrite:
        return [latest_marker]

    payload = _post_bytes(OVERPASS_ENDPOINT, build_overpass_query().encode("utf-8"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(payload)
    latest_marker.write_bytes(payload)
    return [output_path, latest_marker]


def download_gtfs_realtime(raw_dir: Path, overwrite: bool) -> list[Path]:
    api_key = os.getenv("MTA_API_KEY", "").strip()
    urls = resolve_gtfs_realtime_urls()

    if not urls:
        raise DataSourceUnavailableError(
            "No GTFS realtime URLs configured. Set MTA_GTFS_RT_URLS or populate configs/feeds/mta_realtime.yaml"
        )

    request_headers = {"x-api-key": api_key} if api_key else None

    downloaded: list[Path] = []
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    for index, url in enumerate(urls, start=1):
        default_name = f"feed_{index}.pb"
        base = _safe_local_name_from_url(url, default_name=default_name)
        suffix = Path(base).suffix.lower()
        if suffix not in {".pb", ".json", ".xml"}:
            base = f"{Path(base).stem}.pb"
        output_path = raw_dir / f"{Path(base).stem}_{timestamp}.pb"
        if Path(base).suffix.lower() in {".json", ".xml"}:
            output_path = raw_dir / f"{Path(base).stem}_{timestamp}{Path(base).suffix.lower()}"
        if output_path.exists() and output_path.stat().st_size > 0 and not overwrite:
            downloaded.append(output_path)
            continue
        _stream_download(url, output_path, headers=request_headers)
        downloaded.append(output_path)

    return downloaded


def _index(dataset_id: str, source_url: str, access_method: str, raw_root: Path) -> Path:
    return index_raw_dataset(
        dataset_id=dataset_id,
        source_url=source_url,
        access_method=access_method,
        raw_root=raw_root,
        provenance_log_path=PROJECT_ROOT / "data" / "manifests" / f"provenance_{dataset_id}.jsonl",
        manifest_output_dir=PROJECT_ROOT / "data" / "manifests" / "runs",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Download official NYC transit data sources into data/raw")
    parser.add_argument(
        "--tlc-all-months",
        action="store_true",
        help="Download every discovered TLC parquet file (very large). Default downloads latest file per feed type.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Redownload files even when they already exist locally.",
    )
    parser.add_argument(
        "--tlc-max-files",
        type=int,
        default=0,
        help="Limit number of TLC parquet files to download after selection (0 means no limit).",
    )
    args = parser.parse_args()

    raw_gtfs = PROJECT_ROOT / "data" / "raw" / "gtfs"
    raw_gtfs_realtime = PROJECT_ROOT / "data" / "raw" / "gtfs_realtime"
    raw_tlc = PROJECT_ROOT / "data" / "raw" / "tlc"
    raw_osm = PROJECT_ROOT / "data" / "raw" / "osm"

    for directory in (raw_gtfs, raw_gtfs_realtime, raw_tlc, raw_osm):
        directory.mkdir(parents=True, exist_ok=True)

    normalized_realtime = normalize_existing_realtime_files(raw_gtfs_realtime)
    tlc_max_files = args.tlc_max_files if args.tlc_max_files > 0 else None
    tlc_scope = "all_months" if args.tlc_all_months else "latest_per_feed_type"

    datasets_summary: dict[str, dict[str, object]] = {}
    summary: dict[str, object] = {
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "datasets": datasets_summary,
        "tlc_scope": tlc_scope,
        "tlc_max_files": tlc_max_files,
        "normalized_realtime_filenames": normalized_realtime,
    }

    def record_success(dataset_id: str, files: list[Path], manifest_path: Path) -> None:
        datasets_summary[dataset_id] = {
            "status": "completed",
            "downloaded_files": [path.resolve().as_posix() for path in files],
            "manifest_path": manifest_path.resolve().as_posix(),
        }

    def record_unavailable(dataset_id: str, reason: str, manifest_path: Path) -> None:
        datasets_summary[dataset_id] = {
            "status": "unavailable",
            "reason": reason,
            "manifest_path": manifest_path.resolve().as_posix(),
        }

    try:
        gtfs_files = download_mta_gtfs(raw_gtfs, overwrite=args.overwrite)
        manifest = _index("mta_gtfs", MTA_DEVELOPERS_URL, "http_download", raw_gtfs)
        record_success("mta_gtfs", gtfs_files, manifest)
        print(f"mta_gtfs downloaded={len(gtfs_files)} manifest={manifest.as_posix()}")
    except (HTTPError, URLError, DataSourceUnavailableError) as exc:
        manifest = _index("mta_gtfs", MTA_DEVELOPERS_URL, "http_download", raw_gtfs)
        record_unavailable("mta_gtfs", str(exc), manifest)
        print(f"mta_gtfs unavailable reason={exc}")

    try:
        tlc_files = download_tlc(
            raw_tlc,
            all_months=args.tlc_all_months,
            overwrite=args.overwrite,
            max_files=tlc_max_files,
        )
        manifest = _index("nyc_tlc", TLC_LISTING_URL, "html_listing_then_parquet_download", raw_tlc)
        record_success("nyc_tlc", tlc_files, manifest)
        print(f"nyc_tlc downloaded={len(tlc_files)} manifest={manifest.as_posix()}")
    except (HTTPError, URLError, DataSourceUnavailableError) as exc:
        manifest = _index("nyc_tlc", TLC_LISTING_URL, "html_listing_then_parquet_download", raw_tlc)
        record_unavailable("nyc_tlc", str(exc), manifest)
        print(f"nyc_tlc unavailable reason={exc}")

    try:
        osm_files = download_osm_overpass(raw_osm, overwrite=args.overwrite)
        manifest = _index("osm_overpass", OVERPASS_ENDPOINT, "http_post", raw_osm)
        record_success("osm_overpass", osm_files, manifest)
        print(f"osm_overpass downloaded={len(osm_files)} manifest={manifest.as_posix()}")
    except (HTTPError, URLError, DataSourceUnavailableError) as exc:
        manifest = _index("osm_overpass", OVERPASS_ENDPOINT, "http_post", raw_osm)
        record_unavailable("osm_overpass", str(exc), manifest)
        print(f"osm_overpass unavailable reason={exc}")

    try:
        rt_files = download_gtfs_realtime(raw_gtfs_realtime, overwrite=args.overwrite)
        manifest = _index("mta_gtfs_realtime", "https://api.mta.info/", "http_polling", raw_gtfs_realtime)
        record_success("mta_gtfs_realtime", rt_files, manifest)
        print(f"mta_gtfs_realtime downloaded={len(rt_files)} manifest={manifest.as_posix()}")
    except (HTTPError, URLError, DataSourceUnavailableError) as exc:
        manifest = _index("mta_gtfs_realtime", "https://api.mta.info/", "http_polling", raw_gtfs_realtime)
        record_unavailable("mta_gtfs_realtime", str(exc), manifest)
        print(f"mta_gtfs_realtime unavailable reason={exc}")

    summary["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
    output_path = PROJECT_ROOT / "data" / "manifests" / "download_summary_latest.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"download_summary={output_path.as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
