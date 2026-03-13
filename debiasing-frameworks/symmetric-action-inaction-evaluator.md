# Symmetric Action-Inaction Evaluator: N-Dimensional Decision Framework

[Collected 2026-03-13 | Claude Opus 4.6 synthesis from multi-agent research]

---

## Abstract

Standard portfolio decision-making privileges inaction ("hold") as a costless default. This framework treats every feasible action — including "do nothing" — as a first-class decision with its own probability distribution over outcomes, evaluated simultaneously across N denomination/value dimensions. The key insight: **you cannot afford to not-trade without the same scrutiny you'd apply to trading**. Inaction has costs (opportunity cost, option value decay, drift from optimal allocation); action has costs (transaction fees, destroyed optionality, adverse selection). Both must be priced symmetrically.

---

## 1. Core Formulation

### 1.1 The Unified Decision Problem

At time t, the agent faces action set A = {buy₁, buy₂, ..., sell₁, sell₂, ..., rebalance_to_target, **hold**}. For each action a ∈ A:

$$a^* = \arg\max_{a \in \mathcal{A}} \left[ \mathbb{E}_{P(\omega|a,\mathcal{F}_t)}\left[ U\left( \mathbf{V}_{t+h}(\omega) \right) \right] - C(a) \right]$$

where:

* **V_{t+h}(ω) ∈ ℝ^k** — multi-denomination portfolio value vector (USD, BTC, CPI-adjusted, risk-adjusted, etc.)
* **P(ω | a, F_t)** — action-conditional outcome distribution given current information
* **U: ℝ^k → ℝ** — multi-attribute utility function
* **C(a)** — total cost of action a:
  * For a ≠ hold: C(a) = transaction_cost + tax_impact + destroyed_option_value
  * For a = hold: C(hold) = opportunity_cost + drift_from_optimal + option_value_decay

**Critical property**: C(hold) ≠ 0. The framework makes this visible.

### 1.2 Multi-Denomination Value Vector

Following the [denomination-invariant evaluation framework](denomination-invariant-evaluation.md), portfolio value is always a vector, never a scalar:

```
V(t) = [V_USD(t), V_BTC(t), V_gold(t), V_CPI(t), V_risk_adj(t), ...]
```

Growth across dimensions:

```
G_d(t₀, t₁) = V_d(t₁) / V_d(t₀)  for each denomination d
```

**Min-growth metric** (from denomination-invariant framework):

```
G(t₀, t₁) = min_d { G_d(t₀, t₁) }
```

If G > 1, growth is genuine across all frames. An action is only unambiguously good if it improves the min-growth metric.

### 1.3 Why "Hold" Is Never Free

Under the Bellman optimality equation for MDP formulation:

