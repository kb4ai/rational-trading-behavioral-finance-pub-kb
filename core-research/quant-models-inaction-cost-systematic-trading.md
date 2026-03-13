# Quantitative Models of Inaction Cost in Systematic Trading

**[Collected 2026-03-13 | Claude Sonnet 4.6 with web research]**

**Audience:** Quantitative traders, systematic portfolio managers, algorithmic strategists.

**Central claim:** In systematic trading, inaction is not a safe default — it is a costly decision with quantifiable consequences in every major formal framework. This document catalogs the quantitative evidence across transaction cost analysis, optimal execution theory, portfolio rebalancing, alpha decay, reinforcement learning, risk management, and momentum research.

---

## 1. Transaction Cost Analysis and Optimal Execution

### 1.1 Almgren-Chriss (2000): The Efficient Frontier of Execution

**Full citation:** Almgren, R., & Chriss, N. (2000). Optimal execution of portfolio transactions. *Journal of Risk*, 3, 5–39.

**Core framework:** Almgren-Chriss constructs an execution efficient frontier analogous to Markowitz's portfolio frontier — but in the space of (expected implementation cost, variance of implementation cost). Every point on the frontier represents a different speed of execution.

**Price dynamics model:**

* Unperturbed mid-price: $\mathrm{d}\bar{S}_t = \sigma S_0\,\mathrm{d}W_t$
* With permanent impact: $S_t = \bar{S}_t + \theta(X_0 - X_t)$
* Temporary impact per share: $\eta v_t$ (linear in trading speed $v_t$)

**Total execution cost:**

$$C_{0,T} = X_0 S_0 + \int_0^T X_t \sigma S_0\,\mathrm{d}W_t + \eta\int_0^T v_t^2\,\mathrm{d}t + \frac{\theta}{2}$$

**Optimal mean-variance trajectory** (solving $\min_v \mathbf{E}[C] + \lambda \mathrm{Var}[C]$):

$$X_t = X_0 \cdot \frac{\sinh\!\bigl[\kappa(T-t)\bigr]}{\sinh(\kappa T)}, \quad \kappa = \sqrt{\frac{\lambda\sigma^2}{\eta}}$$

where $\kappa$ is the "urgency parameter." High $\lambda$ (risk-averse trader) → high $\kappa$ → front-loaded execution (most shares sold early). Low $\lambda$ → $\kappa \to 0$ → TWAP (uniform schedule).

**The cost of inaction within execution:** Slowing down to TWAP vs. front-loaded execution trades lower market impact for higher variance exposure. The variance of the TWAP schedule is $\mathrm{Var}^{\mathrm{TWAP}} = \sigma^2 S_0^2 X_0^2 T / 3$. The model makes precise when delayed execution (relative to optimal) shifts you off the efficient frontier.

**Risk-neutral minimum:** $\mathbf{E}[C]$ is minimized by TWAP (constant $v_t = X_0/T$), yielding $\mathbf{E}[C_{\mathrm{min}}] = \eta X_0^2/T + \theta X_0$. Delaying the start by $\delta t$ increases expected cost by the variance cost of exposure during the delay period.

**Key implication for inaction-as-action thesis:** Under Almgren-Chriss, the choice to execute slowly (or not at all) is explicitly modeled as a position on the efficient frontier with a defined expected cost and variance. There is no "free" delay — every moment of non-execution is a quantity $X_t$ that remains exposed to $\sigma$ with zero offsetting benefit.

**Implementation / code:** Joshua Jacob's public solver at `github.com/joshuapjacob/almgren-chriss-optimal-execution`.

---

### 1.2 Perold (1988): Implementation Shortfall — Quantifying Delay Cost

**Full citation:** Perold, A. F. (1988). The implementation shortfall: Paper versus reality. *Journal of Portfolio Management*, 14(3), 4–9.

**Core definition:** Implementation Shortfall (IS) = Return(paper portfolio) − Return(actual portfolio), where the paper portfolio assumes instantaneous, costless execution at the decision-point price $P_0$.

**Cost decomposition:**

$$\mathrm{IS} = \underbrace{(P_{\mathrm{execution}} - P_0) \cdot Q_{\mathrm{executed}}}_{\text{execution cost}} + \underbrace{(P_{\mathrm{close}} - P_0) \cdot Q_{\mathrm{unexecuted}}}_{\text{opportunity cost}} + \underbrace{\mathrm{commissions}}_{\text{explicit}}$$

**Radical insight for inaction:** The opportunity cost term makes explicit that every unexecuted share has a cost equal to how much the price moved away from the decision-price during the delay. If the stock rises 2% before the order is filled, the missed 2% on unexecuted quantity is a *measurable loss* — not a "non-event."

**Why IS displaced VWAP as the gold standard:** VWAP benchmarks implicitly assume the right time to trade was spread uniformly through the day. IS anchors to the decision point, revealing the true cost of algorithmic latency and portfolio-manager hesitation. Quantitative brokers have institutionalized IS since the 1990s.

**Practitioner resource:** Quantitative Brokers blog: "A Brief History of Implementation Shortfall" at `quantitativebrokers.com`.

---

### 1.3 Kissell & Glantz (2003): Optimal Trading Strategies

**Full citation:** Kissell, R., & Glantz, M. (2003). *Optimal Trading Strategies: Quantitative Approaches for Managing Market Impact and Trading Risk*. AMACOM.

**Framework:** Introduces a unified cost model decomposing total transaction cost into:

