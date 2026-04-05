# Ingest Reference: GTFS Realtime

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

This page documents how GTFS-Realtime snapshots are acquired, stored, and indexed. It also describes the configuration surface for polling endpoints.

## Acquisition

GTFS-Realtime snapshots are downloaded from the official MTA endpoints configured in `configs/feeds/mta_realtime.yaml` and written under `data/raw/gtfs_realtime/`.

Recommended command:

```powershell
python scripts/download_official_data.py
```

### Authentication

If `MTA_API_KEY` is set, the downloader uses it as the `x-api-key` request header.

## Storage layout

- Raw directory: `data/raw/gtfs_realtime/`
- Snapshot filenames: `<feed>_<timestamp>.<ext>`
- Timestamp format: `YYYYMMDDThhmmssZ`
- Extensions: `.pb` (protobuf), `.json`, `.xml`

## Indexing and manifests

After download, the ingest pipeline indexes the raw directory and writes provenance events plus a run manifest.

- Provenance log: `data/manifests/provenance_mta_gtfs_realtime.jsonl`
- Run manifests: `data/manifests/runs/mta_gtfs_realtime_<ingest_run_id>.json`

The indexing entry point is:

- [src/ingest/pipeline.py](/src/ingest/pipeline.py): `index_raw_dataset()`

## Parsing and mapping

Realtime parsing and mapping utilities live under:

- [src/gtfs_realtime/](/src/gtfs_realtime/)

The dataset-level semantics are documented in:

- [GTFS Realtime Dataset](/docs/datasets/gtfs_realtime.md)

## Related

- [Feed Configuration: MTA Realtime](/configs/feeds/mta_realtime.yaml)
- [GTFS Realtime Dataset](/docs/datasets/gtfs_realtime.md)
- [Download Script](/scripts/download_official_data.py)

---

Document Control

- Owner: Data Engineering Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
