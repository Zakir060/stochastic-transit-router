---
name: Feature request
about: Propose an enhancement with clear algorithmic and operational value
title: "[FEATURE] "
labels: enhancement
assignees: ""

---

<!-- ==============================================================================
     GitHub Issue Template - Feature Request
     Route Intelligence Platform

     PURPOSE:
       Propose new features, algorithms, or enhancements with clear value
       proposition. This template requires technical rigor and analysis.

     WHO SHOULD USE THIS:
       - Researchers proposing new algorithms
       - Users requesting capability enhancements
       - Developers proposing API changes
       - Data engineers suggesting new data sources
       - DevOps proposing operational improvements

     WHEN TO USE THIS TEMPLATE:
       ✓ New routing algorithm (e.g., time-dependent routing)
       ✓ Additional data source support (e.g., real-time bus positions)
       ✓ API endpoint enhancement (e.g., batch routing)
       ✓ New statistic or metric (e.g., accessibility analysis)
       ✓ Performance optimization (e.g., caching strategy)
       ✓ New CLI command or tool

     WHEN NOT TO USE THIS TEMPLATE:
       ✗ Bug report → Use "Bug report" template
       ✗ Data source issue → Use "Data issue" template
       ✗ Documentation question → Create Discussion instead
       ✗ Implementation-specific questions → Create Discussion instead

     EXPECTED RESPONSE TIME:
       - Enhancement aligned with roadmap: 1 week assessment
       - Community voting feature: 2 weeks for voting period
       - Out-of-scope feature: 3-5 days explanation of reasoning
       - Large feature requests: May schedule design review meeting

     FEATURE PRIORITIZATION CRITERIA:
       1. Algorithmic value: Does it improve routing quality?
       2. Research relevance: Supports published academic work?
       3. User demand: Multiple requests or high community interest?
       4. Implementation scope: Feasible within reasonable effort?
       5. Backward compatibility: Non-breaking or graceful deprecation?
       6. Performance impact: Acceptable runtime/memory characteristics?
       7. Maintenance burden: Sustainable long-term?

     TIPS FOR GOOD FEATURE REQUESTS:
       1. Start with problem statement (not solution)
       2. Provide mathematical formulation if applicable
       3. Include complexity analysis (time/space)
       4. Specify data dependencies (which datasets needed)
       5. Describe API/interface changes
       6. Propose validation tests
       7. Link to academic papers/standards if applicable

     EXAMPLES OF GOOD FEATURE REQUESTS:
       - Title: "[FEATURE] Time-dependent routing using temporal availability"
       - Includes: Problem statement, algorithm sketch, complexity analysis,
         data requirements, API changes, validation approach

       - Title: "[FEATURE] Accessibility routing for wheelchair users"
       - Includes: Use case, curb cut data requirements, test scenarios,
         ADA compliance references

     WHAT NOT TO DO:
       ✗ Title: "Make it faster" → Too vague, no specifics
       ✗ No problem statement → Can't evaluate need
       ✗ No validation plan → How do we know if it works?
       ✗ "Everyone wants this" → No evidence of demand
       ✗ Implementation details only → Missing why it matters

     COMMUNITY VOTING/DISCUSSION:
       1. Well-formed feature requests go to community discussion
       2. Community votes over 2-week period
       3. High-vote features prioritized for implementation
       4. Votes considered alongside criteria above

     MAINTAINER GUIDANCE:
       1. Assess alignment with project roadmap
       2. Check feasibility: scope, complexity, dependencies
       3. Evaluate research/algorithmic value
       4. Consider maintenance burden
       5. Request clarification if needed
       6. Propose community voting if broadly interesting
       7. Document decision and reasoning

     ============================================================================== -->

## Problem statement

<!-- Describe the practical or scientific problem this feature would solve.

     Start with the problem, NOT the solution. Help reviewers understand
     the need before diving into implementation details.

     Include:
     - What problem exists today?
     - Who is affected by this problem?
     - What's the impact of not solving this?
     - What constraints/requirements exist?

     Examples (GOOD):
     - "Currently routes ignore real-time service delays. Users receive
        static routes that may become invalid when trains are delayed."
     - "Accessibility analysis requires manual data checking. No programmatic
        way to determine if route is wheelchair accessible."

     Examples (BAD):
     - "Add time-dependent routing" (no problem stated)
     - "Make algorithm faster" (too vague)
-->

Describe the practical or scientific problem.

## Proposed change