* **Explicit costs:** Commissions, fees, taxes
* **Implicit costs — execution component:** Market impact + spread
* **Implicit costs — opportunity component:** Cost of shares not executed (matches Perold's IS opportunity cost)
* **Timing risk:** Variance from price movement during execution window

**Key contribution:** Provides closed-form trading curves that explicitly trade off market impact (increases with execution speed) against opportunity/timing costs (increase with execution slowness). At every speed level, the *cost of not trading faster* is a computable quantity.

**Quantitative Brokers** (firm) was founded specifically to operationalize Kissell's IS-minimization framework via smart-order routing algorithms.

---

### 1.4 Frazzini, Israel & Moskowitz: Real-World Transaction Costs

**Full citation:** Frazzini, A., Israel, R., & Moskowitz, T. J. (2015). Trading costs of asset pricing anomalies. *Working paper, AQR*. See also Frazzini, A., Israel, R., & Moskowitz, T. J. (2018). Trading costs. *SSRN 3229719*.

**Data:** 1.7 trillion USD of live institutional trade execution data across 21 developed equity markets over 19 years.

**Core finding:** Actual trading costs are an order of magnitude *smaller* than previous (TAQ-based) estimates suggested — implying that systematic strategies survive at larger AUM than academics assumed. This has a direct bearing on inaction: if costs of *trading* are lower than believed, the effective cost-benefit ratio of *action* is more favorable, and the inaction zone should be narrower.

**Specific cost estimates (approximate magnitudes):** Value, momentum, and size anomalies show execution costs of 20–57 bps for mid-turnover strategies (Novy-Marx & Velikov 2016 corroboration).

**Implication:** Systematic strategies that avoid trading due to overcautious cost assumptions are leaving money on the table. The *real* cost of not trading an anomaly is often larger than the cost of trading it.

---

### 1.5 Chiyachantana & Jain: Direct Measurement of Opportunity Cost of Unexecuted Decisions

**Full citation:** Chiyachantana, C. N., & Jain, P. K. (2008). The opportunity cost of inaction in financial markets: An analysis of institutional decisions and trades. *SSRN 1220582*.

**Key finding:** For institutional buy decisions, the opportunity cost component of IS (unexecuted portion rising in price) systematically dominates the execution cost component in trending markets. The paper decomposes IS into execution cost vs. opportunity cost across bull, bear, and neutral markets.

**Direct bearing on thesis:** This paper empirically quantifies the opportunity cost of non-execution for large institutional players, showing that the cost of delay is not hypothetical — it shows up in fund performance with measurable magnitude.

---

## 2. Optimal Portfolio Rebalancing with Transaction Costs

### 2.1 Davis & Norman (1990): The No-Trade Zone

**Full citation:** Davis, M. H. A., & Norman, A. R. (1990). Portfolio selection with transaction costs. *Mathematics of Operations Research*, 15(4), 676–713. DOI: 10.1287/moor.15.4.676

**Problem setup:** Investor with bank account (fixed interest $r$) and stock (log-normal, drift $\mu$, volatility $\sigma$). Proportional transaction costs: $\lambda$ (buying), $\mu'$ (selling). CRRA utility.

**Main result (the no-trade zone theorem):** The optimal policy is characterized by a wedge-shaped no-transaction (NT) region in $(y, z)$ space (bank holdings × stock holdings). The NT region is a convex cone. Optimal policy:

* If $(y,z) \in \mathrm{NT}$: do nothing (inaction is optimal)
* If $(y,z)$ breaches the buy boundary: buy exactly to the buy boundary
* If $(y,z)$ breaches the sell boundary: sell exactly to the sell boundary

**Key parameter dependence:** Band width is approximately proportional to $(\text{transaction cost})^{1/3}$ and inversely related to volatility. High-volatility assets have narrower bands because the cost of drift from optimal is larger relative to transaction cost savings.

**Implication for inaction-as-action:** The NT band is the precise region where inaction is optimal — but it is finite and model-derived, not infinite. Outside this band, inaction has a quantifiable cost in expected utility terms. The framework makes inaction a *first-class optimality condition* with specific bounds rather than a vague default.

**DOI:** 10.1287/moor.15.4.676

---

### 2.2 Leland (1996): Optimal Rebalancing for Institutional Portfolios

**Full citation:** Leland, H. E. (1996). Optimal asset rebalancing in the presence of transactions. *SSRN 1060* (Working paper, UC Berkeley Haas).

**Framework:** Generalizes Davis-Norman to multi-asset portfolios with target weight $w^*$. Optimal policy: no-trade band of width $\pm \delta w$ around target.

**Band-width formula (approximate):**

$$\delta w \approx \left(\frac{3\lambda \sigma^2 w^*(1-w^*)}{4\rho}\right)^{1/3}$$

where $\lambda$ = transaction cost rate, $\sigma$ = asset volatility, $w^*$ = target weight, $\rho$ = mean-variance risk tolerance parameter.

**Numeric example from Leland:** For $\lambda = 0.5\%$, $\sigma = 20\%$, $w^* = 0.6$, the band is approximately ±3–5%. Beyond this band, failure to rebalance is suboptimal; within the band, the cost of transacting exceeds the benefit.

**Operational insight:** The formula quantifies *exactly* when inaction (not rebalancing) is rational vs. irrational. An investor who holds when outside the band is paying a measurable utility cost; an investor who trades when inside the band is wasting money on transaction costs.

---

### 2.3 Vanguard Research (2024): Threshold vs. Calendar Rebalancing

**Full citation:** Vanguard Research. (2024, December). *The rebalancing edge: Optimizing target-date fund rebalancing through threshold-based strategies*. Vanguard Institutional.

**Key quantitative findings:**

* Threshold-based rebalancing (200 bps drift triggers rebalance, target 175 bps) outperforms monthly calendar rebalancing by **11–18 bps annually**.
* In high-volatility markets, calendar-based approaches cause substantial drift between rebalance dates; threshold-based approaches correct sooner.
* The 200/175 bps split (trigger at 200, rebalance to 175 not to target) reduces transaction costs vs. rebalancing back to exact target.

**Cost of inaction quantified:** Allowing drift beyond the 200 bps threshold (i.e., not rebalancing when triggered) causes measurable return drag from factor exposure drift.

**URL:** `corporate.vanguard.com/content/dam/corp/research/pdf/the_rebalancing_edge_optimizing_target_date_fund_rebalancing_through_threshold_based_strategies.pdf`

---

### 2.4 DeMiguel, Garlappi & Uppal (2009): When Does Inaction on Optimization Pay?

**Full citation:** DeMiguel, V., Garlappi, L., & Uppal, R. (2009). Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy? *Review of Financial Studies*, 22(5), 1915–1953. DOI: 10.1093/rfs/hhm075

**Finding:** None of 14 optimized portfolio models consistently outperformed equal-weighting (1/N) out-of-sample across 7 empirical datasets, as measured by Sharpe ratio, certainty-equivalent return, or turnover.

**The estimation window paradox:** For a sample-based mean-variance model to beat 1/N with 25 assets, requires ~**3,000 months** of historical data (250 years). For 50 assets: ~6,000 months (500 years). Typical practice uses 120 months.

**The inaction angle:** This paper provides the strongest quantitative argument for *strategic inaction on optimization* — i.e., not aggressively rebalancing to estimated mean-variance optimum when estimation error is high. The cost of the "action" (rebalancing to MV optimum) can exceed the benefit because the optimum estimate is noisy.

**Counter-inaction angle:** However, the paper tests static 1/N, not threshold-based rebalancing that maintains equal weights. Complete inaction (no rebalancing at all) would cause equal weights to drift, eventually performing worse than rebalanced 1/N. The paper implicitly assumes periodic rebalancing of the 1/N benchmark.

---

### 2.5 Novy-Marx & Velikov (2016): Taxonomy of Anomaly Trading Costs

**Full citation:** Novy-Marx, R., & Velikov, M. (2016). A taxonomy of anomalies and their trading costs. *Review of Financial Studies*, 29(1), 104–147. DOI: 10.1093/rfs/hhv063

**Key finding:** Most anomalies with monthly turnover below 50% generate significant net-of-trading-cost excess returns when designed with buy/hold spreads. Anomalies with turnover above 50% (mostly short-term momentum and reversal) are typically subsumed by costs.

**Buy/hold spread technique:** The most effective cost-mitigation strategy — use a more stringent criterion for *establishing* positions than for *maintaining* them. In effect: action threshold > inaction threshold. This is the institutional operationalization of the Davis-Norman no-trade band.

**Execution cost range:** 20–57 bps for mid-turnover strategies.

**Direct implication:** Inaction (maintaining a position that no longer meets entry criteria) is *rational* within the buy/hold spread — this is the quant's formal operationalization of the no-trade zone for factor strategies.

---

## 3. Alpha Decay and Information Half-Life

### 3.1 The Exponential Decay Model

The standard model for trading signal alpha decay:

$$\alpha(t) = \alpha_0 \cdot e^{-\lambda t}$$

where $\lambda$ = decay rate (per unit time), $\alpha_0$ = initial signal strength.

**Cost of waiting:** If the signal decays at rate $\lambda$ and you delay execution by $\Delta t$, the forgone alpha is:

$$\Delta G = \alpha_0 \bigl(1 - e^{-\lambda \Delta t}\bigr) \approx \alpha_0 \lambda \Delta t \quad \text{(for small }\lambda\Delta t\text{)}$$

This is the direct economic cost of inaction when a signal exists. At the half-life $t_{1/2} = \ln(2)/\lambda$, exactly 50% of the original alpha has decayed.

---

### 3.2 Di Mascio, Lines & Naik: Empirical Alpha Decay Costs

**Full citation:** Di Mascio, R., Lines, A., & Naik, N. Y. (2015). Alpha decay. *SSRN 2580551*. Published in *Journal of Finance*, forthcoming (see also journal version).

**Methodology:** Used a mean-reversion signal, simulated lagged versions of the signal (delayed by $n$ days), and measured the annualized return differential between original and lagged strategies.

**Key empirical findings:**

* **US markets:** Average annual alpha decay cost = **5.6%** per unit time delay
* **European markets:** Average annual alpha decay cost = **9.9%** per unit time delay
* **Trend (worsening):** Annual rate of increase in decay cost = 36 bps/year (US), 16 bps/year (Europe)

**Volatility correlation:** Alpha decay is strongly positively correlated with market volatility — in volatile markets, information is priced faster, making delay more costly.

**Mechanism:** As systematic strategies become more prevalent, the marginal speed of price discovery has increased. What was priced over days in 1995 is now priced over hours in 2025.

**Source:** Maven Securities summary at `mavensecurities.com/alpha-decay-what-does-it-look-like-and-what-does-it-mean-for-systematic-traders/`

---

### 3.3 Momentum Half-Lives: Empirical Data Points

From aggregated practitioner research and microalphas.com signal decay analysis:

| Signal Type | Initial Monthly Alpha (bps) | Approximate Half-Life | Turns Negative |
|---|---|---|---|
| Cross-sectional momentum (J&T style) | 54 bps/month | ~5 months | Month 11–12 |
| Mean reversion (intraday) | Varies | Hours to 1 day | — |
| Mean reversion (swing) | Varies | 3–10 days | — |
| Value (Fama-French) | ~30–40 bps/month | ~12–24 months | Rarely in short window |
| Quality / profitability | ~20–30 bps/month | 18–36 months | Rarely |

**Turnover implication (Novy-Marx & Velikov):** Momentum requires ~426% annual turnover; this high turnover is the direct consequence of the short half-life requiring rapid execution.

---

### 3.4 Ma & Smith (2025): Multi-Period Optimization Under Alpha Decay + Transaction Costs

**Full citation:** Ma, C., & Smith, P. (2025). On the effect of alpha decay and transaction costs on the multi-period optimal trading strategy. *arXiv: 2502.04284*.

**Framework:** Infinite-horizon Markov Decision Process with:

1. Signal with exponential alpha decay (retained predictive power from past signals)
2. Proportional transaction costs discouraging frequent rebalancing

**Result:** Derives first-order approximation of the optimal policy with small transaction costs. The optimal strategy is *not* to trade immediately to the maximum alpha position — but to trade partially, balancing the marginal benefit of signal exploitation against the marginal cost of transaction friction and the option value of future signal updates.

**Key structural finding:** With alpha decay, the no-trade band is not symmetric — the urgency to act is higher when the signal is fresh (high $\alpha_0$) than when stale. The model formalizes the interaction between information half-life and trading friction.

---

### 3.5 Garleanu & Pedersen (2013): The Aim Portfolio

**Full citation:** Gârleanu, N., & Pedersen, L. H. (2013). Dynamic trading with predictable returns and transaction costs. *Journal of Finance*, 68(6), 2309–2340. DOI: 10.1111/jofi.12080

**Core result:** Closed-form optimal dynamic portfolio policy when trading is costly and returns are predictable by signals with different mean-reversion (alpha decay) speeds.

**Optimal portfolio update rule:**

$$x_{t+1} = x_t + \rho \cdot (\mathrm{aim}_t - x_t)$$

where the "aim portfolio" is:

$$\mathrm{aim}_t = \sum_j w_j \cdot \mathrm{Markowitz}(x_t^{(j)}, f_t^{(j)})$$

The weights $w_j$ are larger for signals with *slower* alpha decay (more persistent predictors get more weight in the aim because they will remain relevant for longer).

**Trading rate:** $\rho \in (0,1)$ — the fraction of the way from current to aim that is optimal to trade in one period. Optimal $\rho$ balances marginal gain from closing the gap vs. marginal transaction cost.

**"Aim in front of the target":** Because the Markowitz portfolio (the moving target) is predictable and will shift, the aim portfolio leads the current Markowitz portfolio — the trader should aim at where the target will be, not where it is now.

**Implication for inaction:** If $x_t = \mathrm{aim}_t$ (current portfolio equals aim), inaction is optimal. But if a signal moves, the aim shifts immediately while $x_t$ stays fixed — creating a gap where inaction has a cost proportional to $|\mathrm{aim}_t - x_t|^2$ per period (quadratic in distance from optimal). Complete inaction (never trading toward the aim) has a compounding cost that grows faster than linear in time.

---

### 3.6 Bouchaud, Gefen, Potters & Wyart (2004): Price Impact Propagator

**Full citation:** Bouchaud, J.-P., Gefen, Y., Potters, M., & Wyart, M. (2004). Fluctuations and response in financial markets: The subtle nature of "random" price changes. *Quantitative Finance*, 4(2), 176–190. DOI: 10.1080/14697680400000022. arXiv: cond-mat/0307332.

**Key finding:** Market orders are *long-range correlated* (persistence in order flow), which would cause super-diffusion. But limit orders provide mean-reverting pressure, keeping prices near diffusion. The balance is precise — markets are near a "critical point."

**The propagator model:** Price at time $t$ = cumulative impact of all past trades, each decaying via a non-constant propagator function $G(t - s)$. Empirically, $G(\ell) \sim \ell^{-\beta}$ with $\beta \approx 0.5$ (power-law decay, Paris Stock Exchange data).

**Implication for alpha decay:** The propagator measures how long a single trade's information content persists in price. The power-law form means impact (and therefore signal) does not decay to zero instantaneously but also does not persist indefinitely — there is a finite window where action on a signal has full value, and inaction beyond this window surrenders an increasing fraction of it.

---

### 3.7 Cont (2001): Stylized Facts as Signal Constraints

**Full citation:** Cont, R. (2001). Empirical properties of asset returns: Stylized facts and statistical issues. *Quantitative Finance*, 1(2), 223–236. DOI: 10.1080/713665670

**Relevant stylized fact:** Absence of significant autocorrelation in raw returns (at horizons beyond a few minutes). This means short-horizon alpha (from microstructure) decays faster than lower-frequency signals (from fundamentals). Any alpha-based trading strategy must account for the timescale at which the signal remains valid.

---

## 4. Reinforcement Learning for Portfolio Management

### 4.1 Jiang, Xu & Liang (2017): EIIE Framework

**Full citation:** Jiang, Z., Xu, D., & Liang, J. (2017). A deep reinforcement learning framework for the financial portfolio management problem. *arXiv: 1706.10059*.

**Architecture:** Ensemble of Identical Independent Evaluators (EIIE) + Portfolio-Vector Memory (PVM) + Online Stochastic Batch Learning (OSBL). Applied to 13 cryptocurrencies on Poloniex exchange, rebalancing every 30 minutes.

**Action space:** At each timestep, the agent outputs a weight vector $w \in \Delta^{n-1}$ (simplex). The "hold" action corresponds to outputting $w = w_{\mathrm{prev}}$ (unchanged weights). Transaction costs penalize deviation: $r_t = \mu_t (w_t \cdot p_t) - \text{cost}(|w_t - w_{t-1}|)$.

**Inaction handling:** The portfolio vector memory explicitly stores $w_{t-1}$, making inaction (outputting identical weights) a first-class policy option. The agent learns when marginal return from rebalancing exceeds transaction cost penalty. This is an RL-derived no-trade zone.

---

### 4.2 RL Action Space Structure and Hold-Bias Risk

**Survey reference:** Hambly, B., Xu, R., & Yang, H. (2024). The evolution of reinforcement learning in quantitative finance: A survey. *arXiv: 2408.10932*.

**Discrete action RL (DQN, etc.):** Standard setup: $A_t \in \{\text{Buy}, \text{Sell}, \text{Hold}\}$ or $A_t \in \{-1, 0, 1\}$. The hold action (0) is distinct from buy/sell.

**Transaction cost interaction:** The reward function typically includes $-\delta |A_t - A_{t-1}|$ penalizing changes. This creates an *intrinsic bias toward the hold action* — the RL agent is penalized for every state transition, making inaction economically cheaper per step. In volatile markets this is appropriate, but it can produce systematic under-trading if the penalty coefficient $\delta$ is miscalibrated.

**DQN overestimation bias:** DQN overestimates Q-values in volatile environments, especially for rarely-seen states. The hold action Q-value may be systematically overestimated because hold states are more frequent in the replay buffer — creating a data-driven hold bias. PPO (Proximal Policy Optimization) and continuous-action policy gradient methods reduce this by treating position sizing as a continuous variable.

**2026 frontier — behavioral RL:** Nature Scientific Reports (2026) paper on loss-aversion-embedded RL: explicitly incorporates Kahneman-Tversky loss aversion into the reward function, showing that agents with appropriate behavioral activation mechanisms better represent realistic trading psychology. However, the goal is to *debias* these tendencies from the policy, not amplify them.

---

### 4.3 Multi-Agent RL and Market-Wide Inaction Dynamics

**Key paper:** Casgrain, P., & Jaimungal, S. (2022). Multi-agent reinforcement learning in a realistic limit order book market simulation. *(Referenced in survey above.)*

**Key insight for inaction:** In multi-agent settings where multiple strategies share similar signals, simultaneous inaction by all agents (no one trades on the signal) can leave alpha on the table that a single deviating agent could capture. This creates a game-theoretic tension: individually, inaction reduces impact costs; collectively, simultaneous inaction prevents price discovery and signals persist longer than they otherwise would.

---

## 5. Risk Management and the Cost of Not Hedging

### 5.1 Delta Hedging: Dynamic Inaction Costs

**Standard reference:** Hull, J. C. *Options, Futures, and Other Derivatives* (any edition). Chapter on delta hedging.

**The fundamental cost of inaction under delta hedging:**

For a long call position with delta $\Delta_t$, a delta-neutral portfolio requires short $\Delta_t$ shares. If the stock price increases from $S$ to $S + \delta S$:

* New theoretical delta: $\Delta_{t+1} = \Delta_t + \Gamma \cdot \delta S$ (gamma effect)
* Under-hedged quantity: $\Gamma \cdot \delta S$ shares
* Cost of not re-hedging: $\frac{1}{2}\Gamma \cdot (\delta S)^2$ per unit (gamma P&L)

**Continuous re-hedging:** The Black-Scholes model assumes continuous hedging. Every discrete interval without re-hedging accumulates gamma risk proportional to $\Gamma \cdot (\delta S)^2 / 2$. For high-gamma positions (near-the-money, near-expiry), inaction is maximally costly.

---

### 5.2 AQR on Tail Risk Hedging: The Inaction-Cost Paradox

**Full citation:** Israelov, R., & Nielsen, L. (AQR). Chasing your own tail (risk). AQR White Paper. URL: `aqr.com/-/media/AQR/Documents/Insights/White-Papers/AQR-Chasing-Your-Own-Tail-Risk.pdf`

**Key finding:** Purchasing put options for tail hedging (action) has a long-run expected return that is *negative* — the insurance premium consistently exceeds payouts. Yet not purchasing (inaction) leaves the portfolio exposed to left-tail events.

**The quantitative tradeoff:** In normal environments (95%+ of time), tail hedging costs money and creates tracking error vs. unhedged benchmark. In crisis (5%- of time), the hedge pays off. The rational answer depends on the shape of the loss distribution and the investor's CVaR tolerance.

**Asymmetry:** Action (buying hedge) has definite negative carry in normal times. Inaction (no hedge) has positive carry in normal times but catastrophic exposure in tails.

**AQR's conclusion:** Dynamic risk management (reducing exposures before tail events) is preferable to static option-buying, but involves the cost of false positives (reducing exposure when crisis doesn't materialize). The cost of premature de-risking (inaction after the move) compounds.

