# ADR 0015: License choice

| Field | Value |
|---|---|
| Owner | Architecture Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Internal |
| Classification | Internal |

| Field | Value |
| --- | --- |
| Status | Accepted |
| Date | 2026-04-05 |

## Context

The repository needs a legally clear, European context compatible, copyleft license that supports open collaboration while preserving downstream obligations to share modifications under equivalent terms.

## Decision

License the repository under the European Union Public Licence version 1.2 with SPDX identifier EUPL-1.2.

## Rationale

EUPL-1.2 is approved by the European Commission, supports multilingual official texts, and includes a compatibility framework for several widely used copyleft licenses.

## Consequences

- pyproject.toml and CITATION.cff specify EUPL-1.2 as license metadata.
- Downstream distributors must preserve notices, provide license text access, and share source for distributed modifications.

## Related

- [AUTHORS](/AUTHORS.md)
- [CITATION](/CITATION.cff)
- [Repository README](/README.md)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
