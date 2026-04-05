# ADR 0006: Service architecture

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

The project must expose routing capabilities to both automation pipelines and interactive users while maintaining one consistent computation core and avoiding duplicated business logic.

## Decision

Adopt a shared service layer invoked by both FastAPI endpoints and Typer CLI commands.

## Rationale

A shared service core reduces drift between interfaces, centralizes validation and logging, and simplifies test coverage because API and CLI can be validated against the same behavior.

## Consequences

- API and CLI modules are thin adapters around service objects.
- Integration tests exercise parity between endpoint responses and CLI outputs.
- Logging, error handling, and tracing conventions stay consistent across interfaces.

## Related

- [Architecture Overview](/docs/architecture/overview.md)
- [ADR 0009: Algorithm selection](/docs/adr/0009_algorithm_selection.md)
- [OpenAPI Spec](/docs/api/openapi.yaml)

---

Document Control

- Owner: Architecture Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Internal
- Contact: olaf.laitinen@uni.lu