---

### 5.3 Regime-Switching Models: Cost of Not Adapting

**Hamilton (1989) foundation:** Hamilton, J. D. (1989). A new approach to the economic analysis of nonstationary time series and the business cycle. *Econometrica*, 57(2), 357–384.

**Portfolio extension (key papers):**

* Ang, A., & Bekaert, G. (2002). Regime changes and financial markets. *Review of Financial Studies*, 15, 1137–1187.
* Nystrup, P., et al. (2017). Dynamic portfolio optimization across hidden market regimes. *Quantitative Finance*, 17(1), 83–95.

**Cost of not adapting to regime change:** In a two-regime model (risk-on / risk-off), the optimal equity allocation shifts substantially between regimes (e.g., 70% equity in expansion vs. 30% in contraction). Failing to adapt when a regime shift occurs (inaction) leaves the portfolio with the wrong allocation.

**Quantitative estimate:** Nystrup et al. (2017) find that regime-aware dynamic allocation generates roughly 1–3% annual Sharpe improvement over static allocation, depending on regime identification speed.

**Portfolio inertia interaction:** Regime-based rebalancing frameworks explicitly address the cost of *late* action — identifying the regime shift correctly but delaying the allocation change to reduce false positives. The Bulla et al. median-filtering approach and Nystrup's 95%-confidence threshold both represent formal inaction policies with computed costs.

