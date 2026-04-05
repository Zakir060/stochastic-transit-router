# Risk Metrics

| Field | Value |
|---|---|
| Owner | Research Team |
| Department | Documentation |
| Status | Published |
| Version | v1.0 |
| Last Reviewed | 2026-04-05 |
| Audience | Public |
| Classification | Public |

This document defines risk metrics for route ranking and post-hoc analysis under travel-time uncertainty.

Let $T_p$ denote random travel time of path $p$, $\\tau$ an acceptable threshold in seconds, and $\\alpha$ a confidence level.

## Reliability

$$
\\mathrm{Reliability}(p,\\tau) = \\Pr(T_p \\leq \\tau)
$$

## Value at Risk

$$
\\mathrm{VaR}\_{\\alpha}(T_p) = \\inf{t : \\Pr(T_p \\leq t) \\geq \\alpha}
$$

## Conditional Value at Risk

$$
\\mathrm{CVaR}_{\\alpha}(T_p) = \\frac{1}{1-\\alpha}\\int_{\\mathrm{VaR}_{\\alpha}}^{\\infty} t f_{T_p}(t) dt
$$

## Regret

$$
\\mathrm{Regret}(p,\\mathrm{realized}) = T\_{p,realized} - \\min\_{q \\in \\mathcal{A}} T\_{q,realized}
$$

## Risk metric summary

| Metric | Formula reference | Coherent | Use case | Implementation file |
|:--|:--|:--|:--|:--|
| Reliability | Reliability(p,tau) | no | SLA style travel-time guarantees | [src/risk/reliability.py](/src/risk/reliability.py) |
| VaR | VaR_alpha(T_p) | no | percentile tail threshold | [src/risk/var.py](/src/risk/var.py) |
| CVaR | CVaR_alpha(T_p) | yes | robust tail minimization | [src/risk/cvar.py](/src/risk/cvar.py) |
| Regret | Regret(p,realized) | no | post hoc comparative analysis | [src/risk/regret.py](/src/risk/regret.py) |

## Alpha levels

| alpha | Common interpretation | CVaR sensitivity | Recommended use case |
|:--|:--|:--|:--|
| 0.90 | moderate tail focus | medium | commuter planning |
| 0.95 | strong tail focus | high | disruption aware routing |
| 0.99 | extreme tail focus | very high | safety critical planning |

## CVaR coherence note

CVaR is coherent because it satisfies the four axioms.

1. Monotonicity: if $X \\leq Y$ almost surely then $\\mathrm{CVaR}_{\\alpha}(X) \\leq \\mathrm{CVaR}_{\\alpha}(Y)$.
1. Subadditivity: $\\mathrm{CVaR}_{\\alpha}(X+Y) \\leq \\mathrm{CVaR}_{\\alpha}(X) + \\mathrm{CVaR}\_{\\alpha}(Y)$.
1. Translation invariance: $\\mathrm{CVaR}_{\\alpha}(X+c) = \\mathrm{CVaR}_{\\alpha}(X) + c$.
1. Positive homogeneity: $\\mathrm{CVaR}_{\\alpha}(\\lambda X) = \\lambda\\mathrm{CVaR}_{\\alpha}(X)$ for $\\lambda \\ge 0$.

These properties are standard in coherent risk measure literature and motivate CVaR as the default tail metric in robust route ranking.

## Related

- [Stochastic routing](/docs/math/stochastic_routing.md)
- [Evaluation plan](/docs/evaluation/evaluation_plan.md)
- [ADR 0005: Risk metric choice](/docs/adr/0005_risk_metric_choice.md)

---

Document Control

- Owner: Research Team
- Review Cycle: 180 days
- Next Review: 2026-10-02
- Classification: Public
- Contact: zakirbayramov942@gmail.com
