# Estimation

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This document defines statistical estimation procedures used for travel-time modeling, uncertainty quantification, and goodness-of-fit diagnostics.

Let observations be $x_1,\\ldots,x_n$, empirical CDF be $F_n$, and bootstrap replicate means be $\\mu_b^\*$.

## Empirical CDF

$$
F_n(t) = \\frac{1}{n}\\sum\_{i=1}^{n}\\mathbf{1}(x_i \\le t)
$$

## Bootstrap confidence interval

$$
\\mu_b^\* = \\frac{1}{n}\\sum\_{i=1}^{n}x\_{i,b}^*,\\quad CI\_{\\alpha}=\\left\[Q\_{\\alpha/2}(\\mu_b^*),Q\_{1-\\alpha/2}(\\mu_b^\*)\\right\]
$$

## Silverman bandwidth

$$
h = 0.9\\min\\left(s,\\frac{IQR}{1.34}\\right)n^{-1/5}
$$

## Kolmogorov Smirnov statistic

$$
D_n = \\sup_t |F_n(t) - F(t)|
$$

## Distribution candidates

| Distribution | Parameters | Support | Fit condition | Rejection criterion |
|:--|:--|:--|:--|:--|
| Normal | mean variance | all real | symmetric residuals | KS p value below alpha |
| Lognormal | mu sigma | positive real | right skewed durations | tail mismatch in QQ diagnostics |
| Gamma | shape scale | positive real | heterogeneous positive durations | AIC and KS jointly unfavorable |

## Time segments

| Segment name | Start time | End time | Weekday flag | Expected trip volume |
|:--|:--|:--|:--|:--|
| early_morning | 05:00:00 | 06:59:59 | true | low |
| am_peak | 07:00:00 | 09:59:59 | true | high |
| midday | 10:00:00 | 15:59:59 | true | medium |
| pm_peak | 16:00:00 | 18:59:59 | true | high |
| evening | 19:00:00 | 22:59:59 | true | medium |
| overnight | 23:00:00 | 04:59:59 | false mixed | low |

## Related

- [Stochastic routing](/docs/math/stochastic_routing.md)
- [NYC TLC dataset](/docs/datasets/nyc_tlc.md)
- [Goodness-of-fit diagnostics](/src/stats/goodness_of_fit.py)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