---

## 6. Momentum, Mean Reversion, and the Timing of Action

### 6.1 Jegadeesh & Titman (1993): Systematic Profit from Acting When Others Hold

**Full citation:** Jegadeesh, N., & Titman, S. (1993). Returns to buying winners and selling losers: Implications for stock market efficiency. *Journal of Finance*, 48(1), 65–91. DOI: 10.2307/2328882

**Core result:** Long-short strategy (buy prior-12-month winners, sell prior-12-month losers) generates ~**1.5% monthly** abnormal returns (18% annualized) across 1965–1989. Effect survives beta adjustment; not explained by Fama-French three factors at the time.

**The inaction-as-action angle:** Momentum profits exist precisely because the majority of investors fail to act on persistent winner/loser patterns — they hold their losers (omission bias, disposition effect) and sell their winners too early. The momentum trader profits by acting systematically where others sit still.

**30 years later:** Jegadeesh, N., & Titman, S. (2023). Momentum: Evidence and insights 30 years later. *Pacific-Basin Finance Journal*, (available SSRN 4602426). Key finding: momentum remains robust across asset classes and globally. The behavioral explanation (initial under-reaction followed by delayed over-reaction) persists.

---

### 6.2 Moskowitz, Ooi & Pedersen (2012): Time-Series Momentum

