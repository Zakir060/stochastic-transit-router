# Module Boundaries

| Field | Value |
|---|---|
| Owner | Architecture Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

This document defines allowed dependency directions between major packages to prevent cyclic imports and preserve a clean architecture.

## Dependency policy

| From module | To module | Allowed | Justification |
|:--|:--|:--|:--|
| src/algorithms | src/graph | yes | Algorithms consume graph abstractions |
| src/graph | src/algorithms | no | Graph layer must stay algorithm agnostic |
| src/api | src/evaluation | yes | Endpoints expose experiment metadata |
| src/evaluation | src/api | no | Evaluation must run without service runtime |

## Related

- [Architecture overview](/docs/architecture/overview.md)
- [ADR 0006: Service architecture](/docs/adr/0006_service_architecture.md)
- [ADR 0014: City generalization](/docs/adr/0014_city_generalization.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
