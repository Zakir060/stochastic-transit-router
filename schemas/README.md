# Schemas Directory

| Field | Value |
|---|---|
| Owner | Data Modeling |
| Department | Data |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Validation schemas and data contracts for ingestion pipeline and API interfaces.

**Purpose:** Enforce data integrity through schema validation at system boundaries



## Overview

This directory contains machine-readable specifications for:
- GTFS schedule entities (stops, routes, trips, stop times)
- GTFS Realtime updates (delays, cancellations, alerts)
- NYC TLC trip records
- OpenStreetMap graph data
- API request and response formats
- Ingest pipeline contracts

All schemas use JSON Schema draft 2020-12 for language-agnostic validation.



## Schema Types

### GTFS Schemas

Static transit schedule specifications:

```
schemas/gtfs/
├── stops.schema.json         # Station and stop definitions
├── routes.schema.json        # Route (line) definitions
├── trips.schema.json         # Service run instances
├── stop_times.schema.json    # Schedule entries (departure/arrival)
├── calendar.schema.json      # Service day patterns
├── calendar_dates.schema.json # Service exceptions
└── shapes.schema.json        # Route geometry
```

**Example: stops.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "stop_id": { "type": "string" },
    "stop_name": { "type": "string" },
    "stop_lat": { "type": "number", "minimum": -90, "maximum": 90 },
    "stop_lon": { "type": "number", "minimum": -180, "maximum": 180 }
  },
  "required": ["stop_id", "stop_name", "stop_lat", "stop_lon"]
}
```

### GTFS Realtime Schemas

Real-time feed specifications (Protocol Buffer JSON representation):

```
schemas/gtfs_realtime/
├── trip_updates.schema.json  # Departure/arrival delays
├── alerts.schema.json        # Service alerts
└── vehicle_positions.schema.json # Current vehicle positions
```

### NYC TLC Schemas

Taxi and for-hire vehicle trip records:

```
schemas/tlc/
├── taxi_trips.schema.json    # Yellow cab trip records
├── fhv_trips.schema.json     # For-hire vehicle records
└── passenger_counts.schema.json # Trip-level aggregates
```

### Graph Schemas

Transit graph artifact specifications:

```
schemas/graph/
├── nodes.schema.json         # Graph vertices (stops, intersections)
├── edges.schema.json         # Graph edges (transit, walking)
└── metadata.schema.json      # Graph version, build date, coverage
```

### API Schemas

REST API request/response contracts:

```
schemas/api/
├── route_request.schema.json    # GET /api/routes parameters
├── route_response.schema.json   # Route result format
├── topk_request.schema.json     # GET /api/routes/topk parameters
├── health_response.schema.json  # Health check response
└── error_response.schema.json   # Error payload format
```

**Example: route_request.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "origin": { "type": "integer" },
    "destination": { "type": "integer" },
    "departure_time": { "type": "integer" },
    "algorithm": { "enum": ["dijkstra", "astar", "yens"] }
  },
  "required": ["origin", "destination", "departure_time"]
}
```

### Ingest Contracts

Pipeline transformation contracts:

```
schemas/contracts/
├── download_manifest.schema.json # Data acquisition record
├── split_manifest.schema.json    # Dataset split definition
└── experiment_config.schema.json # Experiment specification
```



## Validation Usage

### Python Validation

```python
import json
from jsonschema import validate, ValidationError

# Load schema
with open('schemas/api/route_request.schema.json') as f:
    schema = json.load(f)

# Validate request
request_data = {
    "origin": 123,
    "destination": 456,
    "departure_time": 1711900000
}

try:
    validate(instance=request_data, schema=schema)
    print("Valid!")
except ValidationError as e:
    print(f"Invalid: {e.message}")
```

### CLI Validation

```bash
# Validate GTFS stops file against schema
jq . data/raw/gtfs/stops.txt | \
  python -m jsonschema \
    --instance /dev/stdin \
    schemas/gtfs/stops.schema.json
```



## Testing Schemas

Schema tests ensure:
- Valid samples pass validation
- Invalid samples fail validation
- Error messages are informative

**Test location:** `tests/schema/`

**Run schema tests:**

```bash
pytest tests/schema/ -v
```

**Test structure:**

```
tests/schema/
├── test_gtfs_schemas.py         # GTFS validation tests
├── test_gtfs_realtime_schemas.py # Real-time schema tests
├── test_api_schemas.py          # API request/response tests
├── fixtures/
│   ├── gtfs_valid_stops.json    # Valid test data
│   ├── gtfs_invalid_stops.json  # Invalid test data
│   └── ...
```



## Schema Versioning

Schemas follow semantic versioning:

- **MAJOR:** Breaking changes (field removal, type changes)
- **MINOR:** Additions (new optional fields)
- **PATCH:** Documentation fixes

**Schema metadata:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "GTFS Stops",
  "version": "1.2.0",
  "type": "object",
  ...
}
```

When GTFS spec updates, schemas are updated and version is incremented.



## Validation Points

Data validation occurs at these system boundaries:

| Boundary | Validator | Schemas |
|----------|-----------|---------|
| **Data Download** | Ingest pipeline | download_manifest.schema.json |
| **GTFS Parse** | GTFS parser | gtfs/*.schema.json |
| **API Input** | Pydantic models + JSON Schema | api/route_request.schema.json |
| **API Output** | Response serializer | api/route_response.schema.json |
| **Graph Build** | Graph constructor | graph/*.schema.json |
| **Experiment Setup** | Experiment runner | contracts/experiment_config.schema.json |



## Extending Schemas

To add a new schema:

1. Create schema file in appropriate subdirectory
2. Include $schema, title, version, type metadata
3. Document all properties with descriptions
4. Add test fixtures in tests/schema/fixtures/
5. Add test cases in tests/schema/test_*.py
6. Update this README with entry

**Template:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Your Schema Title",
  "description": "Describe what this schema validates",
  "version": "1.0.0",
  "type": "object",
  "properties": {
    "field_name": {
      "type": "string",
      "description": "Field description"
    }
  },
  "required": ["field_name"]
}
```



## Migration

When changing schemas:

1. Increase version number
2. Ensure backward compatibility where possible
3. Document migration path
4. Update validation tests
5. Add migration script if needed

**Example migration:**

```bash
# Old schema accepts "code"
# New schema requires "route_id" instead

# Migration script:
python scripts/migrate_gtfs_schema.py \
  --input data/raw/gtfs/routes.txt \
  --output data/raw/gtfs/routes_migrated.txt \
  --from 1.0.0 --to 2.0.0
```



## Related

- [Schema Validator Code](/src/validation/schema_validator.py)
- [Schema Tests](/tests/schema/)
- [Pydantic Data Models](/src/models/)
- [GTFS Dataset Documentation](/docs/datasets/gtfs.md)
- [API Reference](/docs/reference/api/routes.md)

---

Document Control

- Owner: Data Modeling Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
