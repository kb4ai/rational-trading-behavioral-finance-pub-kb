# Denomination-Invariant Portfolio Evaluation: A Debiasing Framework

> **A practical protocol for eliminating single-denominator bias through simultaneous multi-asset projection**

[Collected 2026-03-07] [AI Provider: Anthropic, Claude Opus 4.6]

---

## 1. Bias Identification

### 1.1 Name and Aliases

* **Primary**: Single-Denominator Bias (Denomination Bias)
* **Aliases**: Unit-of-account anchoring, Currency framing bias, Denomination illusion, Numeraire anchoring
* **Related constructs**: Money illusion (Shafir, Diamond & Tversky, 1997), Numerosity heuristic (Pelham, Sumarta & Myaskovsky, 1994), Face value effect (Raghubir & Srivastava, 2002), Euro illusion (Hofmann et al., 2006)

### 1.2 Formal Definition

The tendency to evaluate portfolio performance using a single unit of account (denomination), causing systematic misperception of real portfolio growth when the chosen denomination's purchasing power changes relative to other stores of value.

**Formal statement**: An agent exhibits denomination bias when their decisions are not invariant under change of numeraire. That is, switching from denomination d₁ to d₂ changes their risk-taking, rebalancing, or sell/hold decisions for the same portfolio state.

Let D = {d₁, d₂, ..., dₙ} be a set of denominations. Let π(W, d) denote the agent's decision function given wealth state W evaluated in denomination d. The agent is denomination-rational if and only if:

```
π(W, dᵢ) = π(W, dⱼ)   ∀ dᵢ, dⱼ ∈ D
```

Any violation of this invariance condition constitutes denomination bias.

### 1.3 Empirical Evidence

The evidence base spans multiple research traditions. Effect sizes are substantial and replicate cross-culturally:

| Study | Effect | Magnitude |
|-------|--------|-----------|
| Shafir, Diamond & Tversky (1997) | Money illusion: nominal/real confusion | 60-80% of participants exhibit the bias |
| Fehr & Tyran (2001) | Nominal inertia from denomination framing | Substantial and long-lasting; asymmetric for negative shocks |
| Raghubir & Srivastava (2002) | Face value anchoring in foreign currencies | 15-30% spending differences |
| Pelham, Sumarta & Myaskovsky (1994) | Numerosity heuristic (more units = "more value") | Significant across 5 experiments; amplified by cognitive load |
| Wertenbroch, Soman & Chattopadhyay (2007) | Reference-dependent numerosity in transaction evaluation | Robust across 6 experiments |
| Hofmann et al. (2006) | Euro illusion after currency redenomination | >80% of respondents affected; persisted years post-transition |
| Mrkva et al. (2021) | Replication of money illusion in contemporary samples | Effect robust but moderately attenuated vs. 1997 |
| Odean (1998) | Disposition effect anchored to purchase-price denomination | ~60% higher probability of selling winners vs. losers |
| Benartzi & Thaler (1995) | Myopic loss aversion from evaluation frequency | Quantitative match to historical equity premium |

**Key moderators** (from literature review):

* **Amplifiers**: Cognitive load, time pressure, emotional arousal, loss framing
* **Attenuators**: Currency familiarity, financial literacy, salience of alternative reference points, experience

The moderator pattern directly implies the debiasing strategy: *forcing simultaneous salience of multiple denominational representations* should be among the most effective interventions.

### 1.4 Linguistic Markers

How this bias appears in trading discourse:

