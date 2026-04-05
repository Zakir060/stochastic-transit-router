# Code Style

| Field | Value |
|---|---|
| Owner | Dev Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This document defines style constraints for Python, configuration files, and documentation.

## Rules

- Python uses Ruff formatting and lint rules.
- Type annotations are required in public functions.
- Public modules and functions include docstrings with assumptions and complexity when algorithmic.
- Source files include SPDX identifier comments.
- Markdown files are formatted with `mdformat` (see CI).
- Do not hardcode secrets or API credentials.

## Naming

- snake_case for modules and functions.
- PascalCase for dataclasses and exception types.
- UPPER_CASE for constants.

## Related

- [Ruff configuration](/.ruff.toml)
- [Mypy configuration](/.mypy.ini)
- [ADR 0009: Algorithm selection](/docs/adr/0009_algorithm_selection.md)

---

Document Control

- Owner: Development Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
