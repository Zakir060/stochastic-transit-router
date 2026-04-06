import json
from pathlib import Path

from src.ingest.pipeline import discover_raw_files, index_raw_dataset
from src.ingest.provenance import read_provenance_events


def test_discover_raw_files_filters_suffixes(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("alpha", encoding="utf-8")
    (tmp_path / "b.bin").write_bytes(b"beta")
    discovered = discover_raw_files(tmp_path, {".txt"})
    assert [item.name for item in discovered] == ["a.txt"]


def test_index_raw_dataset_writes_manifest_and_provenance(tmp_path: Path) -> None:
    raw_root = tmp_path / "raw"
    raw_root.mkdir()
    (raw_root / "sample.txt").write_text("hello", encoding="utf-8")

    provenance_log = tmp_path / "provenance.jsonl"
    manifest_dir = tmp_path / "manifests"

    manifest_path = index_raw_dataset(
        dataset_id="demo_dataset",
        source_url="https://example.invalid/demo",
        access_method="manual",
        raw_root=raw_root,
        provenance_log_path=provenance_log,
        manifest_output_dir=manifest_dir,
        allowed_suffixes={".txt"},
    )

    assert manifest_path.exists()
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert payload["dataset_id"] == "demo_dataset"
    assert payload["status"] == "completed"
    assert len(payload["input_files"]) == 1

    events = read_provenance_events(provenance_log)
    assert len(events) == 1
    assert events[0].status == "indexed"