| Marker | Bias Revealed |
|--------|---------------|
| "I'm up 30% this year" | In which denomination? Compared to what alternative? |
| "My BTC stack is growing" | But is it shrinking in USD/gold/purchasing-power terms? |
| "I'm in profit on this trade" | In which denomination was the entry price recorded? |
| "Crypto winter" / "Bull market" | Framed relative to which denomination? USD bull = BTC bear possible |
| "HODL" mentality | Holding through losses visible only in alternative denominations |
| "Stack sats" | Community denomination pressure — social framing locks one numeraire |
| "The dollar is losing value" | True in gold terms, false in debt-servicing terms — which? |
| "Fund returned 25% last year" | In nominal USD, while gold returned 30%? While CPI was 6%? |
| "My portfolio hit a new ATH" | In which denomination? Nominal USD ATH may mask real purchasing power loss |

**Diagnostic**: If a statement about portfolio performance cannot be made simultaneously true across three or more denominations, the speaker is likely anchored to a single denomination.

---

## 2. The Debiasing Protocol

### 2.1 Step 1: Define Your Denomination Set D

The denomination set D is the collection of units in which you will simultaneously evaluate all portfolio decisions. Selection criteria:

**Required denominators:**

* Your **primary spending currency** (USD, EUR, GBP, etc.) — this grounds portfolio value in purchasing power for daily life
* Any asset you claim to be **"accumulating"** (BTC, ETH, etc.) — if you say "I'm stacking BTC," then BTC must be in D, or you're not measuring what you claim to optimize

**Recommended denominators:**

* At least one **real-goods denominator** — gold ounces, CPI basket, housing index, or months-of-spending — to anchor against inflation
* An **opportunity cost benchmark** — S&P 500 units, total market index — to measure whether active management adds value

**Minimum**: |D| = 3. Below this, single-denomination bias remains largely unchecked.
**Recommended**: |D| = 4-5. Beyond 5, cognitive load increases without proportional debiasing benefit.

**Profiles:**

| Trader Type | Recommended D | Rationale |
|-------------|---------------|-----------|
| Crypto-native | {USD, BTC, ETH, gold-oz} | Captures fiat, store-of-value, smart-contract, and real-goods dimensions |
| Traditional equity investor | {USD, gold-oz, CPI-basket, SPX-units} | Captures nominal, inflation-adjusted, and benchmark-relative performance |
| Retiree / income-focused | {USD, months-of-spending, gold-oz, bond-index} | Grounds evaluation in actual consumption horizon |
| Multi-asset macro trader | {USD, BTC, gold-oz, CNY, SPX-units} | Captures major currency regimes and asset classes |

### 2.2 Step 2: Compute Multi-Denomination Portfolio Values

For each evaluation period t, compute the portfolio's value in every denomination d ∈ D:

```
V_d(t) = Σᵢ (qᵢ × price_i(t)) / price_d(t)    for each d ∈ D
```

Where:

* qᵢ = quantity of asset i held in portfolio
* price_i(t) = price of asset i at time t in a common base unit
* price_d(t) = price of denominator d at time t in the same common base unit

**In practice**: pick any consistent base (e.g., USD) to compute the numerator once, then divide by each denominator's price.

**Critical rule**: Display ALL values simultaneously. Never look at just one. The debiasing power comes from the simultaneous juxtaposition — seeing your portfolio in 4 denominations at once forces cross-denomination comparison that a single view cannot provide.

### 2.3 Step 3: Calculate Growth Vector and G Metric

For a period from t₀ to t₁, compute:

**Per-denominator growth rate:**

```
g_d = V_d(t₁) / V_d(t₀)    for each d ∈ D
```

**Denomination-invariant growth metric (G):**

```
G = min(g_d)    over all d ∈ D
```

G is the worst-case growth rate across all denominations. If G > 1, the portfolio genuinely grew no matter how you measure it. This is the hardest test — and the only honest one.

**Denomination sensitivity (spread S):**

```
S = max(g_d) - min(g_d)
```

S measures how much your perceived performance depends on denomination choice. High S = your "gains" are largely a denomination artifact.

**What these metrics mean in practice:**

* G is your "floor return" — the worst honest story you can tell about your portfolio
* S is your "denomination sensitivity" — how much the story changes depending on which currency you measure in
* The growth vector [g_d₁, g_d₂, ..., g_dₙ] is the full picture — each component tells you how you did measured in that specific asset

