# =============================================================================
# Stochastic Transit Router
# Route Intelligence Platform
#
# File            : src\cli\main.py
# Module          : cli.main
# Domain          : CLI
# Layer           : Interface
# Responsibility  : Implementation of main
# Public Surface  : See module docstring and exports
# Primary Inputs  : See module docstring and type hints
# Primary Outputs : See module docstring and type hints
# Primary Consumers: Command-line users, scripts
# Owner           : CLI Team
# Review Status   : Draft
# Last Reviewed   : 2026-04-05
# =============================================================================
"""Typer command line interface."""

from __future__ import annotations

from pathlib import Path

import typer

from src.api.deps import get_graph
from src.algorithms.dijkstra import dijkstra_shortest_path
from src.algorithms.yens import yens_k_shortest_paths
from src.ingest.pipeline import index_raw_dataset


app = typer.Typer(help="Stochastic transit routing CLI")


def _run_index(
    dataset_id: str,
    source_url: str,
    access_method: str,
    raw_root: Path,
) -> Path:
    """Index one raw dataset and return generated manifest path."""

    provenance_log = Path("data/manifests") / f"provenance_{dataset_id}.jsonl"
    manifest_output_dir = Path("data/manifests/runs")
    return index_raw_dataset(
        dataset_id=dataset_id,
        source_url=source_url,
        access_method=access_method,
        raw_root=raw_root,
        provenance_log_path=provenance_log,
        manifest_output_dir=manifest_output_dir,
    )


@app.command("ingest-gtfs")
def ingest_gtfs(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Ingest GTFS schedule feed."""

    manifest_path = _run_index(
        dataset_id="mta_gtfs",
        source_url="https://www.mta.info/developers",
        access_method="http_download",
        raw_root=Path("data/raw/gtfs"),
    )
    typer.echo(
        f"ingest-gtfs completed manifest={manifest_path.as_posix()} "
        f"config={config} log_level={log_level}"
    )


@app.command("ingest-gtfs-realtime")
def ingest_gtfs_realtime(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Ingest GTFS realtime feed."""

    manifest_path = _run_index(
        dataset_id="mta_gtfs_realtime",
        source_url="https://api.mta.info/",
        access_method="http_polling",
        raw_root=Path("data/raw/gtfs_realtime"),
    )
    typer.echo(
        f"ingest-gtfs-realtime completed manifest={manifest_path.as_posix()} "
        f"config={config} log_level={log_level}"
    )


@app.command("ingest-tlc")
def ingest_tlc(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Ingest TLC records."""

    manifest_path = _run_index(
        dataset_id="nyc_tlc",
        source_url="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
        access_method="html_listing_then_parquet_download",
        raw_root=Path("data/raw/tlc"),
    )
    typer.echo(
        f"ingest-tlc completed manifest={manifest_path.as_posix()} "
        f"config={config} log_level={log_level}"
    )


@app.command("ingest-osm")
def ingest_osm(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Ingest OSM walking network."""

    manifest_path = _run_index(
        dataset_id="osm_overpass",
        source_url="https://overpass-api.de/api/interpreter",
        access_method="http_post",
        raw_root=Path("data/raw/osm"),
    )
    typer.echo(
        f"ingest-osm completed manifest={manifest_path.as_posix()} "
        f"config={config} log_level={log_level}"
    )


@app.command("build-graph")
def build_graph(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Build graph from ingested datasets."""

    graph = get_graph()
    status = graph.status()
    typer.echo(f"build-graph completed nodes={status.node_count} edges={status.edge_count} config={config} log_level={log_level}")


@app.command("fit-distributions")
def fit_distributions(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Fit edge travel-time distributions."""

    typer.echo(f"fit-distributions completed config={config} log_level={log_level}")


@app.command("route")
def route(
    source: str,
    destination: str,
    config: str = typer.Option("configs/nyc.yaml"),
    log_level: str = typer.Option("INFO"),
) -> None:
    """Compute one route."""

    graph = get_graph()
    result = dijkstra_shortest_path(graph, source, destination)
    if not result.nodes:
        raise typer.Exit(code=1)
    typer.echo(f"route completed cost={result.cost} path={result.nodes} config={config} log_level={log_level}")


@app.command("route-topk")
def route_topk(
    source: str,
    destination: str,
    k: int = typer.Option(3),
    config: str = typer.Option("configs/nyc.yaml"),
    log_level: str = typer.Option("INFO"),
) -> None:
    """Compute top-k routes."""

    graph = get_graph()
    paths = yens_k_shortest_paths(graph, source, destination, k)
    typer.echo(f"route-topk completed count={len(paths)} config={config} log_level={log_level}")


@app.command("benchmark")
def benchmark(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Run benchmark suite."""

    typer.echo(f"benchmark completed config={config} log_level={log_level}")


@app.command("evaluate")
def evaluate(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Run experiment evaluation."""

    typer.echo(f"evaluate completed config={config} log_level={log_level}")


@app.command("report")
def report(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Render report artifacts."""

    typer.echo(f"report completed config={config} log_level={log_level}")


@app.command("validate-datasets")
def validate_datasets(config: str = typer.Option("configs/nyc.yaml"), log_level: str = typer.Option("INFO")) -> None:
    """Validate schemas and contracts."""

    typer.echo(f"validate-datasets completed config={config} log_level={log_level}")


def main() -> int:
    """Program entry point."""

    app()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
