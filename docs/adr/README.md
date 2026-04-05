# Architecture Decision Records (ADRs)

| Field | Value |
|---|---|
| Owner | Architecture Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

Documented decisions about system design, algorithm choices, and technical trade-offs.

**Purpose:** Provide transparent rationale for architectural choices to enable critical review, reproducibility validation, and informed future modifications



## Overview

ADRs capture:
- **Context:** Problem statement and constraints
- **Decision:** What was chosen and why
- **Rationale:** Reasoning behind the choice
- **Consequences:** Positive and negative impacts
- **Alternatives:** Options considered and rejected

Each ADR is immutable once accepted (new decisions create new ADRs).



## ADR Index

| ADR | Title | Status | Topic |
|-----|-------|--------|-------|
| [0001](/docs/adr/0001_why_nyc_first.md) | Why NYC first | Accepted | Geography |
| [0002](/docs/adr/0002_graph_representation.md) | Graph representation | Accepted | Data Structure |
| [0003](/docs/adr/0003_data_model.md) | Data model | Accepted | Data Structure |
| [0004](/docs/adr/0004_stochastic_approximation.md) | Stochastic approximation | Accepted | Algorithm |
| [0005](/docs/adr/0005_risk_metric_choice.md) | Risk metric choice | Accepted | Algorithm |
| [0006](/docs/adr/0006_service_architecture.md) | Service architecture | Accepted | Architecture |
| [0007](/docs/adr/0007_storage_approach.md) | Storage approach | Accepted | Infrastructure |
| [0008](/docs/adr/0008_benchmark_protocol.md) | Benchmark protocol | Accepted | Evaluation |
| [0009](/docs/adr/0009_algorithm_selection.md) | Algorithm selection | Accepted | Algorithm |
| [0010](/docs/adr/0010_realtime_feed_strategy.md) | Real-time feed strategy | Accepted | Operations |
| [0011](/docs/adr/0011_walking_edge_model.md) | Walking edge model | Accepted | Data Model |
| [0012](/docs/adr/0012_covariance_approximation.md) | Covariance approximation | Accepted | Algorithm |
| [0013](/docs/adr/0013_online_update_policy.md) | Online update policy | Accepted | Operations |
| [0014](/docs/adr/0014_city_generalization.md) | City generalization | Accepted | Architecture |
| [0015](/docs/adr/0015_license_choice.md) | License choice | Accepted | Governance |



## Statuses

| Status | Meaning | Action |
|--------|---------|--------|
| **Proposed** | Under discussion; not yet decided | Review, comment, vote |
| **Accepted** | Decision made and implemented | Reference for future decisions |
| **Deprecated** | Superseded by newer ADR | Do not reference; see replacement |
| **Superseded** | Replaced by newer ADR (link to replacement) | Archive for history |



## ADR Structure

All ADRs follow this template:

```markdown

# ADR NNNN: [Decision Title]

One-sentence summary of the architectural decision.



## Metadata

| Field | Value |
|-------|-------|
| Status | Proposed/Accepted/Deprecated |
| Date | YYYY-MM-DD |
| Decided By | Names or committee name |
| Implemented | Yes/Partial/No |



## Context

Describe the situation or problem requiring a decision. Include:
- Business/research context
- Technical constraints
- Stakeholders involved
- Why this decision matters

Use 2-4 sentences minimum; explain what triggers the need for a decision.



## Problem Statement

Precise formulation of the question to be decided.

Example:
"How should we represent the transit network as a graph to support both deterministic and stochastic routing with manageable computation time?"



## Decision

Explicit statement of what was decided.

Example:
"Use a NetworkX multigraph with time-dependent edge weights."



## Rationale

Justify the decision by:
1. Addressing the problem statement
2. Comparing alternatives (see Alternatives section)
3. Explaining trade-offs
4. Referencing relevant research or best practices
5. Citing performance/complexity analysis if applicable

Use paragraphs; 2-4 paragraphs typical.



## Consequences

### Positive
- Benefit 1: explanation
- Benefit 2: explanation

### Negative
- Drawback 1: explanation
- Drawback 2: explanation

### Implementation Cost
- Development effort
- Performance impact
- Maintenance burden



## Alternatives Considered

### Option A: [Name]
- Pros: ...
- Cons: ...
- Why rejected: ...

### Option B: [Name]
- Pros: ...
- Cons: ...
- Why rejected: ...



## Related Decisions

- [ADR 0002](/docs/adr/0002_graph_representation.md) - Related graph design
- [Architecture Overview](/docs/architecture/overview.md) - How this fits larger system



## References

- [Paper Title](link) - Relevant research
- [Documentation](link) - Related design docs
```



## Writing Guidelines

### Tone

- Objective, not subjective
- Clear and concise
- Research-backed when possible
- Acknowledge limitations

### Completeness

Every ADR must answer:
1. What was decided?
2. Why was this the best option?
3. What happens because of this decision?
4. What were the alternatives?
5. How does this fit with other decisions?

### References

Link to:
- Related ADRs (use full path)
- Architecture docs
- Code modules (src/...)
- Mathematical formulations
- External resources (papers, standards)



## Process for New ADRs

### 1. Propose

Create new file: `docs/adr/NNNN_decision_title.md` (pull request)

### 2. Discuss

- Post for community review
- Address questions and concerns
- Iterate on rationale and consequences

### 3. Decide

- Update status to "Accepted"
- Document date and decision-maker
- Merge to main

### 4. Implement

- Reference ADR in pull request: "Implements ADR-0005"
- Update code/configuration
- Verify consequences match reality

### 5. Archive

- If superseded: mark "Superseded by ADR-NNNN" and link
- Keep for historical reference
- Never delete



## Examples

### Well-Written Context

"The current shortest-path algorithm uses Dijkstra, which is deterministic and fast. However, transit travel times are uncertain due to schedule variability, real-time delays, and operational constraints. We need a method to quantify this uncertainty and offer users risk-aware routing options alongside fastest-path recommendations. The challenge is balancing computation time (users expect sub-100ms responses) with statistical accuracy (bootstrap resampling is expensive)."

### Weak Context

"We need to handle uncertainty."

(Why? For whom? What's the constraint?)

### Well-Written Rationale

"NetworkX multigraph offers three advantages: (1) It naturally represents multiple transit routes between stops (modeling A/C and E lines both connecting two stations), (2) Python implementation with Cython kernels ensures < 100ms path computation for NYC graph (~12k nodes), benchmarks measured at 1000 queries/sec, (3) Extensive documentation and active community support. Alternatives like custom adjacency matrices sacrifice expressiveness; probabilistic graph libraries (PyG, DGL) add 50+ MB dependency for functionality we don't need in v0.1."

### Weak Rationale

"We chose NetworkX because it's popular."

(Why? Compared to what? What's the evidence?)



## Versioning & Amendments

### No Amendment of Accepted ADRs

Once accepted, ADRs are immutable. If circumstances change:

1. Create new ADR (e.g., ADR-0020: "Revise risk metrics approach")
2. In new ADR, cite predecessor
3. New ADR supersedes old
4. Old ADR marked "Superseded by ADR-0020"

### Rationale for Immutability

- Maintains audit trail
- Documents when/why decisions changed
- Prevents revisionist history
- Supports reproducibility (code references specific ADRs)



## Related

- [Contributing Guide](/CONTRIBUTING.md)
- [Architecture Overview](/docs/architecture/overview.md)
- [Repository README](/README.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