### 2.4 Step 4: Interpret Results

| G | S | Interpretation | Action |
|---|---|----------------|--------|
| G > 1 | S < 0.05 | **Genuine growth** across all frames | Strategy working; maintain course |
| G > 1 | S > 0.10 | Growth but **denomination-sensitive** | Investigate which denominator barely grew — that's your weak spot. You may be riding one asset's momentum, not generating alpha |
| G ≈ 1 | S > 0.10 | **Breakeven overall**, wild denomination variation | You're riding denomination movements, not generating alpha. Your "gains" in one frame are exactly offset by "losses" in another |
| G < 1 | S < 0.05 | **Loss across all frames** | Strategy failing; review fundamentals. No denomination choice can rescue this |
| G < 1 | S > 0.10 | **Loss in worst frame**, possibly gains in others | **Danger zone**: denomination bias is actively hiding your loss. A single-denomination view would show "profit" while you're actually underwater in the most demanding frame |

**The danger zone deserves emphasis.** When G < 1 but some g_d > 1, a trader using only the favorable denomination will feel confident while actually losing ground. This is the exact scenario where denomination bias causes the most damage — it suppresses the alarm signal that should trigger strategy review.

### 2.5 Step 5: Denomination-Invariant Decision Rules

Replace single-denomination triggers with multi-denomination rules:

**Rebalance trigger:**

```
IF min(g_d) < threshold_rebalance  THEN  trigger rebalance review
```

Recommended threshold: 0.95 (5% drawdown in worst denomination). This catches losses that a favorable denomination would mask.

**Divergence alert:**

```
IF S > 0.10  THEN  flag for investigation
```

When spread exceeds 10%, your performance story is denomination-dependent. This doesn't mean action is required — but it means any action you take is likely contaminated by denomination framing unless you explicitly account for it.

**Position sizing:**

Size positions based on G-adjusted portfolio value, not single-denomination value. If G shows you at 0.92 but USD shows 1.05, you have less real capital than you think. Size for 0.92.

**Stop-loss:**

Check stop-loss conditions in ALL denominations, not just the entry denomination:

```
IF any g_d < stop_loss_threshold  THEN  evaluate exit
```

A position that's "only down 3% in USD" but "down 25% in BTC terms" has breached a meaningful threshold that single-denomination tracking misses.

**Entry denomination independence:**

Record entry price in ALL denominations simultaneously. This prevents the disposition effect from anchoring to whichever denomination happened to be used at entry (Odean, 1998). When reviewing whether to hold or sell, examine P&L in every denomination — if the hold/sell decision changes depending on which denomination you look at, you've found a denomination bias in action.

---

## 3. Exploitation Patterns

How institutions and platforms exploit single-denominator thinking:

### 3.1 P&L Display Manipulation

Exchanges and brokerages choose default denomination displays strategically:

* **USD-default display**: Hides BTC-denominated losses during bull markets. A trader sees "+15% in USD" and feels good, while their BTC-denominated value fell 20% because they were underweight BTC during a rally
* **BTC-default display (crypto exchanges)**: Hides USD losses during bear markets. "Your BTC balance is unchanged!" masks the reality that your USD value halved
* **Percentage-only reporting**: Suppresses absolute loss information and activates numerosity effects for small percentages

### 3.2 Marketing with Favorable Denomination

* **Fund performance**: "Fund returned 25% last year!" — in nominal USD, while gold returned 30% and CPI was 6%. Real return: ~19%. Opportunity cost vs. gold: -5%
* **Token sales**: ICO/IDO pricing uses the denomination that minimizes perceived cost ("only 0.001 ETH per token" sounds cheap; "$3.50 per token" sounds expensive)
* **Retrospective denomination selection**: Reports choose the denomination that tells the best story *after* the fact

