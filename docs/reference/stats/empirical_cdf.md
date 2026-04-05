# Statistics Reference: Empirical CDF

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

The empirical cumulative distribution function (ECDF) provides a non-parametric estimate of the probability that a random variable is below a threshold.

## Interface

```python
from src.stats.empirical_cdf import empirical_cdf, cdf_curve

prob = empirical_cdf(samples, value=42.0)
curve = cdf_curve(samples)
```

## Definitions

Given samples $x_1,\\dots,x_n$, the ECDF at value $t$ is:

$$
\\hat{F}(t) = \\frac{1}{n}\\sum\_{i=1}^n \\mathbf{1}[x_i \\le t]
$$

The `cdf_curve` helper returns the set of points $(x\_{(i)}, i/n)$ where $x\_{(i)}$ denotes the $i$-th order statistic.

## Implementation

- Implementation: [src/stats/empirical_cdf.py](/src/stats/empirical_cdf.py)

## Related

- [Risk Metrics](/docs/math/risk_metrics.md)
- [Reliability Analysis Notebook](/notebooks/07_reliability_analysis.ipynb)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
