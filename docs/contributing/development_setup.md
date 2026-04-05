# Development Setup

| Field | Value |
|---|---|
| Owner | Dev Team |
| Department | Documentation |
| Status | Active |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This guide describes local setup for development, testing, and linting.

## Setup steps

1. Create and activate Python virtual environment.
1. Install editable dependencies.
1. Install pre-commit hooks.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e .[dev,test,benchmarks,notebooks]
pre-commit install
```

## Verification

```powershell
ruff check .
ruff format --check .
mdformat --check README.md AUTHORS.md $(Get-ChildItem docs -Recurse -File -Filter *.md | Select-Object -ExpandProperty FullName)
mypy src
pytest -q
```

## Related

- [Contributing](/CONTRIBUTING.md)
- [Pre-commit configuration](/.pre-commit-config.yaml)
- [Project metadata](/pyproject.toml)

---

Document Control

- Owner: Development Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
