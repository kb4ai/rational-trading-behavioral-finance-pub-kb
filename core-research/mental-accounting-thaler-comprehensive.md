# Mental Accounting: Thaler's Framework — Comprehensive Analysis

[Collected 2026-02-27] [AI Provider: Anthropic, Claude Sonnet 4.6]

---

## 1. Formal Definition and Theoretical Provenance

**Mental accounting** (Thaler, 1999, p. 183) is defined as:

> "the set of cognitive operations used by individuals and households to organize, evaluate, and keep track of financial activities."

This encompasses three separable but interacting functions:

1. **Perception and coding** — how outcomes are experienced and expressed as gains vs. losses relative to a reference point
2. **Assignment to accounts** — how outcomes are categorized into labeled buckets (income, wealth, future income; or: vacation fund, emergency fund, etc.)
3. **Frequency of account evaluation** — the temporal granularity with which accounts are "balanced" (daily P&L vs. annual portfolio vs. lifetime wealth)

Thaler's 1985 *Marketing Science* paper ([DOI: 10.1287/mksc.4.3.199](https://doi.org/10.1287/mksc.4.3.199)) introduced the formal model as a hybrid of Kahneman-Tversky prospect theory with microeconomic consumer theory. The 1999 *Journal of Behavioral Decision Making* paper ([DOI: 10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F](https://doi.org/10.1002/(SICI)1099-0771(199909)12:3%3C183::AID-BDM318%3E3.0.CO;2-F)) constitutes the definitive synthesis.

---

## 2. Mathematical Framework

### 2.1 Prospect Theory Value Function (Kahneman & Tversky, 1979)

The foundation is the reference-dependent value function v(·):

```
v(x) = x^α                    if x ≥ 0  (gains: concave, α < 1)
v(x) = -λ(-x)^β              if x < 0  (losses: convex, β < 1; λ > 1)
```

Empirically estimated: α ≈ β ≈ 0.88, λ ≈ 2.25 (Tversky & Kahneman, 1992).

The key properties:

* **Reference-dependence**: v is defined over *changes* from a reference point, not absolute wealth levels
* **Loss aversion**: |slope for losses| > |slope for gains| by factor λ ≈ 2.25
* **Diminishing sensitivity**: Concavity for gains (risk aversion), convexity for losses (risk seeking)

### 2.2 Thaler's Utility Decomposition (1985)

Total utility of a transaction decomposes into:

```
U(transaction) = v(acquisition utility) + v(transaction utility)
```

Where:

* **Acquisition utility** = v(good received) - v(price paid) = economic surplus, relative to willingness to pay
* **Transaction utility** = v(p_reference - p_actual) = utility derived purely from the "deal quality," independent of the good's intrinsic value

Transaction utility = 0 at the reference price; positive when p_actual < p_reference ("good deal"); negative when p_actual > p_reference ("rip-off"). This explains why consumers reject objectively net-positive purchases when the price exceeds a reference point, and accept negative-EV purchases when the deal feels advantageous.

### 2.3 Integration vs. Segregation: Hedonic Editing Rules

Given outcomes x and y, the agent evaluates either v(x + y) [integration] or v(x) + v(y) [segregation]. Thaler (1985) derives four hedonic editing principles from the shape of v(·):

**Principle 1 — Segregate gains** (because v is concave for gains):

```
v(x) + v(y) > v(x + y)   for x, y > 0
```

Experimental support: 64% of subjects believed a person winning two separate lotteries of $25 and $50 is happier than one winning $75 (Thaler, 1999).

**Principle 2 — Integrate losses** (because v is convex for losses):

```
v(-(x+y)) > v(-x) + v(-y)   for x, y > 0
```

A single $500 loss is less painful than two separate $200 and $300 losses.

**Principle 3 — Integrate small losses with larger gains** (loss absorption to exploit loss aversion):

```
v(G - L) > v(G) + v(-L)   when L << G and λ·L > v(G) - v(G-L)
```

A $30 tax bill feels less painful when mentally absorbed into a $500 paycheck than encountered separately.

**Principle 4 — Segregate small gains from larger losses** ("silver lining" effect):

```
v(G) + v(-L) > v(G - L)   when G << L
```

Winning $30 from a raffle feels better segregated from a $500 car repair than absorbed into the net -$470.

