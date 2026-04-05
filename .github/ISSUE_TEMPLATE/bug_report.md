---
name: Bug report
about: Report a reproducible defect in routing, ingest, stats, or API behavior
title: "[BUG] "
labels: bug
assignees: ""

---

<!-- ==============================================================================
     GitHub Issue Template - Bug Report
     Route Intelligence Platform

     PURPOSE:
       Report bugs/defects in functioning code. Use this template when something
       that should work is broken, producing wrong results, or crashing.

     WHO SHOULD USE THIS:
       - Developers finding bugs in their own code
       - Users/researchers discovering bugs in deployed code
       - QA/testers validating functionality
       - Anyone reproducing existing bug report

     WHEN TO USE THIS TEMPLATE:
       ✓ API endpoint returns error 500
       ✓ Route computation produces wrong result
       ✓ Data ingest fails with cryptic error
       ✓ Performance degradation after update
       ✓ Crash/traceback in logs
       ✓ Incorrect calculation or output

     WHEN NOT TO USE THIS TEMPLATE:
       ✗ Feature request → Use "Feature request" template
       ✗ Data source issue → Use "Data issue" template
       ✗ Question about usage → Create Discussion instead
       ✗ Documentation unclear → Create Docs issue

     EXPECTED RESPONSE TIME:
       - Severity Critical (system down): 2 hours acknowledgment
       - Severity High (major feature broken): 24 hours acknowledgment
       - Severity Medium (workaround available): 3-5 business days
       - Severity Low (minor cosmetic issue): Best effort, no SLA

     TIPS FOR GOOD BUG REPORTS:
       1. Include minimal reproducible example (MRE)
       2. Provide exact error message/traceback
       3. List environment details (OS, Python version)
       4. Explain what you expected vs what actually happened
       5. Share data source URL/timestamp if relevant
       6. Include log excerpts (error logs, not entire log file)
       7. One bug per issue (don't combine multiple bugs)

     EXAMPLES OF GOOD BUG REPORTS:
       - Title: "[BUG] Dijkstra returns wrong shortest path for NYC subway"
       - Includes: Steps to reproduce, expected path vs actual path, GTFS feed URL

       - Title: "[BUG] API endpoint /routes/<id> returns 500 on valid request"
       - Includes: Request example, error traceback, environment info

     WHAT NOT TO DO:
       ✗ Title: "It doesn't work" → Too vague
       ✗ No reproduction steps → Can't verify bug
       ✗ Just error message → No context
       ✗ "Fix this ASAP" → No urgency modifier respected
       ✗ Multiple unrelated bugs → One issue per bug

     MAINTAINER GUIDANCE:
       1. Verify reproducibility before work starts
       2. Check if already reported (search existing issues)
       3. Assign severity: Critical/High/Medium/Low
       4. Request additional info if needed (use template questions)
       5. Link to related PRs/commits if fixing

     ============================================================================== -->

## Description

<!-- Provide a clear, concise description of what isn't working.
     Be specific about what component is affected.

     Examples:
     - "Route computation returns path with 0 cost (should be positive)"
     - "API returns 500 error when calling /routes/find?from=...&to=..."
     - "Data ingest hangs after 10 minutes on large GTFS feed"

     GOOD: "When routing from stop A to stop B, algorithm returns wrong path"
     BAD: "Routing doesn't work"
-->

## Reproduction

<!-- Provide exact steps to reproduce the bug. Someone else should be able to
     follow these steps and see the same bug.

     Include:
     - Code snippet or API call
     - Input data or parameters
     - Any configuration changes
     - Commands run

     Example:
     1. Load GTFS feed from https://transitfeeds.com/feed/123
     2. Call API: POST /routes/find with {"from": "stop:1", "to": "stop:2"}
     3. Observe response includes invalid path

     PRO TIP: Include minimal reproducible example (MRE)
     - Smallest code sample that shows bug
     - Use test data from tests/data/fixtures/
     - Remove irrelevant details
-->

1. Step one
2. Step two
3. Step three

## Expected behavior

<!-- Describe what SHOULD happen.

     Include:
     - Expected output/response
     - Expected performance (time, memory)
     - Expected behavior according to docs

     Example:
     "When routing stops A→B, should return shortest path with total cost < 100"

     Reference docs if applicable:
     - API documentation: docs/reference/api.md
     - Algorithm docs: docs/math/algorithms.md
-->

Describe expected behavior.

## Actual behavior

<!-- Describe what ACTUALLY happens.

     Include:
     - Actual output/response
     - Error message (full traceback if available)
     - Actual performance (time, memory)
     - Screenshots if visual issue

     If error message exists, paste full traceback:
     ```
     Traceback (most recent call last):
       File "src/api/server.py", line 42, in compute_route
         result = dijkstra(graph, start, end)
     ...
     ```

     If output is wrong, show:
     - What you got: [actual output]
     - What you expected: [expected output]
-->

Describe actual behavior.

## Environment

<!-- Provide environment details. These help reproduce the issue.

     Run this to get exact versions:
       python --version
       pip show stochastic-transit-router
       git rev-parse HEAD

     Include:
     - OS: Ubuntu 22.04, Windows 11, macOS 13, etc.
     - Python version: Run 'python --version'
     - Package version: Run 'pip show stochastic-transit-router'
     - Installation method: pip, from source, Docker, etc.
     - Configuration: Any custom config in config/ directory
-->

- OS: [e.g., Ubuntu 22.04, Windows 11]
- Python version: [e.g., 3.12.1]
- Package version: [e.g., 0.1.0 or git commit hash]
- Installation method: [pip, from source, Docker]
- Configuration: [Any non-default config]

## Data source context

<!-- If bug involves data ingest, provide data source information.

     Include:
     - Official feed URL (from transitfeeds.com or agency website)
     - Access timestamp (when you downloaded data)
     - File hash: md5sum <file> or sha256sum <file>
     - Any transformations applied

     Example:
     - Source URL: https://api.transitfeeds.com/v1/feeds/123/feed
     - Timestamp: 2026-04-01 14:30 UTC
     - Hash: sha256:abc123def456...

     This helps maintainers reproduce with exact same data.
-->

Specify the official feed or dataset URL and timestamp involved in the issue.

## Additional context

<!-- Add any other information that might help debug the issue.

     Include:
     - Recent code changes that broke it
     - Related issues (link with #number)
     - Workarounds you've found
     - Performance metrics (memory, CPU, time)
     - Log excerpts (error logs, not entire file)
     - Screenshots for visual issues

     Example:
     - Started after updating to v0.2.0
     - Related to issue #42 (timezone handling)
     - Workaround: Use simplified routing algorithm
     - Memory usage: 2GB (expected: <500MB)
-->

Add any additional context here.

---

**Quick checklist:**
- [ ] I included steps to reproduce the bug
- [ ] I described expected vs actual behavior
- [ ] I provided environment details
- [ ] I searched existing issues (no duplicate)
- [ ] I included relevant error messages/logs
- [ ] For data issues, I included data source URL