$$V^*(s) = \max_{a \in \mathcal{A}} \left[ r(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s') \right]$$

"Hold" is a first-class action with its own reward r(s, hold). This reward is:

* **Positive** if portfolio appreciates while idle and no better alternative exists
* **Negative** if better alternatives exist (opportunity cost) or portfolio drifts from optimal (drift cost)
* **Never zero** unless the portfolio is exactly at the optimal allocation with no alternatives

The Merton (1971) continuous-time solution gives the optimal fraction as:

```
w* = (μ - r_f) / (γ σ²)
```

Any deviation from w* — including the deviation caused by not rebalancing — is a measurable, priced decision.

---

## 2. Three Symmetric Cost Functions

### 2.1 Cost of Acting (Well-Understood)

```
C_act(a) = spread + commission + market_impact + tax_realization + Ω_destroyed
```

where Ω_destroyed is the real option value destroyed by committing (Dixit & Pindyck 1994). For irreversible investments:

```
V*_trigger = (β / (β-1)) · I
```

where β > 1 depends on volatility. Higher volatility → higher trigger → more optionality destroyed per action. This is why the "option to wait" has value.

### 2.2 Cost of Not Acting (Systematically Neglected)

```
C_hold = OC_best_alternative + drift_cost + option_decay + information_decay
```

Components:

* **OC_best_alternative**: Kelly growth rate foregone = G(f*) - G(f_actual), where f* is Kelly-optimal and f_actual is current allocation. When f_actual = 0 for a positive-edge opportunity, this is strictly positive.
* **drift_cost**: For a target allocation w*, unrebalanced portfolio drifts at rate proportional to return dispersion. Empirically: 60/40 → 80/20 in a bull decade → outsized drawdown risk.
* **option_decay**: Time-sensitive opportunities (earnings announcements, liquidity windows) have decaying option value. Delay = value destruction.
* **information_decay**: Edge from research decays as information propagates. ΔG/Δt < 0 for most informational advantages.

### 2.3 The Symmetry Principle

**For rational evaluation, every decision gate must compute BOTH costs:**

| Decision Point | Action Cost | Inaction Cost |
|---|---|---|
| Entry opportunity | Spread + impact + optionality destroyed | Foregone Kelly growth + missed alpha |
| Exit signal | Tax realization + re-entry risk | Continued loss + alternative OC |
| Rebalancing trigger | Transaction costs | Drift from optimal + concentration risk |
| Position sizing | Capital committed + leverage cost | Under-sizing = foregone geometric growth |

---

## 3. The Reversal Test (Bostrom & Ord 2006)

The most powerful single-question debiasing heuristic for inaction bias:

### For Held Positions

> "If I did not own this position today, would I buy it at the current price, size, and risk parameters?"

* **Yes** → holding is justified
* **No** → holding is status quo bias; exit (adjusted for transaction costs)
* **Uncertain** → requires the same investigation as a new position entry

### For Avoided Actions

> "If I had already taken this action and needed to decide whether to reverse it, would I reverse it?"

* **No** → the action is probably justified; avoiding it is omission bias
* **Yes** → genuine reasons against action exist

### For Sizing

> "If this were a fresh allocation with no existing position, what size would I choose?"

* If answer ≠ current size: current size reflects anchoring to entry, not current fundamentals

---

## 4. Minimax Regret Across N Dimensions

The minimax regret framework bounds worst-case decision quality symmetrically for action and inaction.

**Regret of action a given realized scenario s:**

```
R(a, s) = V*(s) - V(a, s)
```

where V*(s) = max_{a'} V(a', s) is the best achievable value in hindsight.

**Minimax regret portfolio:**

```
w_MMR = argmin_w max_s R(w, s)
```

For multi-denomination evaluation, regret is computed per-denomination and aggregated:

```
R_total(a, s) = max_d { R_d(a, s) }   (worst-denomination regret)
```

The "hold" action explicitly participates in the minimax:

```
R(hold, s) = V*(s) - V(hold, s)
```

This can be very large when the optimal action was to exit a crashing position or enter a surging opportunity.

Key papers:

* Xidonas, Mavrotas, Hassapis & Zopounidis (2017). "Robust Multiobjective Portfolio Optimization: A Minimax Regret Approach." *European J. Operational Research* 262(1):299–305. DOI: [10.1016/j.ejor.2017.03.041](https://doi.org/10.1016/j.ejor.2017.03.041)
* Perez Gladish et al. (2022). "A Minimax Regret Portfolio Model Based on the Investor's Utility Loss." *Operational Research* 22(1):1–26. DOI: [10.1007/s12351-020-00550-0](https://doi.org/10.1007/s12351-020-00550-0)

---

## 5. Kelly Criterion: Inaction Is Priced

Under Kelly, optimal fraction f* = (bp - q) / b.

**Cost of inaction when Kelly prescribes positive f*:**

```
ΔG = G(f*) - G(0)
```

This is strictly positive and computable. "Not betting" when Kelly says bet is a decision with measurable expected wealth loss.

**Multi-asset Kelly** (Merton fraction approximation):

```
f* ≈ Σ⁻¹(μ - r_f · 1)
```

Kelly prescribes f = 0 (cash) only when Σ⁻¹μ ≤ r_f — when no asset has positive edge after correlation adjustment.

**Bayesian Kelly** (Browne & Whitt 1996): Under parameter uncertainty, drift μ has prior distribution π(μ). The posterior-mean optimal strategy shrinks f* toward zero — uncertainty about edge rationally reduces position size but still prices inaction when posterior edge is positive.

---

## 6. Real Options: Can You Afford to Act?

The other side: every irreversible action destroys option value.

**Investment threshold** (Dixit & Pindyck 1994):

```
Invest iff V ≥ V*_trigger = (β/(β-1)) · I > I
```

where:

* I = investment cost
* β = f(α, σ, ρ) > 1, increasing in volatility σ
* V*_trigger > I always (the option to wait has positive value)

**Trading translation**: The true entry threshold is NOT "positive expected value." It is "expected value > option value of waiting." This provides a **rational basis for deliberate non-entry** that is distinct from omission bias. The framework thus avoids the trap of treating all inaction as irrational.

**The asymmetry resolved**: Strategic non-action (wu wei / via negativa / option preservation) is justified when option value > immediate expected value. Pathological inaction (omission bias / thumb-sucking) is when expected value > option value but the agent still does not act due to psychological costs of commission.

---

## 7. Practical Implementation

### 7.1 Symmetric Decision Gate Checklist

For every portfolio decision (including the decision to hold unchanged):

```
SYMMETRIC DECISION EVALUATION
Date: [YYYY-MM-DD]
Position: [ticker/asset or "HOLD ALL"]

=== ACTION ANALYSIS ===
Proposed action: [buy/sell/rebalance/hold]
Expected outcome (N dimensions):
  USD return: [%]
  BTC return: [%]
  CPI-adjusted return: [%]
  Risk-adjusted (Sharpe): [ratio]
Action cost: [spread + commission + tax + destroyed optionality]

=== INACTION ANALYSIS ===
Cost of NOT acting:
  Kelly growth foregone: [ΔG = G(f*) - G(f_actual)]
  Best alternative OC: [expected alpha of next-best idea]
  Drift from target: [% deviation from optimal allocation]
  Information decay: [edge half-life estimate]

=== REVERSAL TEST ===
"Would I initiate this position today at current price/size?" [Y/N]
"If I had NOT acted, and outcome was bad, what mechanism?" [describe]
"If I HAD acted, and outcome was bad, what mechanism?" [describe]

=== BIAS AUDIT ===
[ ] Omission bias: Am I favoring inaction because it feels safer?
[ ] Status quo bias: Am I anchored to current allocation?
[ ] Inaction inertia: Did I miss a prior entry and now avoiding?
[ ] Action bias: Am I trading to feel productive?
[ ] Sunk cost: Is entry price influencing this decision?

=== DECISION ===
Optimal action: [chosen action with justification]
Min-growth metric impact: G = min_d{growth_d} = [value]
```

### 7.2 Automated Position Review System

```python
# Pseudocode: N-dimensional symmetric action evaluator
def evaluate_all_actions(portfolio_state, market_data, denominators):
    actions = generate_action_set(portfolio_state)  # includes 'hold'

    results = {}
    for a in actions:
        # Monte Carlo: P(outcomes | action)
        outcomes = simulate(portfolio_state, action=a, n=10000)

        # Multi-denomination value vector
        V = {d: value_in(outcomes, d) for d in denominators}

        # Kelly growth rate per denomination
        G = {d: np.mean(np.log(1 + returns_d)) for d in denominators}

        # Min-growth (denomination-invariant)
        min_G = min(G.values())

        # Transaction + option cost
        cost = transaction_cost(a) + option_value_destroyed(a, volatility)

        # Regret vs best counterfactual (per denomination)
        # Computed after all actions evaluated

        results[a] = {
            'V': V, 'G': G, 'min_G': min_G,
            'cost': cost,
            'net_EU': multi_attribute_utility(V, weights) - cost
        }

    # Compute minimax regret
    for a in actions:
        results[a]['max_regret'] = max(
            results[best_action]['V'][d] - results[a]['V'][d]
            for d in denominators
            for best_action in actions
        )

    # Optimal = max net EU (or min max regret)
    optimal = max(results, key=lambda a: results[a]['net_EU'])

    # Flag if 'hold' is suboptimal
    if optimal != 'hold':
        alert(f"INACTION COST: {results['hold']['net_EU'] - results[optimal]['net_EU']:.2%}")

    return optimal, results
```

---

## 8. Integration with Existing Frameworks

### 8.1 Connection to Denomination-Invariant Evaluation

The [denomination-invariant framework](denomination-invariant-evaluation.md) already forces multi-dimensional portfolio assessment. This framework extends it by:

* Making "hold" an explicit action evaluated in the same N dimensions
* Adding opportunity cost computation per denomination
* Incorporating real option value and Kelly growth into the evaluation

### 8.2 Connection to Stoic Decision Protocol

The [Stoic inaction-as-action framework](../core-research/stoic-inaction-as-action-framework.md) provides the philosophical foundation:

1. **Prohairesis** → every decision (including hold) is an exercise of rational will
2. **Kathêkon** → fiduciary duty to evaluate hold as rigorously as entry/exit
3. **Apatheia** → calm rational engagement, not passive withdrawal
4. **Reversal test** → operationalizes Bostrom & Ord (2006) as trading heuristic

### 8.3 Connection to Omission/Status Quo Debiasing

The [omission-status-quo-inaction-inertia analysis](../core-research/omission-status-quo-inaction-inertia-trading.md) provides the empirical evidence for why this framework is necessary:

* Omission bias: 72% prefer inaction (Ritov & Baron 1992)
* Status quo bias: WTA/WTP ≈ 2.25x (Kahneman, Knetsch & Thaler 1991)
* Inaction inertia: missed opportunities propagate to subsequent paralysis
* The "hypothetical cash reframe" is the single strongest debiasing intervention

---

## 9. Key References

### Decision Theory

* Von Neumann, J. & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton UP.
* Merton, R. (1971). "Optimum Consumption and Portfolio Rules in a Continuous-Time Model." *J. Economic Theory* 3(4):373–413. DOI: [10.1016/0022-0531(71)90038-X](https://doi.org/10.1016/0022-0531(71)90038-X)
* Loomes, G. & Sugden, R. (1982). "Regret Theory." *Economic Journal* 92(368):805–824.
* Bostrom, N. & Ord, T. (2006). "The Reversal Test." *Ethics* 116(4):656–679.

### Real Options & Optimal Stopping

* Dixit, A. & Pindyck, R. (1994). *Investment under Uncertainty*. Princeton UP. ISBN: 978-0-691-03410-2.
* McDonald, R. & Siegel, D. (1986). "The Value of Waiting to Invest." *QJE* 101(4):707–727.
* Peskir, G. & Shiryaev, A. (2006). *Optimal Stopping and Free-Boundary Problems*. Birkhäuser.

### Kelly Criterion & Information Theory

* Cover, T. (1991). "Universal Portfolios." *Mathematical Finance* 1(1):1–29. DOI: [10.1111/j.1467-9965.1991.tb00002.x](https://doi.org/10.1111/j.1467-9965.1991.tb00002.x)
* Browne, S. & Whitt, W. (1996). "Portfolio Choice and the Bayesian Kelly Criterion." *Advances in Applied Probability* 28(4):1145–1176.

### Multi-Objective Portfolio Optimization

* Xidonas, P. et al. (2017). "Robust Multiobjective Portfolio Optimization: A Minimax Regret Approach." *EJOR* 262(1):299–305.
* Atkinson, A. & Bourguignon, F. (1982). "The Comparison of Multi-Dimensioned Distributions." *Review of Economic Studies* 49(2):183–201.
* Jondeau, E. & Rockinger, M. (2006). "Optimal Portfolio Allocation under Higher Moments." *European Financial Management* 12(1):29–55.

---

*Cross-references: [Denomination-Invariant Evaluation](denomination-invariant-evaluation.md) | [Stoic Inaction Framework](../core-research/stoic-inaction-as-action-framework.md) | [Omission/Status Quo Analysis](../core-research/omission-status-quo-inaction-inertia-trading.md) | [Opportunity Cost Neglect](../core-research/opportunity-cost-neglect-in-trading.md) | [Multi-Denomination Valuation](../core-research/multi-denomination-portfolio-valuation.md)*
