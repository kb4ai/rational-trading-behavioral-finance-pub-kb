# Multi-Denomination Portfolio Valuation: A Framework for Denomination-Invariant Performance Assessment

> **A mathematical framework for eliminating denomination bias through simultaneous multi-asset projection of portfolio value**

[Collected 2026-03-07] [AI Provider: Anthropic, Claude Opus 4.6]

---

## 1. The Problem: Single-Denominator Bias

### 1.1 Denomination Anchoring

Every portfolio tracker, every brokerage statement, every mental calculation a trader performs begins with an implicit choice: **which asset to denominate in**. A crypto trader checks their "BTC stack." An equities investor watches their "dollar P&L." A gold bug measures purchasing power "in ounces." Each denomination choice is a frame — and frames distort perception.

This is not a minor bookkeeping detail. The denomination choice determines:

* Whether a portfolio appears to be growing or shrinking
* Which positions appear profitable and which appear underwater
* Whether the trader feels confident or anxious
* Which trades get executed (via the disposition effect's reference-point dependence)

A portfolio that gained 15% in USD terms may have *lost* 8% in BTC terms during a crypto bull run. The same portfolio, the same period, but two contradictory emotional narratives and potentially two contradictory trading decisions. The denomination frame is doing the work, not the underlying economics.

### 1.2 Three Pathological Patterns

**Denomination anchoring**: The trader selects a single denomination at account inception and never questions it. All subsequent P&L is evaluated in this denomination, creating a fixed reference frame that may diverge arbitrarily from the portfolio's actual multi-dimensional performance. This is a specific instance of anchoring (Tversky & Kahneman, 1974) applied to the numéraire rather than to a price level.

**Asset attachment via denomination**: By denominating in a specific asset, the trader implicitly treats that asset as the "real" unit of value. A BTC-denominating trader begins to view USD gains as irrelevant if their "sat stack" is shrinking — a form of mental accounting (Thaler, 1999) where the denomination label creates a privileged reference point. The denomination *becomes* the mental account.

**Selective denominator shopping**: The most insidious pattern. Traders unconsciously select whichever denomination makes their performance look best. "I'm up in USD!" (while down in gold). "My BTC stack is growing!" (while portfolio net worth in purchasing-power terms has declined). This is hedonic editing (Thaler, 1985) applied to the denomination choice itself — agents segregate favorable framings and suppress unfavorable ones.

### 1.3 Denomination Choice as Frame Selection

Tversky & Kahneman (1981) demonstrated that logically equivalent descriptions of the same decision problem can reverse preferences. The choice of denomination is precisely such a re-description: the portfolio's objective state is invariant, but the *narrative* changes with the denominator.

Choosing a denomination is choosing which branch of the prospect theory value function v(·) is activated. In denomination d₁, a position may sit in the gain domain (v concave, risk-averse); in denomination d₂, the same position sits in the loss domain (v convex, risk-seeking). The denomination frame can literally flip the trader's risk posture on the same underlying position.

### 1.4 Linguistic Markers

These utterances reveal active denomination bias:

| Statement | Denomination frame | What it conceals |
|-----------|-------------------|------------------|
| "I'm up in USD!" | USD-only view | May be down in gold, BTC, real purchasing power |
| "My BTC stack is growing" | BTC-only view | Portfolio may be losing total purchasing power |
| "Priced in gold, everything is falling" | Gold-only view | Nominal returns may be strongly positive |
| "I'm beating inflation" | CPI-adjusted USD | May be underperforming equities, commodities, crypto |
| "My portfolio doubled" | Implicit single denomination | Doubled relative to *what*? |

Each statement is formally incomplete: it reports V_d(t₁)/V_d(t₀) for exactly one d, while the portfolio exists in an N-dimensional denomination space.

---

## 2. Formal Framework: N-Dimensional Valuation

### 2.1 Setup and Notation

Let an agent hold a portfolio of assets at time t:

```
Portfolio P(t) = {(aᵢ, qᵢ) | i ∈ I}
```

Where aᵢ is an asset type and qᵢ is the quantity held. Let price_i(t) denote the market price of asset aᵢ at time t, expressed in some arbitrary base unit (which will cancel out). Let D = {d₁, d₂, ..., dₙ} be a set of **denomination assets** — assets in which we wish to express portfolio value.

### 2.2 Portfolio Value in Denomination d

The portfolio's total value projected into denomination d at time t:

```
V_d(t) = Σᵢ (qᵢ · price_i(t)) / price_d(t)
```

This gives the number of units of asset d that the portfolio could be exchanged for at prevailing market prices. When d = USD, this is the familiar "portfolio value in dollars." When d = BTC, it is the portfolio's value measured in bitcoin. When d = XAU (gold), it is the portfolio's value in troy ounces.

**Key observation**: V_d(t) is well-defined for any asset d with price_d(t) > 0. The portfolio's value is not a scalar — it is a **vector** indexed by the denomination set D.

### 2.3 The Valuation Vector

At any time t, the portfolio has a **valuation vector**:

```
V(t) = (V_d₁(t), V_d₂(t), ..., V_dₙ(t)) ∈ ℝⁿ₊
```

This vector is the complete, denomination-free description of the portfolio's value state. Any single-denomination view is a projection onto one coordinate axis — a lossy compression that discards (n-1) dimensions of information.

### 2.4 Growth Vector

Between times t₀ and t₁, the **per-denomination growth ratios** form a growth vector:

```
g(t₀, t₁) = (V_d₁(t₁)/V_d₁(t₀), V_d₂(t₁)/V_d₂(t₀), ..., V_dₙ(t₁)/V_dₙ(t₀)) ∈ ℝⁿ₊
```

Each component g_d = V_d(t₁)/V_d(t₀) is the portfolio's growth rate as measured in denomination d. A single-denomination trader sees only one component. The rational trader sees the full vector.

### 2.5 Denomination-Invariant Growth Metric

Define the **denomination-invariant growth metric**:

```
G(t₀, t₁) = min_{d ∈ D} { V_d(t₁) / V_d(t₀) }
```

This is the portfolio's growth in its *worst-performing denomination*. It is the most conservative, bias-resistant measure of portfolio performance available.

### 2.6 Denomination Sensitivity (Spread)

Define the **denomination spread**:

```
S(t₀, t₁) = max_{d ∈ D} { g_d } - min_{d ∈ D} { g_d }
```

The spread measures how much the portfolio's apparent performance depends on the denomination choice. A large spread signals that single-denomination reporting is highly misleading.

**Growth vector diagnostics**:

| Condition | Interpretation |
|-----------|---------------|
| S small, G > 1 | Robust growth — portfolio genuinely outperformed across all denominations |
| S large, G > 1 | Fragile growth — performance is denomination-sensitive; some denominations show strong gains, others barely positive |
| S small, G < 1 | Robust contraction — portfolio underperformed uniformly |
| S large, G < 1 | Mixed — portfolio is growing in some denominations, contracting in others; single-denomination reporting is maximally misleading |
| S ≈ 0 | Denomination-invariant performance — the denomination choice is irrelevant (rare in practice; occurs when portfolio is concentrated in a single asset) |

---

## 3. Properties of the Growth Metric G

### P1: Monotonicity

**Statement**: If V_d(t₁) > V_d(t₀) for all d ∈ D, then G(t₀, t₁) > 1.

**Proof**: G = min_d {V_d(t₁)/V_d(t₀)}. If every ratio exceeds 1, the minimum exceeds 1. ∎

**Interpretation**: If the portfolio grew in *every* denomination, G confirms genuine growth. This is the condition under which the trader can truthfully claim unambiguous positive performance.

### P2: Conservatism

**Statement**: G(t₀, t₁) ≤ V_d(t₁)/V_d(t₀) for every d ∈ D.

**Proof**: Immediate from the definition of minimum. ∎

**Interpretation**: G never overstates performance relative to any denomination. It is a lower bound on all single-denomination growth figures. Any trader claiming a growth rate above G is engaging in denomination cherry-picking.

### P3: Super-Multiplicativity

**Statement**: G(t₀, t₂) ≥ G(t₀, t₁) · G(t₁, t₂).

**Proof sketch**: Let d* be the denomination that achieves the minimum at (t₀, t₂), so G(t₀, t₂) = V_{d*}(t₂)/V_{d*}(t₀). Decompose:

```
V_{d*}(t₂)/V_{d*}(t₀) = [V_{d*}(t₁)/V_{d*}(t₀)] · [V_{d*}(t₂)/V_{d*}(t₁)]
```

Now, V_{d*}(t₁)/V_{d*}(t₀) ≥ min_d {V_d(t₁)/V_d(t₀)} = G(t₀, t₁), and similarly V_{d*}(t₂)/V_{d*}(t₁) ≥ G(t₁, t₂). Therefore:

```
G(t₀, t₂) = V_{d*}(t₂)/V_{d*}(t₀) ≥ G(t₀, t₁) · G(t₁, t₂)  ∎
```

**Interpretation**: G does not penalize for intermediate denomination switching. Compounding G across sub-periods gives a *lower bound* on the true end-to-end G. This means a trader who achieves G > 1 in every sub-period is guaranteed G > 1 over the full period — a consistency property that single-denomination metrics lack (where a trader "up in BTC" in Q1 and "up in USD" in Q2 may be down in both over the full year).

### P4: Boundary Behavior

**Statement**: G(t₀, t₁) = 1 if and only if the portfolio at least broke even in its worst denomination and lost ground in none.

More precisely: G = 1 ⟺ min_d {V_d(t₁)/V_d(t₀)} = 1, meaning the portfolio exactly maintained its value in its worst-performing denomination while potentially gaining in others.

### P5: Continuity

**Statement**: G(t₀, t) is continuous in t (assuming continuous price processes), but not everywhere differentiable.

**Explanation**: G is the minimum of finitely many continuous functions (the per-denomination growth ratios), so it is continuous. However, at points where the argmin switches — where a different denomination becomes the worst performer — the function has a kink (the minimum of smooth functions is piecewise smooth with corners at switch points).

**Interpretation**: The denomination that "constrains" the portfolio's invariant growth can change over time. These switch points are informative: they reveal when the portfolio's relative exposure to different denomination assets changes sign.

---

## 4. Connection to Existing Frameworks

### 4.1 W_total as Single-Denomination Special Case

The existing fungibility framework (see [fungibility-asset-transformation-rational-framework.md](fungibility-asset-transformation-rational-framework.md)) defines total wealth as:

```
W_total(t) = Σᵢ vᵢ(t) · qᵢ
```

where vᵢ(t) is the market value of asset i. If "market value" is denominated in USD, then W_total(t) ≡ V_USD(t). The entire fungibility framework is the **D = {USD} special case** of multi-denomination valuation.

**Proof**: Set D = {USD}. Then V_USD(t) = Σᵢ (qᵢ · price_i(t)) / price_USD(t). Since price_USD(t) = 1 by definition (one dollar costs one dollar), V_USD(t) = Σᵢ qᵢ · price_i(t) = W_total(t). ∎

This reveals that W_total implicitly carries a denomination label — "USD" — that is treated as though it were denomination-neutral. The multi-denomination framework makes this hidden assumption explicit and generalizes beyond it.

### 4.2 Multi-Denomination Fungibility Axiom

The fungibility axiom states: *for any rational optimization problem, only W_total(t) and the covariance/utility structure of the portfolio matters; the labels attached to sub-portfolios carry zero information content.*

We extend this: **the denomination label on W_total also carries zero information for rational optimization.** The choice to report W_total in USD rather than BTC or gold or a basket is itself a label — and labels, per the fungibility axiom, are informationally vacuous.

The partition welfare loss from mental accounting is:

```
L_partition = U*(W_total) - Σⱼ Uⱼ*(μ(Pⱼ))
```

We add a second loss term for denomination bias:

```
L_total = L_partition + L_denomination
```

where L_denomination captures the welfare loss from optimizing in a single denomination frame rather than across the full denomination vector. An agent who would hold a position in USD terms but sell it in BTC terms is making denomination-dependent decisions — a form of framing-induced inconsistency that destroys welfare exactly as mental accounting does.

### 4.3 Denomination as Frame Selection

De Martino et al. (2008) showed that framing a sure option as "keep £20" vs. "lose £30" (mathematically equivalent) changed gambling rates: 43.75% vs. 57.99% in controls. The framing manipulation activates different branches of the prospect theory value function v(·).

Denomination choice operates identically. For a portfolio position:

* In denomination d₁ (e.g., USD): entry price was $10,000, current price is $12,000 → **gain frame**, v(+$2,000) → risk-averse
* In denomination d₂ (e.g., BTC): entry price was 0.5 BTC, current price is 0.35 BTC → **loss frame**, v(-0.15 BTC) → risk-seeking

The same position, the same moment, but the denomination choice determines which branch of v(·) is activated. This is not merely analogous to the De Martino framing manipulation — it is structurally identical. The denomination label is the "keep" vs. "lose" wording of portfolio performance.

**Critical difference**: De Martino's framing manipulation was binary (gain/loss). Denomination framing is **continuous** — the trader can choose from an infinite space of denomination assets, each producing a different point on the v(·) function. This makes denomination framing a richer, more dangerous source of bias than binary gain/loss framing, because the agent has more degrees of freedom to hedonic-edit their perception.

### 4.4 Entry Price Denomination as Reference Point Anchor

In prospect theory, the reference point determines the gain/loss partition. In trading, the reference point is typically the entry price (Shefrin & Statman, 1985). But the entry price itself is denomination-dependent:

* Entry in USD: "I bought at $50,000" → reference point r_USD = 50,000
* Entry in BTC: "I bought at 1.2 BTC" → reference point r_BTC = 1.2
* Entry in gold: "I bought at 25 oz" → reference point r_XAU = 25

Each denomination creates a different reference point for the same position. Loss aversion λ ≈ 2.25 (Tversky & Kahneman, 1992) is activated only in denominations where current value falls below the entry reference. The agent holds a **menu of reference points** indexed by denomination, and the denomination they attend to determines whether loss aversion fires.

Formally, the hedonic value of holding a position at time t is:

```
H(t) = v(V_d(t) - r_d)     where d is the attended denomination
```

If V_d(t) > r_d: gain domain, v concave, moderate positive hedonic signal.
If V_d(t) < r_d: loss domain, v convex, λ-amplified negative hedonic signal.

Since V_d(t) > r_d and V_d'(t) < r_d' can hold simultaneously for different denominations d, d', the trader's emotional state is literally a function of which denomination they are looking at. **The reference point is not a property of the position — it is a property of the denomination frame.**

### 4.5 Denomination-Dependent Disposition Effect

Odean (1998) measured the disposition effect via:

```
PGR = realized gains / (realized gains + paper gains)     = 0.148
PLR = realized losses / (realized losses + paper losses)   = 0.098
DE  = PGR - PLR                                            = 0.050
```

These metrics are implicitly denomination-specific. Define the **denomination-d disposition effect**:

```
PGR(d) = positions with gain in denomination d that are sold / total gain positions in d
PLR(d) = positions with loss in denomination d that are sold / total loss positions in d
DE(d)  = PGR(d) - PLR(d)
```

**Key insight**: A position can be a "winner" in denomination d₁ and a "loser" in denomination d₂. Therefore:

* PGR(d₁) includes this position (it's a gain → more likely to be sold)
* PLR(d₂) includes this position (it's a loss → more likely to be held)

The disposition effect can **flip sign** depending on the denomination. A trader who denominates in USD may sell a position (it's a "winner"), while a trader who denominates in BTC would hold the identical position (it's a "loser"). Same position, same moment, opposite actions — driven entirely by the denomination frame.

This is not a theoretical curiosity. In the cryptocurrency ecosystem, traders routinely switch between USD and BTC denomination views, and their trading behavior changes accordingly. The denomination-dependent disposition effect is a live, ongoing source of systematic error.

### 4.6 Hedonic Editing via Denomination Selection

Thaler (1985) identified four hedonic editing rules derived from the shape of v(·):

1. **Segregate gains**: v(x) + v(y) > v(x + y) for x, y > 0
2. **Integrate losses**: v(-(x+y)) > v(-x) + v(-y) for x, y > 0
3. **Integrate small losses with larger gains**
4. **Segregate small gains from larger losses** (silver lining)

Applied to denomination selection, these rules predict:

* **When the portfolio is up in most denominations**: The agent segregates — checking each denomination separately to savor multiple "win" narratives. "I'm up in dollars AND in gold AND in BTC!"
* **When the portfolio is down in most denominations**: The agent integrates — choosing a single denomination (whichever shows the least loss) and avoiding checking others. "At least I'm holding steady in euro terms."
* **When the portfolio is up in some denominations, down in others**: The agent selectively attends to the gaining denominations. This is **denomination shopping** — the hedonic editing rule applied not to outcome bundling but to denomination selection.

The prediction is testable: agents should preferentially report portfolio performance in whichever denomination shows the most favorable trajectory, and should avoid or suppress denominations that show losses. Cryptocurrency forums provide rich naturalistic data for this pattern — the switch from "show me USD value" to "show me sat value" typically coincides with BTC price surges that make USD-denominated performance look poor relative to a BTC benchmark.

### 4.7 The Neurodivergent Advantage: Fourth Prediction

De Martino et al. (2008) showed autistic individuals have ~46% reduced susceptibility to gain/loss framing (7.66% vs. 14.24% framing effect). The existing KB documents three predictions from this finding:

1. Weaker mental account formation
2. Lower partition granularity
3. Higher effective fungibility

We add a **fourth prediction**: **autistic traders should show higher denomination invariance**.

**Mechanism**: If denomination choice is a framing manipulation (Section 4.3), and autistic individuals show reduced framing susceptibility, then autistic traders should:

* Show lower variance in risk-taking across denomination conditions
* Be less likely to switch denominations based on hedonic optimization
* Exhibit more consistent DE(d) values across denominations (less denomination-dependent disposition effect)
* Be more receptive to multi-denomination dashboard views (the multi-denomination view is the *systematic* approach; single-denomination is the *heuristic* approach; high-systematizing individuals should prefer the former — per Baron-Cohen, 2009)

**Testable prediction**: In an experimental setting, present traders with identical portfolios displayed in different denominations. Measure risk-taking (willingness to hold, increase, or decrease position). Autistic traders should show a smaller standard deviation of risk-taking across denomination conditions.

**Connection to Grinblatt et al. (2012)**: Higher-IQ investors showed reduced disposition effect and better performance. If IQ correlates with reduced framing susceptibility (plausible given the cognitive mechanism), then higher-IQ traders should also show higher denomination invariance. The multi-denomination framework provides a new dimension for testing the IQ-performance relationship.

---

## 5. Geometric Interpretation

### 5.1 Growth Vector Space

The growth vector g(t₀, t₁) ∈ ℝⁿ₊ lives in the positive orthant of n-dimensional space. For the n = 2 case (e.g., D = {USD, BTC}), we can visualize:

```
        g_BTC
        ↑
        |
   III  |  I       (Growth Cone C)
        |  /
        | /  G = γ iso-line
  ------+/------→ g_USD
        |
   IV   |  II
        |
```

**Regions**:

* **Quadrant I** (g_USD > 1, g_BTC > 1): Portfolio grew in both denominations. G > 1. **Genuine growth.**
* **Quadrant II** (g_USD > 1, g_BTC < 1): Portfolio grew in USD, shrank in BTC. Mixed signal. A USD-denominating trader feels good; a BTC-denominating trader feels bad. G < 1.
* **Quadrant III** (g_USD < 1, g_BTC < 1): Portfolio shrank in both. G < 1. **Genuine contraction.**
* **Quadrant IV** (g_USD < 1, g_BTC > 1): Opposite of Quadrant II.

### 5.2 The Growth Cone

The **growth cone** C is the region where all components exceed 1:

```
C = {g ∈ ℝⁿ₊ : g_d > 1  for all d ∈ D}
```

In general dimension, C = (1, ∞)ⁿ — the interior of the unit hypercube's complement in the positive orthant. The growth cone is the region of **denomination-invariant growth**: inside C, the portfolio is unambiguously growing regardless of denomination choice.

### 5.3 Iso-G Surfaces

For a given threshold γ, the set {g : G(g) = γ} = {g : min_d g_d = γ} is the boundary of the hypercube [γ, ∞)ⁿ. These are "L-shaped" boundaries in 2D (right angles at corners), forming the level sets of the G metric.

### 5.4 Portfolio Trajectory

Over time, the cumulative growth vector traces a curve through ℝⁿ₊. Entry into the growth cone C is a significant event (the portfolio begins denomination-invariant growth); exit from C signals that at least one denomination has turned negative. The trajectory's distance from the diagonal (the line g_d₁ = g_d₂ = ... = g_dₙ) measures denomination sensitivity — portfolios near the diagonal perform similarly across all denominations.

---

## 6. Edge Cases and Pathologies

### 6.1 Denominator Goes to Zero

If price_d(t) → 0 (a denomination asset becomes worthless), then V_d(t) → ∞. This is harmless for G computation (an infinite growth ratio is never the minimum), but creates numerical instability.

**Resolution**: Require price_d(t) > ε for some minimum threshold ε > 0. In practice, restrict D to liquid, actively-traded assets. If a denomination asset begins to fail, remove it from D.

### 6.2 Circular Dependency

When the portfolio holds a denomination asset (e.g., portfolio contains BTC and D includes BTC), the valuation is well-defined but **partially degenerate**:

```
V_BTC(t) includes a term (q_BTC · price_BTC(t)) / price_BTC(t) = q_BTC
```

The BTC component of the portfolio always contributes exactly q_BTC to V_BTC(t), regardless of BTC price. This means changes in BTC price only affect V_BTC through the *other* portfolio holdings. When the portfolio is concentrated in the denomination asset (e.g., 90% BTC, denominated in BTC), V_BTC becomes insensitive to the main portfolio driver — a degenerate but well-defined case.

### 6.3 Transaction Costs

Real exchanges incur costs (fees, slippage, bid-ask spread). The denomination-adjusted value after costs:

```
V_d^real(t) = V_d(t) - T_d(t) / price_d(t)
```

where T_d(t) is the cumulative transaction cost in base units. Importantly, transaction costs are themselves denomination-dependent: converting to BTC may incur different fees than converting to USD. The G metric computed on V_d^real correctly penalizes for denomination-specific friction.

### 6.4 Time-Varying Denomination Sets

If D changes over time (an asset enters or exits the denomination set), compute G over the intersection:

```
G(t₀, t₁) = min_{d ∈ D(t₀) ∩ D(t₁)} { V_d(t₁) / V_d(t₀) }
```

This ensures comparability: only denominations observable at both endpoints are used.

---

## 7. Multi-Denomination Risk Metrics

Single-denomination risk metrics (Sharpe ratio, maximum drawdown, Sortino ratio) inherit all the framing biases of their denomination. We define denomination-invariant counterparts:

### 7.1 Denomination-Invariant Sharpe Ratio

```
SR_d = (E[r_d] - r_f,d) / σ(r_d)       for each d ∈ D

SR_inv = min_{d ∈ D} { SR_d }
```

where r_d is the portfolio return in denomination d, and r_f,d is the risk-free rate in denomination d (note: there is no universal risk-free rate — even the "risk-free rate" is denomination-dependent).

### 7.2 Denomination-Invariant Maximum Drawdown

```
MDD_d = max_{t₀ < t₁} { 1 - V_d(t₁) / V_d(t₀) }     for each d ∈ D

MDD_inv = max_{d ∈ D} { MDD_d }
```

The worst drawdown across all denominations. A trader who experienced "only" a 15% drawdown in USD may have experienced a 40% drawdown in BTC terms — and MDD_inv reports the 40%.

### 7.3 Denomination-Invariant Sortino Ratio

```
Sortino_d = (E[r_d] - r_f,d) / σ_down(r_d)     for each d ∈ D

Sortino_inv = min_{d ∈ D} { Sortino_d }
```

### 7.4 Spread of Sharpe Vector as Hidden Currency Risk

The vector (SR_d₁, SR_d₂, ..., SR_dₙ) is the **Sharpe vector**. Its spread:

```
Δ_SR = max_d { SR_d } - min_d { SR_d }
```

measures hidden denomination risk. A portfolio with high SR in USD but low SR in BTC has implicit currency exposure that single-denomination Sharpe reporting conceals. High Δ_SR is a red flag: the portfolio's risk-adjusted returns are fragile and denomination-dependent.

### 7.5 Connection to Purchasing Power

When D includes consumption goods (e.g., d = "barrel of oil," d = "bushel of wheat," d = "median rent"), the denomination-invariant metrics become **real** metrics in the economic sense — measuring performance against actual purchasing power rather than against an arbitrary currency. This is the natural extension: denominate in what you actually consume, and G tells you whether your portfolio's real purchasing power grew.

---

## 8. Practical Implementation

### 8.1 Multi-Denomination Dashboard

A rational portfolio monitoring system computes V_d(t) for all d ∈ D simultaneously, displaying:

* Current valuation vector V(t)
* Growth vector g(t₀, t) from portfolio inception
* Denomination-invariant growth G
* Denomination spread S
* Alert when S exceeds a configurable threshold

The dashboard eliminates denomination anchoring by presenting all denominations simultaneously. The trader cannot selectively attend to a single favorable denomination when all are visible.

### 8.2 Divergence Alerts

Set threshold τ on the denomination spread. When S > τ:

* Flag that single-denomination P&L is unreliable
* Display the growth vector explicitly
* Force the trader to acknowledge the spread before making trade decisions

### 8.3 Historical Denomination-Invariant Alpha

To assess whether a trading strategy generates genuine alpha (outperformance), compute:

```
α_inv = G_portfolio - G_benchmark
```

If α_inv > 0, the portfolio outperformed the benchmark in *every* denomination — a much stronger claim than single-denomination alpha.

### 8.4 Reference Implementation

See [`debiasing-frameworks/examples/multi-denomination-tracker.py`](../debiasing-frameworks/examples/multi-denomination-tracker.py) for a working Python implementation of the N-dimensional valuation framework, including growth vector computation, G metric calculation, and spread diagnostics.

---

## 9. Why This Matters for Behavioral Finance

### 9.1 The Invisible Bias

Most cognitive biases in trading are at least *partially* visible to the trader. A trader may recognize they are "riding a loser" (disposition effect) or "revenge trading" (break-even effect). But denomination bias is typically **invisible**: the denomination is treated as a neutral, objective measurement choice rather than as a frame that shapes perception and behavior.

This invisibility makes denomination bias more dangerous than many cataloged biases. The trader does not know they are being biased, because the denomination feels like a fact ("my portfolio is worth $X") rather than a choice ("I chose to measure my portfolio in USD rather than in gold or BTC or purchasing-power units").

### 9.2 Mechanical Debiasing

The multi-denomination framework is a **mechanical debiasing system**. Unlike cognitive debiasing strategies that require ongoing effort, vigilance, and metacognition, the multi-denomination dashboard operates automatically:

1. Compute V_d(t) for all d — no judgment required
2. Compute G = min_d {g_d} — no interpretation required
3. Display the result — the math eliminates the bias before it forms

The min-growth metric G is specifically designed to resist hedonic editing: it always reports the worst denomination, preventing selective attention to favorable framings.

### 9.3 Honest Alpha Assessment

Many apparently successful trading strategies are actually denomination-correlated momentum plays. A crypto portfolio that "outperformed" in USD during a crypto bull run may have underperformed in BTC terms — revealing that the "alpha" was simply long exposure to the asset class, not genuine skill.

G forces an honest assessment: if G_portfolio > G_benchmark > 1, the strategy generated real value. If G_portfolio > 1 but only because one denomination (the familiar one) showed strong performance, S will be large, flagging the fragility of the claim.

---

## 10. References

| Citation | Full Reference | DOI |
|---------|----------------|-----|
| **Tversky & Kahneman (1981)** | Tversky A, Kahneman D. The Framing of Decisions and the Psychology of Choice. *Science*, 211(4481), 453-458. | [10.1126/science.7455683](https://doi.org/10.1126/science.7455683) |
| **Thaler (1985)** | Thaler RH. Mental Accounting and Consumer Choice. *Marketing Science*, 4(3), 199-214. | [10.1287/mksc.4.3.199](https://doi.org/10.1287/mksc.4.3.199) |
| **Thaler (1999)** | Thaler RH. Mental Accounting Matters. *J. Behav. Decision Making*, 12(3), 183-206. | [10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F](https://doi.org/10.1002/(SICI)1099-0771(199909)12:3%3C183::AID-BDM318%3E3.0.CO;2-F) |
| **Kahneman & Tversky (1979)** | Kahneman D, Tversky A. Prospect Theory: An Analysis of Decision under Risk. *Econometrica*, 47(2), 263-291. | [10.2307/1914185](https://doi.org/10.2307/1914185) |
| **Tversky & Kahneman (1992)** | Tversky A, Kahneman D. Advances in Prospect Theory: Cumulative Representation of Uncertainty. *J. Risk & Uncertainty*, 5(4), 297-323. | [10.1007/BF00122574](https://doi.org/10.1007/BF00122574) |
| **De Martino et al. (2008)** | De Martino B, Harrison NA, Knafo S, Bird G, Dolan RJ. Explaining Enhanced Logical Consistency during Decision Making in Autism. *J. Neuroscience*, 28(42), 10746-10750. | [10.1523/JNEUROSCI.2895-08.2008](https://doi.org/10.1523/JNEUROSCI.2895-08.2008) |
| **Shefrin & Statman (1985)** | Shefrin H, Statman M. The Disposition to Sell Winners Too Early and Ride Losers Too Long. *Journal of Finance*, 40(3), 777-790. | [10.2307/2327802](https://doi.org/10.2307/2327802) |
| **Odean (1998)** | Odean T. Are Investors Reluctant to Realize Their Losses? *Journal of Finance*, 53(5), 1775-1798. | [10.1111/0022-1082.00072](https://doi.org/10.1111/0022-1082.00072) |
| **Weber & Johnson (2009)** | Weber EU, Johnson EJ. Mindful Judgment and Decision Making. *Annual Review of Psychology*, 60, 53-85. | [10.1146/annurev.psych.60.110707.163633](https://doi.org/10.1146/annurev.psych.60.110707.163633) |
| **Raghubir & Srivastava (2002)** | Raghubir P, Srivastava J. Effect of Face Value on Product Valuation in Foreign Currencies. *J. Consumer Research*, 29(3), 335-347. | [10.1086/344430](https://doi.org/10.1086/344430) |
| **Shafir, Diamond & Tversky (1997)** | Shafir E, Diamond P, Tversky A. Money Illusion. *Quarterly Journal of Economics*, 112(2), 341-374. | [10.1162/003355397555208](https://doi.org/10.1162/003355397555208) |
| **Grinblatt et al. (2012)** | Grinblatt M, Keloharju M, Linnainmaa J. IQ, Trading Behavior, and Performance. *J. Financial Economics*, 104(2), 339-362. | [10.1016/j.jfineco.2011.05.016](https://doi.org/10.1016/j.jfineco.2011.05.016) |
| **Baron-Cohen (2009)** | Baron-Cohen S. Autism: The Empathizing-Systematizing (E-S) Theory. *Annals NY Acad. Sci.*, 1156(1), 68-80. | [10.1111/j.1749-6632.2009.04467.x](https://doi.org/10.1111/j.1749-6632.2009.04467.x) |
| **Tversky & Kahneman (1974)** | Tversky A, Kahneman D. Judgment under Uncertainty: Heuristics and Biases. *Science*, 185(4157), 1124-1131. | [10.1126/science.185.4157.1124](https://doi.org/10.1126/science.185.4157.1124) |

---

## 11. Cross-References

* [fungibility-asset-transformation-rational-framework.md](fungibility-asset-transformation-rational-framework.md) — The fungibility axiom and W_total framework; this paper extends it to N-dimensional denomination space (Section 4.1–4.2)
* [mental-accounting-thaler-comprehensive.md](mental-accounting-thaler-comprehensive.md) — Hedonic editing rules that predict denomination shopping behavior (Section 4.6); fungibility violation as the core irrationality that denomination bias exemplifies
* [de-martino-2008-framing-effects-autism-explained.md](de-martino-2008-framing-effects-autism-explained.md) — Framing effects and autism; denomination choice as frame selection (Section 4.3); neurodivergent advantage fourth prediction (Section 4.7)
* [behavioral-biases-multi-paper-synthesis.md](behavioral-biases-multi-paper-synthesis.md) — Multi-paper synthesis establishing the shared mechanism of context-dependent framing; denomination as a continuous framing dimension
* [BIBLIOGRAPHY.md](../BIBLIOGRAPHY.md) — Master bibliography for the KB
* [KB-ROUTING.md](../KB-ROUTING.md) — Navigation routing for the knowledge base

*Implementation: [`debiasing-frameworks/examples/multi-denomination-tracker.py`](../debiasing-frameworks/examples/multi-denomination-tracker.py)*
