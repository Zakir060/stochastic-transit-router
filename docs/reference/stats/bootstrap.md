# Statistics Reference: Bootstrap Mean Confidence Interval

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This page documents the bootstrap utilities used for lightweight uncertainty quantification in metric reporting.

## Interface

```python
from src.stats.bootstrap import bootstrap_mean_ci

low, high = bootstrap_mean_ci(samples, iterations=1000, alpha=0.05, seed=20260405)
```

## Method

The implementation uses a percentile bootstrap for the sample mean:

1. Resample $n$ observations with replacement for `iterations` rounds.
1. Compute the mean for each resample.
1. Return the empirical $(\\alpha/2)$ and $(1-\\alpha/2)$ quantiles of the bootstrap means.

## Determinism

The function uses an explicit PRNG seed by default so that test and benchmark outputs are reproducible.

## Implementation

- Implementation: [src/stats/bootstrap.py](/src/stats/bootstrap.py)

## Related

- [Reproducibility](/docs/operations/reproducibility.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