Empirical verification: Investors show bundled loss sales and segregated gain sales on the same day, consistent with these principles (Thaler, 1999, citing portfolio data).

---

## 3. The Fungibility Violation (Core Irrationality)

### 3.1 Theoretical Statement

Standard economic theory: money is **fully fungible** — $1 in a "vacation fund" has identical purchasing power and opportunity cost as $1 in a "checking account." Mental accounting violates fungibility by assigning different *marginal propensities to consume* (MPC) to identically-valued money based on:

* **Source** (inheritance vs. wages vs. windfall vs. gambling proceeds)
* **Label/category** (earmarked savings vs. discretionary spending)
* **Temporal position** (current income account vs. future income account vs. wealth account)

### 3.2 Three-Account Framework (Thaler, 1999)

Households segregate wealth into three non-fungible buckets with empirically distinct MPC values:

| Account | Examples | Typical MPC |
|---------|---------|-------------|
| Current income | Paycheck, recurring revenue | ~1.0 (high spend-through) |
| Current wealth | Savings, investments | ~0.03-0.05 (low spend-through) |
| Future income | Pension, illiquid assets | ~0.0 (treated as untouchable) |

The rational prediction — that $1 from any source has equal MPC — is systematically violated. Empirical finding: households have higher propensity to consume out of windfall income vs. regular income, and this propensity *decreases* as windfall size increases (Thaler, 1999).

### 3.3 The "I'm Broke" Pathology

A canonical manifestation: a person maintains $10,000 in a "rainy day" savings account at 2% while carrying $8,000 in credit card debt at 22% APR. The rational action — pay down the 22% debt with savings — is blocked by mental accounting: the savings are labeled "untouchable/future security," the credit card is a separate "current expenses" account. The net-wealth view (fungibility) sees these as the same pool; the mental accounting view sees irreconcilable categorical boundaries.

Formal characterization: let W = total wealth, partitioned into accounts A₁, A₂, ..., Aₙ with individual reference points rᵢ. The agent maximizes Σᵢ vᵢ(Aᵢ - rᵢ) subject to Σᵢ Aᵢ = W, rather than maximizing v(W - r_total). The decoupling of accounts from total wealth creates welfare losses from suboptimal capital allocation.

### 3.4 Spending as Asset Transformation (Mislabeled Loss)

Another pathology: treating consumption expenditure as a *loss* rather than an *exchange*. When purchasing electricity or groceries, the rational view is an asset transformation: money (liquid claim on goods) → utility (energy, nutrition). The money is not "gone"; it was exchanged at a mutually agreed price. Mental accounting frames the monetary outflow as a loss via the loss-aversion branch of v(·), generating unnecessary hedonic pain. This is compounded by the **pain of paying** construct (Prelec & Loewenstein, 1998).

---

## 4. Sub-Phenomena

### 4.1 The House Money Effect

