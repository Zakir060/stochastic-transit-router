# Stochastic Routing

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This document defines the stochastic travel-time model, path risk decomposition, and online update equations used by the routing engine.

Let $T_e(t)$ denote travel time random variable for edge $e$ at departure time $t$, and let path $p = (e_1, \\dots, e_k)$.

## Edge-level distribution model

$$
T_e(t) \\sim F_e(t)
$$

The distribution family is estimated from official historical observations conditioned on time-of-day segment and weekday indicator.

## Path expectation

$$
\\mathbb{E}[T_p] = \\sum\_{i=1}^{k} \\mathbb{E}[T\_{e_i}]
$$

## Path variance with covariance

$$
\\mathrm{Var}(T_p) = \\sum\_{i=1}^{k} \\mathrm{Var}(T\_{e_i}) + 2\\sum\_{i=1}^{k}\\sum\_{j=i+1}^{k} \\mathrm{Cov}(T\_{e_i}, T\_{e_j})
$$

When pairwise observations are sparse, the diagonal approximation is explicitly used:

$$
\\mathrm{Var}(T_p) \\approx \\sum\_{i=1}^{k} \\mathrm{Var}(T\_{e_i})
$$

## Path standard deviation

$$
\\sigma_p = \\sqrt{\\mathrm{Var}(T_p)}
$$

## Mean variance score

$$
\\mathrm{Score}\_{\\lambda}(p) = \\mathbb{E}[T_p] + \\lambda \\cdot \\sigma_p
$$

## Lambda interpretation

| lambda | Interpretation | Risk profile |
|:--|:--|:--|
| 0.0 | Fastest expected route | risk neutral |
| 1.0 | One sigma robust route | balanced |
| 2.0 | Strongly conservative route | high risk aversion |

## Online update for mean

$$
\\mu_t = \\alpha\_{ema} x_t + (1 - \\alpha\_{ema})\\mu\_{t-1}
$$

## Online update for variance

$$
\\sigma_t^2 = \\alpha\_{ema}(x_t - \\mu_t)^2 + (1 - \\alpha\_{ema})\\sigma\_{t-1}^2
$$

## Approximation choices

| Approximation | Condition | Error bound | Implementation file |
|:--|:--|:--|:--|
| Diagonal covariance | pair observations below min_obs | empirical deviation monitored by calibration | [src/stats/covariance.py](/src/stats/covariance.py) |
| Segmented stationarity | same segment and weekday only | segment drift bounded by rolling diagnostics | [src/stats/time_segmentation.py](/src/stats/time_segmentation.py) |
| Empirical CDF interpolation | finite sample bins | bounded by sample resolution | [src/stats/empirical_cdf.py](/src/stats/empirical_cdf.py) |

## Related

- [Risk metrics](/docs/math/risk_metrics.md)
- [Estimation](/docs/math/estimation.md)
- [ADR 0012: Covariance approximation](/docs/adr/0012_covariance_approximation.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