**Full citation:** Moskowitz, T. J., Ooi, Y. H., & Pedersen, L. H. (2012). Time series momentum. *Journal of Financial Economics*, 104(2), 228–250. DOI: 10.1016/j.jfinec.2011.11.003

**Core result:** Past 12-month return of an asset predicts its next-month return with a positive sign across all major asset classes (equity indices, currencies, commodities, government bonds) in 58 instruments, 1985–2009. A strategy that buys assets with positive trailing-12-month returns and sells those with negative trailing returns earns significant risk-adjusted returns.

**Direct anti-inertia implication:** TSMOM is mathematically the precise anti-thesis of inaction: the optimal policy is to continuously act in the direction of the trend. An investor who holds a downtrending position (inertia) is systematically on the wrong side of TSMOM profits.

**Persistence:** Returns persist for ~12 months before partially reversing over longer horizons — consistent with behavioral under-reaction (failure to act promptly on trend information).

**Data availability:** AQR makes the original factor data publicly available at `aqr.com/Insights/Datasets/Time-Series-Momentum-Original-Paper-Data`.

---

### 6.3 Interaction: Omission Bias as the Supply of Momentum Alpha

**Synthesis (not a single paper):** The behavioral mechanism supplying momentum alpha is the market's systematic reluctance to act — specifically:

