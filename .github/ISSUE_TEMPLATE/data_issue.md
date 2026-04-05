---
name: Data issue
about: Report an ingestion or schema issue with an official data source
title: "[DATA] "
labels: data
assignees: ""

---

<!-- ==============================================================================
     GitHub Issue Template - Data Source Issue
     Route Intelligence Platform

     PURPOSE:
       Report issues with data ingestion, schema validation, or data quality
       from official transit feeds (GTFS, OSM, TLC) or custom data sources.

     WHO SHOULD USE THIS:
       - Data engineers working with feed ingestion
       - Researchers using transit data
       - Users discovering data source problems
       - Anyone identifying data schema incompatibilities

     WHEN TO USE THIS TEMPLATE:
       ✓ GTFS feed missing required fields
       ✓ OSM data transforms incorrectly to graph
       ✓ TLC trip data doesn't match schema
       ✓ Data parser throws validation error
       ✓ Feed quality issues (duplicates, missing stops)
       ✓ Custom data schema incompatibilities

     WHEN NOT TO USE THIS TEMPLATE:
       ✗ Algorithmic bug in routing → Use "Bug report" template
       ✗ API response format issue → Use "Bug report" template
       ✗ Feature request for data handling → Use "Feature request" template
       ✗ Documentation question → Create Discussion instead

     EXPECTED RESPONSE TIME:
       - Data source unavailable: 24 hours acknowledgment
       - Schema breaking change: 2-3 business days
       - Data quality issue: 3-5 business days
       - Enhancement request: Best effort, no SLA

     TIPS FOR GOOD DATA ISSUE REPORTS:
       1. Include exact data source URL
       2. Specify when you accessed the data (timestamp)
       3. Include data sample showing the issue
       4. Provide file hash for exact reproduction
       5. Show schema validation error if available
       6. Link to schema definition (if custom)
       7. Include data source documentation reference

     EXAMPLES OF GOOD DATA ISSUE REPORTS:
       - Title: "[DATA] NYC GTFS feed missing stop_times.txt required field"
       - Includes: Feed URL, timestamp, schema error, affected stop count

       - Title: "[DATA] OSM node data produces invalid graph edges"
       - Includes: Node sample data, transformation error, expected output

     WHAT NOT TO DO:
       ✗ Title: "Data is broken" → Too vague
       ✗ No feed URL → Can't verify data issue
       ✗ No data samples → Can't debug schema issue
       ✗ External blog link only → Need official feed URL
       ✗ Multiple data sources → One issue per source

     DATA VALIDATION CHECKS:
       1. Required fields: Check against official schema
       2. Data types: Stop ID should be string, not int
       3. Foreign keys: Stop references must exist
       4. Enumerations: route_type in valid set
       5. Temporal validity: Dates format YYYYMMDD
       6. Geographic validity: Coordinates in valid range

     MAINTAINER GUIDANCE:
       1. Verify data source URL is accessible and valid
       2. Check if data schema is documented
       3. Attempt reproduction with provided data
       4. Identify root cause: data quality vs schema incompatibility
       5. Propose solution: schema update, adapter fix, or data validation check
       6. Link to data provider's documentation

     ============================================================================== -->

## Source metadata

<!-- Provide complete source information for exact reproduction.

     This ensures maintainers can access exact same data you're analyzing.

     Include:
     - Source URL: Official feed URL (from transitfeeds.com, agency website)
     - Access method: HTTP, SFTP, API endpoint, etc.
     - Acquisition timestamp: Exact date/time you downloaded
     - File hash: md5sum or sha256sum for exact file matching

     Example:
     - Source URL: https://api.transitfeeds.com/v1/feeds/123/latest/download
     - Access method: HTTP GET
     - Timestamp: 2026-04-01 14:30:00 UTC
     - Hash: sha256:a1b2c3d4e5f6...

     Run: sha256sum <file> or md5sum <file>
-->