### 3.3 Community Denomination Pressure

* **"Stack sats" culture**: Establishes satoshis as the community numeraire, creating social pressure against BTC-denominated or USD-denominated loss awareness
* **"Number go up" framing**: Locks attention on USD price of BTC, preventing evaluation in real-goods terms (gold, CPI, housing)
* **Tribal denomination identity**: "Bitcoiners don't care about USD price" — this is denomination bias elevated to cultural norm

### 3.4 Benchmark Gaming

Fund managers choose the benchmark denomination that maximizes apparent alpha:

* A crypto fund benchmarking against USD during a crypto bull market captures beta as alpha
* A gold fund benchmarking against CPI during inflationary periods captures commodity momentum as alpha
* **Defense**: Always ask "What would this return look like measured in [alternative denomination]?"

### 3.5 Inflation Masking

Nominal USD returns mask real purchasing power losses. A "5% annual return" during 6% inflation is a -1% real return — but the nominal number activates the gain branch of the prospect theory value function, suppressing the loss signal.

### 3.6 Entry Price Denomination Anchoring

The denomination in which entry price is recorded determines the reference point for disposition effect (Shafir et al., 1997; Odean, 1998). Platforms that record entry price in USD anchor all subsequent P&L evaluation to USD, even for assets whose "natural" denomination might be different (e.g., DeFi yields denominated in ETH).

---

## 4. Connection to Existing KB Frameworks

### 4.1 The Fungibility Axiom

The denomination label is a form of mental accounting label. The fungibility axiom (see [fungibility-asset-transformation-rational-framework.md](../core-research/fungibility-asset-transformation-rational-framework.md)) requires that:

> Only W_total(t) and the covariance/utility structure of the portfolio matters. The *labels* attached to sub-portfolios carry zero information content.

Denomination invariance is a direct corollary: if labels carry no information, then the *unit label* attached to the portfolio's value carries no information. Any decision that changes based on denomination choice reveals a rationality violation — the agent is optimizing over labels, not over the underlying wealth state.

The partition welfare loss from the fungibility framework applies directly:

```
L_denomination = U*(W_total) - U*(W_viewed_in_single_denom)
```

This loss is non-negative and increases with the divergence between denominations.

### 4.2 Mental Accounting

Thaler's (1999) three-account framework (current income, current wealth, future income) partitions wealth into non-fungible buckets. Denomination choice creates a **fourth axis of non-fungibility** beyond Thaler's three (see [mental-accounting-thaler-comprehensive.md](../core-research/mental-accounting-thaler-comprehensive.md)):

1. **Source non-fungibility** — wages vs. windfall vs. investment returns
2. **Label non-fungibility** — "savings" vs. "spending money" vs. "emergency fund"
3. **Temporal non-fungibility** — current income vs. wealth vs. future income
4. **Denomination non-fungibility** — USD-denominated vs. BTC-denominated vs. gold-denominated wealth

The empirical MPC (marginal propensity to consume) differences Thaler documents across accounts likely extend to denomination: gains in an "alien" denomination (e.g., BTC gains for a USD-native trader) are re-risked more readily because they feel like "play money" — precisely the house money effect operating through denomination framing.

### 4.3 Framing Effects

Denomination = frame. The same portfolio state can be described as gain or loss depending on denomination choice. This is a direct application of Tversky & Kahneman's (1981) framing paradigm.

De Martino et al. (2008) showed that autistic individuals exhibit ~46% reduced susceptibility to gain/loss framing (see [de-martino-2008-framing-effects-autism-explained.md](../core-research/de-martino-2008-framing-effects-autism-explained.md)). This predicts that individuals with high systematizing cognitive style may be *less* susceptible to denomination bias — but not immune. The multi-denomination protocol provides explicit systematic support for what reduced framing susceptibility provides implicitly.

### 4.4 Kelly Criterion Integration