* **Disposition effect** (Odean 1998): Investors hold losers and sell winners, creating continued underperformance of losers and continued outperformance of winners.
* **Delayed reaction** (Hong & Stein 1999 model): Gradual information diffusion when some investors fail to act on public information.
* **Herding and anchoring:** Analysts revise forecasts slowly (updating only partially on new information).

These frictions are the *source* of momentum alpha. The quant trader who acts promptly and systematically harvests the alpha left by behaviorally-biased investors who do not act.

---

## 7. Quant Practitioner Perspectives

### 7.1 Ed Thorp: Kelly Criterion and the Cost of Under-Betting

**Key paper:** Thorp, E. O. (2007). The Kelly criterion in blackjack, sports betting, and the stock market. In MacLean, Thorp, & Ziemba, *The Kelly Capital Growth Investment Criterion*. World Scientific. Available at: `web.williams.edu/Mathematics/sjmiller/public_html/341/handouts/Thorpe_KellyCriterion2007.pdf`

**Kelly formula:**

$$f^* = \frac{bp - q}{b} = \frac{\text{edge}}{\text{odds}}$$

where $p$ = probability of win, $q = 1-p$, $b$ = odds ratio. For continuous returns: $f^* = \mu/\sigma^2$ (mean return over variance).

**The asymmetry of under-betting vs. over-betting:**

* Betting $f^*/2$ (half-Kelly): Growth rate is ~75% of full-Kelly growth rate — a 25% reduction.
* Betting $2f^*$ (double-Kelly): **Growth rate = 0** (zero long-run compounding).
* Betting $> 2f^*$: Negative long-run growth (eventual ruin).

**The cost of inaction = cost of betting 0:** Growth rate = 0 always, regardless of edge. The opportunity cost of not betting when you have a positive-EV edge is the full Kelly growth rate forgone: $g^* = \mu - \sigma^2/2$ (continuous time, log-optimal portfolio).

**Thorp's philosophy:** Complete inaction (not sizing up when edge is known) is as irrational as overbetting. Both produce suboptimal geometric growth. Thorp's recommendation of half-Kelly acknowledges *uncertainty about edge* — but not inaction as a default.

---

### 7.2 Jim Simons / Renaissance Technologies: Institutional Anti-Inaction

