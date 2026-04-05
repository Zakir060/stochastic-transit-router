# Statistics Reference: Covariance

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This page documents the covariance helper used by risk and robustness components.

## Interface

```python
from src.stats.covariance import covariance

value = covariance(x, y, min_obs=30)
```

## Sparse fallback policy

When the number of paired observations is below `min_obs` (or below 2), the function returns `0.0` instead of raising, to provide a conservative fallback in low-data regimes.

## Implementation

- Implementation: [src/stats/covariance.py](/src/stats/covariance.py)

## Related

- [Covariance Approximation ADR](/docs/adr/0012_covariance_approximation.md)
- [Risk Metrics](/docs/math/risk_metrics.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