When computing the Kelly fraction f* = (bp - q) / b, the parameters b (odds), p (probability of win), and q (probability of loss) should be **denomination-invariant**. If the Kelly-optimal position size changes when you switch from USD to BTC denomination, one of these things is true:

1. Your estimates of b, p, q are contaminated by denomination framing
2. The asset's return distribution is genuinely different in different denominations (which is real — but the Kelly fraction should account for this explicitly, not accidentally)

**Practical rule**: Compute Kelly fraction in at least 2 denominations. If f* differs significantly, investigate why. Often the cause is that the "odds" b were estimated in a favorable denomination that inflated perceived edge.

---

## 5. Implementation Reference

A complete working implementation is provided in [`debiasing-frameworks/examples/multi-denomination-tracker.py`](examples/multi-denomination-tracker.py).

The script demonstrates:

* **Multi-denomination valuation**: Computing V_d(t) for each denominator in D, projecting a single portfolio into multiple simultaneous views
* **Growth vector computation**: Per-denominator growth rates g_d revealing how performance differs across frames
* **G metric (min-growth)**: The denomination-invariant floor — genuine growth only when G > 1
* **Divergence alerts**: Automatic flagging when denomination sensitivity S exceeds threshold, warning that performance perception is frame-dependent
* **Three diagnostic scenarios**: Genuine growth (G > 1, S small), denomination divergence (G ≈ 1, S large), and hidden loss (G < 1 masked by favorable denomination)

The implementation uses hardcoded market snapshots for reproducibility. To use with live data, replace `MarketSnapshot` prices with API calls to your preferred price feed. The mathematical core (`compute_denominated_values`, `growth_vector`, `min_growth_metric`, `divergence_alert`) is dependency-free and can be embedded directly into any trading system.

**Running the example:**

```bash
cd debiasing-frameworks/examples/
./multi-denomination-tracker.py
# or: python multi-denomination-tracker.py
```

---

## 6. Quick-Start Checklist

For a trader implementing this framework today:

- [ ] **Choose D**: Select 3-5 denominations covering your spending currency, accumulation targets, and at least one real-goods anchor
- [ ] **Set up tracking**: Create a spreadsheet or script that computes V_d(t) for each d ∈ D at your evaluation frequency (weekly recommended)
- [ ] **Record entry prices in all denominations**: When opening any position, log the entry price in every d ∈ D, not just your default currency
- [ ] **Compute G and S at each evaluation**: G = min(g_d), S = max(g_d) - min(g_d). Write these down. Track them over time
- [ ] **Apply the interpretation table**: Map your (G, S) pair to the table in Section 2.4. If G < 1 and S > 0.10, treat this as a red alert regardless of what your best denomination shows
- [ ] **Check stop-losses in all denominations**: A position that breaches stop-loss in *any* denomination deserves review, even if other denominations show it as fine
- [ ] **Review denomination divergence monthly**: If S has been consistently > 0.10, your portfolio's story depends on which currency you tell it in. This is a signal to investigate, not a signal to pick the flattering denomination

---

## References

