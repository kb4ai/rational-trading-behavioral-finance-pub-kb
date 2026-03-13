# Alpha Decay, Execution Cost, and the Quant Case Against Inaction — Summary

*2026-03-13 — Key insight from quant trading models deep dive*

## The Quant Trader's Core Problem

Every signal has a half-life. Every day you don't trade on a positive-edge signal, alpha decays. The formal cost of delay:

```
Cost_delay(Δt) = α₀ · (1 - e^{-λΔt})
```

where α₀ is initial alpha and λ is decay rate. **Inaction on a decaying signal is not neutral — it is measurable wealth destruction.**

## Key Quantitative Findings

### Implementation Shortfall (Perold 1988)

Decomposition: IS = delay cost + market impact + opportunity cost of unfilled orders.

**Delay cost is typically the LARGEST component** — Kissell & Glantz (2003) show delay costs dominate impact costs for institutional orders. The quant problem: optimizing between acting too fast (high impact) and too slow (high decay).

### Alpha Decay Empirics

Di Mascio, Lines & Naik (2015) — measured alpha decay across institutional trades:

* **US equities: 5.6% annual cost of delay** (alpha half-life ~months)
* **European equities: 9.9% annual cost of delay**
* Active manager buys outperform sells → asymmetric decay rates
* Signals with fundamental basis decay slower than momentum/flow signals

### Optimal Execution Frontier (Almgren-Chriss 2000)

Trade-off: risk vs. transaction cost. The efficient frontier maps market impact (trading too fast) against timing risk (trading too slow). **Inaction = maximum timing risk at zero transaction cost.** For positive-edge signals, the interior optimum is ALWAYS inside the frontier, never at the "full inaction" corner.

### No-Trade Zones (Davis & Norman 1990)

With proportional transaction costs ε, optimal policy: do nothing if portfolio weights are within band [w* - Δ, w* + Δ] where:

```
Δ ∝ ε^{1/3} · σ^{2/3}
```

The band is FINITE. Outside it, action is strictly optimal. **Inaction beyond the band boundary is a dominated strategy.**

### Gârleanu & Pedersen (2013) Aim Portfolio

Closed-form optimal trading rate: trade toward an "aim portfolio" that is between current holdings and Markowitz optimal, weighted by transaction cost parameter. **The aim portfolio is NEVER "current holdings" when alpha exists** — some trading is always optimal.

### Momentum as Anti-Inertia Alpha

Jegadeesh & Titman (1993): buying past winners / selling past losers → 1%/month excess returns. **Momentum profits exist precisely because other investors are inert** — they don't exit losers or chase winners fast enough. Moskowitz, Ooi & Pedersen (2012): time-series momentum (trend-following) profits from the aggregate sluggishness of position adjustment.

### The Kelly Argument

Under-betting cost: ΔG = G(f*) - G(f_actual) grows quadratically with edge quality. Missing a 2-Sharpe opportunity costs 4x as much as missing a 1-Sharpe opportunity. **Ed Thorp**: systematic full-Kelly or Half-Kelly betting was the entire foundation of Princeton-Newport Partners and the first hedged equity portfolio.

## Practitioner Perspectives

* **Renaissance Technologies** (~66%/yr gross, ~39%/yr net for 30 years): extreme anti-inaction through rapid systematic turnover. Median holding period ~2 days. The most successful hedge fund in history is built on the principle that every signal must be acted on before it decays.

* **AQR (Cliff Asness)**: "Rebalancing is a source of returns, not just risk management." Systematic rebalancing discipline as anti-inertia mechanism. Frazzini, Israel & Moskowitz (2015): most anomaly alphas survive transaction costs, contradicting the "costs eat alpha" excuse for inaction.

* **López de Prado (2018)**: *Advances in Financial Machine Learning* treats all portfolio actions (including hold) as decisions in a formal ML pipeline. Feature importance, triple barrier method, meta-labeling — all designed to make inaction as analyzable as action.

*Full document: [core-research/quant-models-inaction-cost-systematic-trading.md](../../core-research/quant-models-inaction-cost-systematic-trading.md)*