**Source:** Multiple practitioner accounts; Zuckerman, G. (2019). *The Man Who Solved the Market*. Portfolio/Penguin.

**Key statistics:**

* Medallion Fund: Average annual return ~66% gross (1988–2018), 39% net of fees.
* Daily trading volume: 150,000–300,000 trades per day (fully automated).
* Holding period: Seconds to days (predominantly).
* 2008 return: +98% while most funds lost substantially.

**Philosophy on inaction:** Renaissance's approach is the structural negation of inaction-as-default. The entire firm is built on the premise that every statistically identified edge must be acted upon immediately, at optimal size, without discretionary override. The Medallion Fund's construction assumes near-zero tolerance for letting identified alpha decay untraded.

**Operational mechanism:** Algorithms execute autonomously; human discretion is excluded from real-time trading decisions. This is institutional debiasing of omission bias at scale — the system is *designed* to prevent the human default of not acting.

---

### 7.3 AQR / Cliff Asness: Systematic Rebalancing Discipline

**Key reference:** AQR Alternative Thinking Q3 2017: "Systematic versus Discretionary". URL: `aqr.com/-/media/AQR/Documents/Insights/Alternative-Thinking/AQR-Alternative-Thinking--3Q17.pdf`

**Also:** Asness, C. S., Moskowitz, T. J., & Pedersen, L. H. (2013). Value and momentum everywhere. *Journal of Finance*, 68(3), 929–985.

**Asness on rebalancing:** AQR employs high-conviction systematic processes precisely to prevent the discretionary override that produces inertia. The key insight is that systematic investing does require judgment — but that judgment is applied to *strategy design*, not to second-guessing individual signals.

**Momentum + transaction costs:** Asness acknowledges momentum's higher turnover creates real costs, but argues the premium survives at institutional scale when costs are managed via smart execution (limit orders, patient execution, buy/hold spreads).

**"You can have your momentum factor and eat it too":** AQR white paper arguing that net-of-cost momentum returns remain substantial even accounting for realistic implementation costs — implying the cost of *not* implementing momentum (inaction on the signal) is the forfeited premium.

---

### 7.4 Marcos López de Prado: Advances in Financial Machine Learning

**Full citation:** López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley.

**Relevant frameworks:**

1. **Triple-barrier labeling:** Labels each observation as "buy," "sell," or "hold (time expires)" — explicitly making the hold action a labeled training outcome, not an absence of signal.

2. **Hierarchical Risk Parity (HRP):** Alternative to mean-variance optimization that is numerically stable and does not require matrix inversion. HRP explicitly treats the *timing* of rebalancing as a decision with costs.

3. **Meta-labeling:** Separates the "side" of a bet (long/short) from the "size" (how much). A meta-label of 0 represents not trading a primary signal. This formalizes inaction as a machine-learned decision, not a default.

4. **Feature importance for bet timing:** López de Prado emphasizes that knowing *when* to act is as important as knowing *what* direction to act. Signal freshness and alpha decay are implicit in the feature importance framework.

**Core contribution to inaction-as-action thesis:** By making "hold" a labeled, machine-learned outcome (rather than an absence of prediction), ML-based approaches like López de Prado's formally treat inaction as a first-class decision requiring justification, not a fallback.

---

### 7.5 Frazzini, Israel & Moskowitz: Real Implementation Demonstrates Feasibility

**Core message for practitioners:** The $1.7T trade execution dataset demonstrates that:

1. Real institutional transaction costs are far lower than academic models assumed (often by 5–10×).
2. Value, size, and momentum all survive at large AUM when implemented with smart execution.
3. The primary source of strategy death is *not* transaction costs on executed trades — it is failure to trade (leaving alpha on the table due to over-cautious execution thresholds).

---

## 8. Unified Framework: When Is Inaction Rational?

Synthesizing the above quantitative literature, inaction is **strictly rational** only under these conditions:

| Condition | Formal Model | Reference |
|---|---|---|
| Portfolio is within the no-trade band | Davis-Norman NT zone: $(y,z) \in \mathrm{NT}$ | Davis & Norman (1990) |
| Signal strength $< $ transaction cost | IS break-even: $\alpha_0 < 2\lambda$ | Almgren-Chriss; Kissell-Glantz |
| Optimization error $>$ expected gain | Estimation window $< 3000$ months for 25 assets | DeMiguel et al. (2009) |
| Tail hedge carry cost $>$ CVaR reduction | AQR tail hedge framework | Israelov & Nielsen |
| RL Q(hold) genuinely $>$ Q(buy)/Q(sell) | After correct calibration of transaction penalty $\delta$ | Jiang et al. (2017) |

**Inaction is irrational (has quantifiable cost) when:**

* Position is outside the Davis-Norman band
* Signal strength $> $ transaction cost (Almgren-Chriss break-even)
* Alpha has not yet decayed significantly (still within the information half-life: $t < t_{1/2}$)
* Portfolio is overexposed to a regime that has shifted (Hamilton regime-switch cost)
* Kelly fraction $f^* > 0$ and current bet is 0 (full Kelly growth rate forfeited)
* Momentum signal is active and position is not aligned with it (TSMOM cost)

**The inaction cost function (unified approximation):**

$$C(\text{inaction}, \Delta t) \approx \underbrace{\alpha_0(1 - e^{-\lambda \Delta t})}_{\text{alpha decay cost}} + \underbrace{\frac{1}{2}\Gamma \cdot \sigma^2 \cdot \Delta t}_{\text{options gamma cost}} + \underbrace{\rho |\mathrm{aim}_t - x_t|^2 \cdot \Delta t}_{\text{Garleanu-Pedersen drift cost}} + \underbrace{g^*(f^*) \cdot \Delta t}_{\text{Kelly growth forgone}}$$