Barberis, N., & Thaler, R. H. (2003). A survey of behavioral finance. In G. Constantinides, M. Harris, & R. Stulz (Eds.), *Handbook of the Economics of Finance*, Vol. 1, pp. 1053-1128. Elsevier. [DOI: 10.1016/S1574-0102(03)01027-6](https://doi.org/10.1016/S1574-0102(03)01027-6)

Benartzi, S., & Thaler, R. H. (1995). Myopic loss aversion and the equity premium puzzle. *Quarterly Journal of Economics*, 110(1), 73-92. [DOI: 10.2307/2118511](https://doi.org/10.2307/2118511)

De Martino, B., Harrison, N. A., Knafo, S., Bird, G., & Dolan, R. J. (2008). Explaining enhanced logical consistency during decision making in autism. *Journal of Neuroscience*, 28(42), 10746-10750. [DOI: 10.1523/JNEUROSCI.2895-08.2008](https://doi.org/10.1523/JNEUROSCI.2895-08.2008)

Fehr, E., & Tyran, J.-R. (2001). Does money illusion matter? *American Economic Review*, 91(5), 1239-1262. [DOI: 10.1257/aer.91.5.1239](https://doi.org/10.1257/aer.91.5.1239)

Hofmann, E., Kamleitner, B., Kirchler, E., & Schulz-Hardt, S. (2006). Kaufkraftschwund nach der Euroeinführung: Befunde und Implikationen. *European Psychologist*. [DOI: 10.1027//1016-9040.7.4.302](https://doi.org/10.1027//1016-9040.7.4.302)

Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263-291. [DOI: 10.2307/1914185](https://doi.org/10.2307/1914185)

Mrkva, K., et al. (2021). Revisiting "money illusion": Replication and extension of Shafir, Diamond, and Tversky (1997). *Journal of Economic Psychology*, 83. [DOI: 10.1016/j.joep.2020.102355](https://doi.org/10.1016/j.joep.2020.102355)

Odean, T. (1998). Are investors reluctant to realize their losses? *Journal of Finance*, 53(5), 1775-1798. [DOI: 10.1111/0022-1082.00072](https://doi.org/10.1111/0022-1082.00072)

Pelham, B. W., Sumarta, T. T., & Myaskovsky, L. (1994). The easy path from many to much: The numerosity heuristic. *Cognitive Psychology*, 26(2), 103-133. [DOI: 10.1006/cogp.1994.1004](https://doi.org/10.1006/cogp.1994.1004)

Raghubir, P. (2021). Valuing new currencies: A framework for future research. *Marketing Science Institute*. [MSI Working Paper](https://www.msi.org/wp-content/uploads/2021/03/Valuing_New_Currencies_-_Priya_Raghubir.pdf)

Raghubir, P., & Srivastava, J. (2002). Effect of face value on product valuation in foreign currencies. *Journal of Consumer Research*, 29(3), 335-347. [DOI: 10.1086/344432](https://doi.org/10.1086/344432)

Shafir, E., Diamond, P., & Tversky, A. (1997). Money illusion. *Quarterly Journal of Economics*, 112(2), 341-374. [DOI: 10.1162/003355397555208](https://doi.org/10.1162/003355397555208)

Thaler, R. H. (1985). Mental accounting and consumer choice. *Marketing Science*, 4(3), 199-214. [DOI: 10.1287/mksc.4.3.199](https://doi.org/10.1287/mksc.4.3.199)

Thaler, R. H. (1999). Mental accounting matters. *Journal of Behavioral Decision Making*, 12(3), 183-206. [DOI: 10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F](https://doi.org/10.1002/(SICI)1099-0771(199909)12:3%3C183::AID-BDM318%3E3.0.CO;2-F)

Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*, 211(4481), 453-458. [DOI: 10.1126/science.7455683](https://doi.org/10.1126/science.7455683)

Wertenbroch, K., Soman, D., & Chattopadhyay, A. (2007). On the perceived value of money: The reference dependence of currency numerosity effects. *Journal of Consumer Research*, 34(1), 1-10. [DOI: 10.1086/513041](https://doi.org/10.1086/513041)

---

*Cross-references: [fungibility-asset-transformation-rational-framework.md](../core-research/fungibility-asset-transformation-rational-framework.md) | [mental-accounting-thaler-comprehensive.md](../core-research/mental-accounting-thaler-comprehensive.md) | [de-martino-2008-framing-effects-autism-explained.md](../core-research/de-martino-2008-framing-effects-autism-explained.md) | [denomination-effects-literature-review.md](../research-artifacts/denomination-effects-literature-review.md) | [multi-denomination-tracker.py](examples/multi-denomination-tracker.py) | [KB-ROUTING.md](../KB-ROUTING.md)*
