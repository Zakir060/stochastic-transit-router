# Ingest Reference: GTFS

| Field | Value |
|---|---|
| Owner | Data Engineering |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

This page documents how static GTFS schedule data is acquired, stored, indexed, and validated.

## Acquisition

Static GTFS is downloaded from the official MTA developers listing and written under `data/raw/gtfs/`.

Recommended command:

```powershell
python scripts/download_official_data.py
```

## Storage layout

- Raw directory: `data/raw/gtfs/`
- File format: `.zip` archives as published by the source
- Policy: files are treated as immutable inputs and should not be edited in place

## Indexing and manifests

After download, the ingest pipeline indexes the raw directory and writes provenance events plus a run manifest.

- Provenance log: `data/manifests/provenance_mta_gtfs.jsonl`
- Run manifests: `data/manifests/runs/mta_gtfs_<ingest_run_id>.json`

The indexing entry point is:

- [src/ingest/pipeline.py](/src/ingest/pipeline.py): `index_raw_dataset()`

## Validation

GTFS CSV content validation is defined by schemas under `schemas/gtfs/`.

For a human-readable overview of required and optional GTFS tables, see:

- [GTFS Dataset](/docs/datasets/gtfs.md)

## Related

- [Data Manifests](/data/manifests/README.md)
- [Reproducibility](/docs/operations/reproducibility.md)
- [GTFS Dataset](/docs/datasets/gtfs.md)
- [Download Script](/scripts/download_official_data.py)

---

Document Control

- Owner: Data Engineering Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