<!-- Describe HOW this problem should be solved: the solution design.

     Include:
     - Proposed behavior (what users will see)
     - API contract: New endpoints or method signatures
     - Configuration impact: New config options needed?
     - Backward compatibility: Breaking changes?
     - Default behavior if configurable

     For routing/algorithm features include:
     - High-level algorithm sketch (pseudocode ok)
     - Key design decisions
     - Alternative approaches considered

     Example (GOOD):
     "Add new endpoint POST /routes/find/time-dependent:
      Request: {from: stop_id, to: stop_id, departure_time: ISO8601}
      Response: {route_id, duration_minutes, delay_probability, alternatives}
      Config option: enable_temporal_analysis=true
      Backward compatible: existing /routes/find unchanged"

     Example (BAD):
     "Make it support time-dependent routing" (no detail)
-->

Describe the proposed behavior, API contract, and configuration impact.

## Mathematical and algorithmic implications

<!-- Provide mathematical formulation and complexity analysis.

     Include:
     - Algorithm description (pseudocode or formula)
     - Time complexity: Big-O analysis (e.g., O(V log V))
     - Space complexity: Memory requirements (e.g., O(V))
     - Known limitations or edge cases
     - Comparison to alternatives

     Only include if algorithmically relevant. Skip for UI/data-only features.

     Example (GOOD):
     "Algorithm: Modified Dijkstra with time-dependent edge weights
      Complexity: O((V + E) log V) where E may grow with time discretization
      Edge case: Handles periodic schedules (24-hour cycles)
      Alternative: A* with time heuristic (same complexity, potentially faster)"

     Reference papers if applicable:
     - Dijkstra, E. W. (1959). "A note on two problems in connexion with graphs"
     - Pyrga, E., et al. (2008). "Efficient algorithms for time-dependent networks"

     Example (BAD):
     "Use standard Dijkstra" (no analysis)
-->

Provide formulas, complexity impact, and required assumptions when relevant.

## Data implications

<!-- Specify which official datasets are required and data provenance tracking.

     Include:
     - Required datasets: Which GTFS, OSM, TLC feeds?
     - Data availability: Is data freely available and up-to-date?
     - Data freshness requirements: Real-time? Daily? Weekly?
     - Data quality dependencies: Any specific quality thresholds?
     - Provenance tracking: How to record data source/version used?

     Example (GOOD):
     "Requires: Real-time GTFS-RT service alerts feed
      Availability: Most US agencies provide via GTFS-RT standard
      Freshness: Updates every 30-60 seconds (real-time)
      Quality: Requires <5% missing data timestamps
      Provenance: Record feed URL, timestamp, hash with each computation"

     Example (BAD):
     "Use traffic data" (no specifics about source or availability)
-->

State which official datasets are required and how provenance is recorded.

## Validation plan

<!-- Describe how to validate the feature works correctly.

     Include:
     - Unit test scenarios: What should pass/fail?
     - Integration tests: End-to-end workflows
     - Regression tests: Performance/accuracy baselines
     - Edge cases to test
     - Success criteria: What defines "working correctly"?

     Examples of good test scenarios:
     - "Unit: Algorithm returns empty set for unreachable destinations"
     - "Integration: API endpoint with real GTFS data returns valid routes"
     - "Regression: Performance within 10% of baseline Dijkstra"
     - "Edge case: Handles circular routes, same start/end stop"

     Example (GOOD):
     "Validation:
      1. Unit: Time-dependent distance calculation matches formula
      2. Integration: End-to-end on NYC GTFS with real-time delays
      3. Regression: Query time <100ms (vs current 50ms baseline)
      4. Edge case: Handles no-service periods (overnight)
      5. Success: 95%+ route accuracy vs ground truth"

     Example (BAD):
     "Test it works" (too vague)
-->

Describe unit, integration, and regression tests needed for acceptance.

## Additional context

<!-- Add any other information that helps evaluate the feature.

     Include:
     - Related academic papers or standards
     - Community demand or feedback
     - Competitive features in other tools
     - Performance/scaling implications
     - Deployment considerations
     - Links to related issues/discussions

     Example:
     - Requested by: 5+ community members
     - Paper: "Efficient time-dependent shortest paths" (reference)
     - Performance: May need graph preprocessing for large networks
     - Deployment: Requires new config parameter for time discretization
     - Related: Issue #42 (partial implementation started)
-->

Add any additional context here.

---

**Quick checklist:**
- [ ] I stated the problem clearly (not just the solution)
- [ ] I described the proposed change with specifics
- [ ] I included algorithmic/mathematical analysis (if applicable)
- [ ] I specified required datasets and data provenance
- [ ] I described validation/test approach
- [ ] I checked for related issues/discussions
- [ ] I provided complexity analysis (time/space)
- [ ] I considered backward compatibility
- [ ] I reviewed alignment with project roadmap