**Paper**: Thaler & Johnson (1990). Gambling with the House Money and Trying to Break Even: The Effects of Prior Outcomes on Risky Choice. *Management Science*, 36(6), 643-660. [DOI: 10.1287/mnsc.36.6.643](https://doi.org/10.1287/mnsc.36.6.643)

**Mechanism**: Prior gains are mentally coded as "house money" — winnings that don't feel like "real" capital. Prospect theory integration applies: a prior gain G creates a cushion such that a subsequent potential loss L is partially absorbed. Formally, the agent evaluates v(G - L) rather than v(-L), where G > 0 reduces loss aversion.

**Quasi-Hedonic Editing (QHE)**: Thaler & Johnson proposed that agents integrate possible future losses with prior gains (treating them as reductions of previous gains) while segregating possible future gains — yielding increased risk proneness after a prior gain.

**Empirical evidence (2025 meta-analysis)**:

* 36 studies, Hedges' g = 0.37 (low-to-moderate) for continuous outcomes
* Risk ratio = 1.33 for binary outcomes after outlier adjustment
* Heterogeneity: I² = 88.1% (high); stronger in student samples (g = 0.50) and Asian samples (g = 0.68)
* Publication bias correction (trim-and-fill): g reduced to 0.07, suggesting true population effect may be substantially smaller
* Effect strongest in laboratory settings, weakest in real-world environments

**Source**: Frontiers in Psychology (2025). [The role of mental accounting in risk-taking and spending: a meta-analysis of the house-money effect](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1549626/full).

**Trading implication**: Traders who are "up on the day" take larger subsequent positions, treating profits as less real than initial capital. This is rational only if the trader is operating near a hard floor/bankruptcy constraint; in continuous portfolio management it represents error.

### 4.2 Break-Even Effect (Companion to House Money)

**Mechanism**: After a prior loss, gambles offering a chance to "break even" become disproportionately attractive. The agent is seeking to close a loss account that is generating ongoing hedonic pain. Formally: if current state is (-L), a gamble offering {+L with p, -K with (1-p)} is evaluated in a reference frame where +L returns the account to zero (massive gain on the loss branch of v), making even low-probability break-even bets attractive.

**Trading manifestation**: "Revenge trading" after a bad day; doubling down on losing positions to avoid realizing a loss in the account.

### 4.3 Sunk Cost Effect in Mental Accounting

**Paper**: Arkes & Blumer (1985). The Psychology of Sunk Cost. *Organizational Behavior and Human Decision Processes*, 35(1), 124-140. [DOI: 10.1016/0749-5978(85)90049-4](https://doi.org/10.1016/0749-5978(85)90049-4)

**Field experiment**: 60 theater season ticket purchasers randomly assigned full-price ($15), $2-discount, or $7-discount tickets. Full-price purchasers attended significantly more performances (4.11 vs. ~3.3 in first half-season) — the sunk cost drove consumption behavior even though all holders had identical future value.

**Mental accounting mechanism**: Paying for a ticket opens a "theater account." Failing to attend leaves the account closed at a loss (-$15). Attending closes the account with the cost partially "paid off" by consumption. The irrationality: the ticket price is sunk regardless of attendance decision; the marginal decision should be made solely on the marginal utility of attending vs. not attending.

**Generalization**: Any mental account with a debit balance creates pressure to consume/realize value to close the account — even when the marginal utility of that consumption is negative.

### 4.4 Payment Coupling and the Pain of Paying

**Paper**: Prelec & Loewenstein (1998). The Red and the Black: Mental Accounting of Savings and Debt. *Marketing Science*, 17(1), 4-28. [DOI: 10.1287/mksc.17.1.4](https://doi.org/10.1287/mksc.17.1.4)

**Double-entry mental accounting theory**: Consumption generates hedonic benefit; payment generates hedonic cost ("pain of paying"). The degree to which consumption activates thoughts of payment — and vice versa — is **coupling**. High coupling = tight integration of payment pain with consumption pleasure; low coupling = decoupled experiences.

**Key asymmetry** (Prelec & Loewenstein, 1998):

* *Hedonic ideal*: Pain of paying tightly coupled to the payment act, but consumption decoupled from payment pain (consume without the shadow of the bill)
* *Efficiency ideal*: Opposite — consumers should be aware of payment costs during consumption to self-regulate

Credit cards exploit the gap: they temporally separate purchase from payment (reducing coupling at the point of sale) while aggregating many small payments into one large bill (reducing salience of each individual transaction).

**Prepayment effect**: Advance payment decouples payment from consumption in the temporal direction. A prepaid all-inclusive vacation allows consumption without payment pain — the account is already "closed" before arrival. This generates higher consumption rates and satisfaction from prepaid experiences vs. pay-as-you-go.

**Empirical**: Consumers spend more with credit cards than cash across multiple experimental and observational studies (Prelec & Loewenstein, 1998; Prelec & Simester, 2001).

### 4.5 Hedonic Editing in Practice

The four hedonic editing rules (Section 2.3) predict specific behaviors:

| Situation | Rational action | Mental accounting action |
|-----------|----------------|--------------------------|
| Two gains on same day | Combine into one event | Announce separately ("two pieces of good news") |
| Two losses on same day | Announce separately | Combine ("get it all over with") |
| Small gain + large loss | Absorb gain into loss | Announce gain separately ("silver lining") |
| Small loss + large gain | Announce separately | Absorb loss ("minor tax on the windfall") |

These rules are preference-reversals induced by framing; they violate procedure invariance (a normative requirement of rational choice).

---

## 5. Prospect Theory Connection: Formal Mapping

Kahneman & Tversky (1979) established:

1. **Reference dependence**: Utility defined over Δwealth, not absolute wealth
2. **Loss aversion**: v'(x⁻) > v'(x⁺) near origin; λ = |v'(-ε)| / |v'(+ε)| ≈ 2.25
3. **Diminishing sensitivity**: v''(x) < 0 for x > 0 (concave gains); v''(x) > 0 for x < 0 (convex losses)
4. **Probability weighting**: w(p) ≠ p; people overweight small probabilities, underweight large

Mental accounting is the *cognitive architecture* through which prospect theory value functions are applied:

* The *reference point* of v(·) is set by the mental account's baseline (what you paid, what you expected, what you budgeted)
* *Which* transactions get integrated vs. segregated determines whether v(x+y) or v(x)+v(y) is computed
* Account framing determines *which branch* of v(·) is activated (gain vs. loss domain)

Crucially, prospect theory is a theory of *evaluation*; mental accounting is a theory of *organization*. Together they form a complete behavioral model of financial decision-making.

**Disposition effect** (Shefrin & Statman, 1985; Odean, 1998) is a direct joint product: loss aversion (PT) applied within individual stock accounts (MA) → sell winners to "close" profitable accounts, hold losers to avoid realizing losses. Odean (1998) measured PGR = 0.148 vs. PLR = 0.098 — 50% higher realization rate for gains than losses.

---

## 6. Institutional Exploitation of Mental Accounting

### 6.1 Credit Card Architecture

**Mechanism**: Exploit payment decoupling. Cash payment is maximally coupled (immediate, physical, salient). Credit card payment is decoupled: the purchase act is temporally and psychologically separated from the payment event; individual transactions are aggregated into a single bill (reducing per-item salience).

**Effect**: Increased willingness to pay, higher transaction values. The credit card industry monetizes the consumer's reduced pain-of-paying.

**Exploitation vector**: Minimum payment framing. By anchoring the "minimum payment" amount prominently, card issuers exploit anchoring to reduce actual payments made, increasing interest revenue (Thaler, 1999; subsequent regulatory research).

### 6.2 Subscription and Flat-Rate Models

**Flat-rate bias**: Consumers systematically prefer flat-rate pricing (e.g., $50/month unlimited) over pay-per-use that would be cheaper given their actual usage. Mental accounting explanation: flat-rate creates a single, closed mental account at contract signing; variable billing creates ongoing, open accounts with repeated payment pain.

**Decoupling via subscription**: Monthly SaaS charges fade into background mental accounts ("fixed costs"). Each consumption event is decoupled from marginal cost — generating higher usage and satisfaction without per-use payment pain.

**Zero-price effect**: Free tier offerings activate mental accounts with zero baseline; upgrade decisions are then framed as "adding a cost" (loss) rather than "receiving more value for small price" (gain). Freemium models exploit this framing asymmetry to create sticky users who resist upgrading.

### 6.3 Loyalty Programs and Reward Point Currencies

**Mechanism**: Points/miles are a synthetic currency with higher pain-of-paying than cash, but lower loss aversion. Spending points feels less painful than spending cash because:

* Points were "earned" (windfall framing, less real than wages)
* Points exist in a separate mental account from real wealth
* The exchange rate between points and value is opaque (reducing transaction utility calculation)

**Effect**: Higher spending rates in loyalty currencies than in cash equivalents; consumers accept lower-value redemptions (e.g., merchandise at poor point-per-dollar rates) rather than high-value redemptions (cash back).

### 6.4 Casino and Gambling Architecture

Direct house money effect exploitation: chips replace cash, temporally and visually separating money from its real-world value. Winnings are delivered in chips (same currency), creating a single "gambling account" in which losses are absorbed against prior gains. Casino architecture ensures near-continuous play (preventing account closure between sessions).

### 6.5 Bundling and Price Framing

**Segregate gains** (Principle 1): Retailers advertise "FREE shipping + 10% off + extended warranty" as three separate announcements rather than a single bundled discount, maximizing hedonic value.

**Integrate losses** (Principle 2): Car dealerships add features ($500 stereo upgrade, $200 floor mats) after establishing a base price in the $30,000 range — absorbing small losses into the larger purchase.

**Transaction utility exploitation**: "Sale" pricing creates transaction utility even when the pre-sale price was artificially inflated, exploiting the v(p_reference - p_actual) term.

---

## 7. Empirical Evidence Summary

| Phenomenon | Study | Finding | Effect Size |
|-----------|-------|---------|-------------|
| Theater ticket sunk cost | Arkes & Blumer (1985), *Org. Behav. Hum. Dec. Proc.* | Full-price buyers attended 4.11 vs. ~3.3 performances | Not reported as standardized ES |
| House money effect | Thaler & Johnson (1990), *Mgmt Sci* | Increased risk-seeking after prior gains | Confirmed experimentally |
| House money meta-analysis | Frontiers Psych. (2025), 36 studies | g = 0.37 (continuous); RR = 1.33 (binary); pub-bias corrected g ≈ 0.07 | Hedges' g = 0.37; I² = 88.1% |
| Credit card vs. cash spending | Prelec & Simester (2001) | Willingness-to-pay significantly higher with credit cards | Multiple replications |
| Windfall MPC vs. regular income | Multiple studies (cited Thaler 1999) | Higher consumption from small windfalls; decreasing as windfall size increases | Pattern robust |
| Disposition effect (linked to MA) | Odean (1998), *J. Finance* | PGR = 14.8% vs. PLR = 9.8%; 50% asymmetry | Economically significant |
| Fungibility violation (gasoline) | Various (cited Thaler 1999) | Households' gas spending responds to gas price shocks non-fungibly | Rejected H₀ of full fungibility |
| Role integration debiasing | Paul, Parker & Dommer (2023), *J. Marketing Res.* 60(2), 263-277 | Cross-role fund access increases with psychological role integration | Positive intervention effect |
| Debt repayment irrationality | Prelec & Loewenstein (1998), *Mktg Sci* | Savings-debt coexistence explained by account non-fungibility | Theoretical + empirical |

---

## 8. Specific Irrational Behaviors: Formal Analysis

### 8.1 "I'm Broke" While Holding Savings

**Situation**: Person holds S in savings (labeled "emergency fund," mentally sequestered in Future Income account) while carrying D in high-interest debt (Current Income account).

**Rational action**: If r_debt >> r_savings, deplete savings to pay debt up to the point where marginal liquidity value of emergency fund equals the interest rate differential.

**Mental accounting block**: The accounts are non-fungible by label. Accessing "emergency fund" for debt repayment requires reframing the transaction as an account transfer, which closes the emergency fund account (feels like a loss against its reference point) rather than a simple optimization. The pain of closing a "safety" account dominates the rational calculation.

**Magnitude of error**: Credit card at 22% APR vs. savings at 2% APY = 20 percentage point annual wealth destruction. For D = $10,000, this is $2,000/year in pure waste, compounding.

### 8.2 Artificial Fund Categorization

Creating "vacation fund," "home repair fund," "Christmas fund" as separate accounts, often in separate physical containers, when mathematically W = Σᵢ Aᵢ and all have identical opportunity cost. The behavioral function served: mental accounting as a commitment device against hyperbolic discounting — people who cannot commit to saving via pure willpower use labeled accounts as precommitment.

**Important nuance**: Labeled accounts *can* improve welfare if they serve as commitment mechanisms for people with self-control deficits. The irrationality is when the labeling creates cross-account inefficiencies (holding low-return "safe" savings while paying high interest on debt) that a unified account would avoid.

### 8.3 Treating Consumption as Loss

Expenditure on energy, food, insurance is not a loss — it is an exchange: cash → services/goods/utility flows. The reference point error: framing the pre-purchase cash balance as the status quo, making any expenditure a negative deviation from that reference. Rational framing: the reference point is the bundle {cash, expected utility from consumption}; paying for electricity at fair market price is a zero-net-value exchange in expectation.

**Manifestation in trading**: Treating brokerage commissions and bid-ask spread costs as "losses" rather than as the price of market access — causing traders to either overtrade (ignoring frictional costs, treating them as separate accounts) or undertrade (treating each commission as a discrete loss, inducing excessive holding).

---

## 9. Debiasing Strategies from Academic Literature

### 9.1 Fungibility Salience Interventions

**Principle**: Make cross-account opportunity costs explicit and vivid. Instead of seeing a savings account and a credit card as separate objects, present unified net-wealth view.

**Evidence**: Nudges based on proactive interventions reduced drop-off rates for 450,000 clients of a debt consolidation organization by 46% (cited in web search; specific citation TBD).

**Implementation**: Net-worth dashboards that consolidate all accounts, express all balances in common terms, and explicitly show cross-account opportunity costs (e.g., "Your emergency fund earns 2%; your credit card charges 22%; net cost of holding both = $X/month").

### 9.2 Role Integration (Paul, Parker & Dommer, 2023)

**Finding**: Individuals whose life roles (employee, spouse, parent) are psychologically integrated rather than compartmentalized show higher fund fungibility — they are more willing to use funds from one role-specific mental account to service needs of another.

**Intervention implication**: Psychological exercises that reduce role compartmentalization may reduce pathological mental account segregation. Cognitive reframing: "All my money serves all my goals" rather than "Each goal has its dedicated pool."

**Publication**: *Journal of Marketing Research*, 60(2), 263-277.

### 9.3 Temporal Aggregation and Broad Framing

**Principle (Thaler, 1999)**: Evaluating portfolios less frequently (annual vs. daily) reduces the frequency of encountering loss outcomes, reducing the emotional impact of loss aversion. "Myopic loss aversion" (Benartzi & Thaler, 1995) is the combination of loss aversion + frequent evaluation — it explains the equity premium puzzle.

**Implementation**: Deliberately reduce portfolio check frequency; evaluate total portfolio P&L rather than individual position P&L (aggregating accounts reduces segregation-induced loss aversion).

**Benartzi & Thaler (1995)**: *Quarterly Journal of Economics*, 110(1), 73-92. [DOI: 10.2307/2118511](https://doi.org/10.2307/2118511)

### 9.4 Pre-Commitment to Reference Point Rules

Since mental accounting pathologies arise from reference point selection, pre-committing to explicit, rational reference points before positions are established reduces post-hoc reference point manipulation.

**Example**: Write down explicit exit rules (stop-loss at -5%, take-profit at +15%) before entering a trade. The rules set the mental account boundaries at initiation, preventing the reference point drift that causes disposition effect and break-even seeking.

### 9.5 Opportunity Cost Activation

Explicit framing of opportunity costs counteracts mental accounting isolation. Asking "What else could I do with this money?" before each account-specific decision forces integration across accounts.

**Experimental evidence**: Frederick et al. (2009) showed that explicit opportunity cost reminders significantly reduced willingness to pay, demonstrating that normal spending decisions omit opportunity cost consideration.

### 9.6 Implementation in Quantitative/Systematic Trading

For quantitative traders, mental accounting is largely eliminated by:

1. **Portfolio-level PnL tracking only** — no individual position mental accounts
2. **Kelly/fractional Kelly position sizing** — all positions sized by portfolio-level expected value, not by per-trade account logic
3. **Automated rebalancing** — removes human account evaluation timing
4. **Bayesian updating** — explicit probabilistic position revision eliminates reference point anchoring

The 2025 Norges Bank study showed algorithms exhibit significantly weaker disposition effect than human traders (PGR ≈ PLR), consistent with elimination of mental account structures from the decision process.

---

## 10. Key Citations — Complete Reference List

| Citation | Full Reference | DOI |
|---------|----------------|-----|
| **Thaler (1985)** | Thaler RH. Mental Accounting and Consumer Choice. *Marketing Science*, 4(3), 199-214. | [10.1287/mksc.4.3.199](https://doi.org/10.1287/mksc.4.3.199) |
| **Thaler (1999)** | Thaler RH. Mental Accounting Matters. *Journal of Behavioral Decision Making*, 12(3), 183-206. | [10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F](https://doi.org/10.1002/(SICI)1099-0771(199909)12:3%3C183::AID-BDM318%3E3.0.CO;2-F) |
| **Kahneman & Tversky (1979)** | Kahneman D, Tversky A. Prospect Theory: An Analysis of Decision under Risk. *Econometrica*, 47(2), 263-291. | [10.2307/1914185](https://doi.org/10.2307/1914185) |
| **Tversky & Kahneman (1992)** | Tversky A, Kahneman D. Advances in Prospect Theory: Cumulative Representation of Uncertainty. *J. Risk & Uncertainty*, 5(4), 297-323. | [10.1007/BF00122574](https://doi.org/10.1007/BF00122574) |
| **Thaler & Johnson (1990)** | Thaler RH, Johnson EJ. Gambling with the House Money and Trying to Break Even: The Effects of Prior Outcomes on Risky Choice. *Management Science*, 36(6), 643-660. | [10.1287/mnsc.36.6.643](https://doi.org/10.1287/mnsc.36.6.643) |
| **Arkes & Blumer (1985)** | Arkes HR, Blumer C. The Psychology of Sunk Cost. *Organizational Behavior and Human Decision Processes*, 35(1), 124-140. | [10.1016/0749-5978(85)90049-4](https://doi.org/10.1016/0749-5978(85)90049-4) |
| **Prelec & Loewenstein (1998)** | Prelec D, Loewenstein G. The Red and the Black: Mental Accounting of Savings and Debt. *Marketing Science*, 17(1), 4-28. | [10.1287/mksc.17.1.4](https://doi.org/10.1287/mksc.17.1.4) |
| **Shefrin & Statman (1985)** | Shefrin H, Statman M. The Disposition to Sell Winners Too Early and Ride Losers Too Long: Theory and Evidence. *Journal of Finance*, 40(3), 777-790. | [10.2307/2327802](https://doi.org/10.2307/2327802) |
| **Odean (1998)** | Odean T. Are Investors Reluctant to Realize Their Losses? *Journal of Finance*, 53(5), 1775-1798. | [10.1111/0022-1082.00072](https://doi.org/10.1111/0022-1082.00072) |
| **Benartzi & Thaler (1995)** | Benartzi S, Thaler RH. Myopic Loss Aversion and the Equity Premium Puzzle. *Quarterly Journal of Economics*, 110(1), 73-92. | [10.2307/2118511](https://doi.org/10.2307/2118511) |
| **Paul, Parker & Dommer (2023)** | Paul I, Parker JR, Dommer SL. Role Integration Increases the Fungibility of Mentally Accounted Funds. *Journal of Marketing Research*, 60(2), 263-277. | [10.1177/00222437221112058](https://doi.org/10.1177/00222437221112058) |
| **Frontiers Psych. (2025)** | [Authors TBD]. The role of mental accounting in risk-taking and spending: a meta-analysis of the house-money effect. *Frontiers in Psychology*. | [Link](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1549626/full) |

---

## 11. Connections to Repository's Broader Framework

* **Disposition effect** (Odean 1998, Shefrin & Statman 1985): Direct application of mental accounting — each stock position is its own account with an acquisition-price reference point; v(·) applied per-account generates PGR ≠ PLR asymmetry
* **Framing effects** (De Martino et al. 2008): Prospect theory framing operates on the same v(·) function; autism-spectrum individuals' reduced framing susceptibility implies weaker reference-point anchoring → reduced mental accounting distortions
* **Myopic loss aversion** (Benartzi & Thaler 1995): Mental accounting over time horizon → narrow framing of daily returns vs. annual returns → explains equity premium puzzle and excessive risk aversion in asset allocation
* **Anchoring** (Tversky & Kahneman 1974): Acquisition price as anchor sets the reference point for the mental account; price anchoring IS the mechanism by which mental accounts are opened and their reference points set
* **Kelly criterion debiasing**: Portfolio-level expected value optimization (Kelly) is mathematically incompatible with per-position mental accounting — implementing Kelly systematically dissolves individual account structures

---

*Cross-references: [fungibility-asset-transformation-rational-framework.md](fungibility-asset-transformation-rational-framework.md) | [mental-accounting-cognitive-science-parallels.md](mental-accounting-cognitive-science-parallels.md) | [behavioral-biases-multi-paper-synthesis.md](behavioral-biases-multi-paper-synthesis.md) | [BIBLIOGRAPHY.md](../BIBLIOGRAPHY.md) | [KB-ROUTING.md](../KB-ROUTING.md)*

*Philosophical foundations: [spending-as-ontological-error-semiotics-language.md](../ramblings/2026-02-27--spending-as-ontological-error-semiotics-language.md) | [platonic-formalist-economics-beyond-keynesian.md](../ramblings/2026-02-27--platonic-formalist-economics-beyond-keynesian.md) | [artificial-partitioning-work-leisure-watts-krishnamurti.md](../ramblings/2026-02-27--artificial-partitioning-work-leisure-watts-krishnamurti.md)*