- Source URL: [Official feed URL, not internal mirror]
- Access method: [HTTP, SFTP, API endpoint, etc.]
- Acquisition timestamp: [YYYY-MM-DD HH:MM UTC]
- File hash: [md5 or sha256 of data file]

## Issue description

<!-- Describe the schema or content issue clearly.

     Include:
     - What's wrong with the data
     - Which data source/file affected
     - Impact on routing or analysis
     - Severity (critical/major/minor)

     Examples:
     - "GTFS feed missing mandatory stop_times.txt file"
     - "OSM ways contain invalid node references (50% of dataset)"
     - "TLC trip records have inconsistent timestamp formats"

     GOOD: "Feed has 500 stops but only 200 have coordinates"
     BAD: "Feed is broken"
-->

Describe the schema or content issue.

## Observed parser behavior

<!-- Describe what the parser/validator actually does.

     Include:
     - Error messages (exact, from logs)
     - Parse failures: How many records fail, what percentage?
     - Mapping conflicts: Field names don't match schema
     - Integrity failures: Foreign key violations, type mismatches

     Include error logs:
     ```
     ERROR: Schema validation failed
     File: stops.txt, Line: 42
     Field 'stop_lat' expected float, got string: "42.3601°N"
     ```

     Include sample of problematic data:
     ```
     stop_id,stop_name,stop_lat,stop_lon
     123,Times Square,40.7580,INVALID
     ```

     GOOD: Include exact error message with line numbers
     BAD: Just say "it fails"
-->

Describe parse errors, mapping conflicts, or integrity failures.

## Expected behavior

<!-- Describe what SHOULD happen per schema/documentation.

     Include:
     - Schema reference (link to official GTFS/OSM spec)
     - Expected data format
     - Expected behavior
     - Link to validator documentation

     Example:
     "Per GTFS specification, stop_lat must be float in range [-90, 90].
      Feed provides latitude as string with degree symbol.
      Parser should either auto-convert or reject with clear error."

     References:
     - GTFS Spec: https://gtfs.org/reference/static-overview/
     - OSM Tags: https://wiki.openstreetmap.org/wiki/Map_features
     - TLC Data: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
-->

Describe expected parser and validation behavior.

## Suggested remediation

<!-- Propose one or more solutions to resolve the issue.

     Options typically include:
     - Schema update: Accept new field format/value
     - Adapter change: Transform data during ingest
     - Quality check: Validate before use, skip bad records
     - Data correction: Fix at source or in preprocessing

     Examples:
     1. Schema: Add support for latitude strings with degree symbols
     2. Adapter: Strip degree symbol during parsing: `lat = float(lat.replace("°", ""))`
     3. Quality: Reject feeds with >5% invalid coordinates
     4. Source: Contact agency to fix feed generation

     Include implementation approach:
     - Which module to modify? (src/ingest/gtfs.py, etc.)
     - What test should validate fix? (test name or new test)
     - Any breaking changes to API?
     - Backward compatibility implications?
-->

Propose schema updates, adapter changes, or quality checks.

## Additional context

<!-- Add any other information that helps understand the issue.

     Include:
     - Related issues (link with #number)
     - Data source documentation links
     - Workarounds you've found
     - Impact on datasets (how many records affected?)
     - Similar issues with other data sources
     - Performance implications

     Example:
     - Affects 15% of NYC feed records
     - Also happens with Boston GTFS (feed #456)
     - Data provider acknowledged bug but no timeline for fix
     - Workaround: Pre-process feed with custom script
-->

Add any additional context here.

---

**Quick checklist:**
- [ ] I included data source URL
- [ ] I provided acquisition timestamp (not just date)
- [ ] I included file hash for exact reproduction
- [ ] I showed actual error message/sample data
- [ ] I referenced schema specification
- [ ] I explained expected vs observed behavior
- [ ] I proposed potential remediation
- [ ] I searched existing data issues (no duplicate)