Each term corresponds to a distinct channel through which delay costs accumulate.

---

## 9. Cross-Reference Map

* **Behavioral mechanisms** causing irrational inaction: [`omission-status-quo-inaction-inertia-trading.md`](omission-status-quo-inaction-inertia-trading.md)
* **Opportunity cost neglect** as the cognitive failure: [`opportunity-cost-neglect-in-trading.md`](opportunity-cost-neglect-in-trading.md)
* **Symmetric action-inaction evaluator** (debiasing tool): [`../debiasing-frameworks/symmetric-action-inaction-evaluator.md`](../debiasing-frameworks/symmetric-action-inaction-evaluator.md)
* **Multi-denomination framework** (inaction across denomination frames): [`multi-denomination-portfolio-valuation.md`](multi-denomination-portfolio-valuation.md)
* **Stoic framework** (philosophical grounding for treating inaction as choice): [`stoic-inaction-as-action-framework.md`](stoic-inaction-as-action-framework.md)
* **Behavioral biases synthesis**: [`behavioral-biases-multi-paper-synthesis.md`](behavioral-biases-multi-paper-synthesis.md)

---

## 10. Bibliography (All Papers Cited)

1. Almgren, R., & Chriss, N. (2000). Optimal execution of portfolio transactions. *Journal of Risk*, 3, 5–39.
2. Bouchaud, J.-P., Gefen, Y., Potters, M., & Wyart, M. (2004). Fluctuations and response in financial markets. *Quantitative Finance*, 4(2), 176–190. DOI: 10.1080/14697680400000022.
3. Casgrain, P., & Jaimungal, S. (2022). Multi-agent reinforcement learning in realistic limit order book simulation. *(SSRN).*
4. Cont, R. (2001). Empirical properties of asset returns: Stylized facts and statistical issues. *Quantitative Finance*, 1(2), 223–236. DOI: 10.1080/713665670.
5. Davis, M. H. A., & Norman, A. R. (1990). Portfolio selection with transaction costs. *Mathematics of Operations Research*, 15(4), 676–713. DOI: 10.1287/moor.15.4.676.
6. DeMiguel, V., Garlappi, L., & Uppal, R. (2009). Optimal versus naive diversification. *Review of Financial Studies*, 22(5), 1915–1953. DOI: 10.1093/rfs/hhm075.
7. Di Mascio, R., Lines, A., & Naik, N. Y. (2015). Alpha decay. *SSRN 2580551*.
8. Frazzini, A., Israel, R., & Moskowitz, T. J. (2015). Trading costs of asset pricing anomalies. *AQR Working Paper*.
9. Frazzini, A., Israel, R., & Moskowitz, T. J. (2018). Trading costs. *SSRN 3229719*.
10. Gârleanu, N., & Pedersen, L. H. (2013). Dynamic trading with predictable returns and transaction costs. *Journal of Finance*, 68(6), 2309–2340. DOI: 10.1111/jofi.12080.
11. Hamilton, J. D. (1989). A new approach to the economic analysis of nonstationary time series and the business cycle. *Econometrica*, 57(2), 357–384.
12. Jegadeesh, N., & Titman, S. (1993). Returns to buying winners and selling losers. *Journal of Finance*, 48(1), 65–91. DOI: 10.2307/2328882.
13. Jegadeesh, N., & Titman, S. (2023). Momentum: Evidence and insights 30 years later. *SSRN 4602426*.
14. Jiang, Z., Xu, D., & Liang, J. (2017). A deep reinforcement learning framework for the financial portfolio management problem. *arXiv: 1706.10059*.
15. Kissell, R., & Glantz, M. (2003). *Optimal Trading Strategies: Quantitative Approaches for Managing Market Impact and Trading Risk*. AMACOM.
16. Leland, H. E. (1996). Optimal asset rebalancing in the presence of transactions. *SSRN 1060*.
17. López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley.
18. Ma, C., & Smith, P. (2025). On the effect of alpha decay and transaction costs on the multi-period optimal trading strategy. *arXiv: 2502.04284*.
19. Moskowitz, T. J., Ooi, Y. H., & Pedersen, L. H. (2012). Time series momentum. *Journal of Financial Economics*, 104(2), 228–250. DOI: 10.1016/j.jfinec.2011.11.003.
20. Novy-Marx, R., & Velikov, M. (2016). A taxonomy of anomalies and their trading costs. *Review of Financial Studies*, 29(1), 104–147. DOI: 10.1093/rfs/hhv063.
21. Perold, A. F. (1988). The implementation shortfall: Paper versus reality. *Journal of Portfolio Management*, 14(3), 4–9.
22. Thorp, E. O. (2007). The Kelly criterion in blackjack, sports betting, and the stock market. In *The Kelly Capital Growth Investment Criterion*. World Scientific.
23. Vanguard Research. (2024). The rebalancing edge. *Vanguard Institutional Research*.
24. Zuckerman, G. (2019). *The Man Who Solved the Market*. Portfolio/Penguin.

---

*This document is part of the Rational Trading & Behavioral Finance KB. For the companion behavioral-psychology perspective on inaction, see [`omission-status-quo-inaction-inertia-trading.md`](omission-status-quo-inaction-inertia-trading.md). For the debiasing implementation, see [`../debiasing-frameworks/symmetric-action-inaction-evaluator.md`](../debiasing-frameworks/symmetric-action-inaction-evaluator.md).*
