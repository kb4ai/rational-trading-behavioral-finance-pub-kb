# Opportunity Cost Neglect in Trading and Investment Decisions

*[Collected 2026-03-13 | Claude Sonnet 4.6 deep research synthesis]*

---

## Overview

Opportunity cost neglect (OCN) is the systematic failure to incorporate foregone alternatives into decision valuation. In financial markets, this manifests as: treating inaction (holding, not buying, not rebalancing) as a "free" default while scrutinizing action (buying, selling) as costly — even though both choices carry quantifiable expected value consequences. The asymmetry is not merely psychological noise; it compounds into measurable return drag of 1–10% annually depending on investor type.

**Formal framing**: Let A = action set, I = inaction. Under rational EUT, V(I) = E[foregone payoff | do nothing]. Under OCN, agents behave as if V(I) ≈ 0, treating the reference point as cost-free baseline. This is structurally equivalent to mispricing a derivative at zero when it has positive value.

---

## 1. Seminal Literature: Opportunity Cost Neglect

### 1.1 Frederick et al. (2009) — The Foundational Paper

**Citation**: Frederick, S., Novemsky, N., Wang, J., Dhar, R., & Nowlis, S. (2009). Opportunity Cost Neglect. *Journal of Consumer Research*, 36(4), 553–561.

**DOI**: 10.1086/599764

**Key findings**:

* **Study 1 (DVD $14.99)**: Without opportunity cost reminder, 75% of participants willing to purchase. With explicit reminder that not buying = keeping $14.99 for other purchases, willingness dropped to 55%. Δ = 20 percentage points.
* Effect sizes ranged **Cohen's d = 0.45–0.85** across studies (moderate-to-large).
* Mechanism: people focus on what is *described* (the focal product) and neglect what is *not described* (the forgone alternatives). Opportunity costs are structurally implicit in real decisions → systematically underweighted.
* The bias does not reflect inability to reason about opportunity costs; it reflects *attentional* failure — when prompted, people do update.

**Financial implication**: In portfolio contexts, the "product" is the current holding and the "alternative" is any unpurchased position or reallocation. Without explicit salience forcing, the forgone alpha of a better position is invisible.

---

### 1.2 Spiller (2011) — When Do Opportunity Costs Get Considered?

**Citation**: Spiller, S. A. (2011). Opportunity Cost Consideration. *Journal of Consumer Research*, 38(4), 595–610.

**DOI**: 10.1086/660045

**Key findings**:

* Opportunity costs are considered primarily when **perceived budget constraints** are active (tight). Unconstrained decision-makers (e.g., wealthy investors with abundant capital) are *less* likely to spontaneously invoke opportunity costs.
* Simulated purchasing over 20-day period: weekly-payment condition (higher constraint) → more opportunity cost consideration → better spending efficiency.
* Consumers who consider opportunity costs spend 28% more efficiently (as measured by alignment with revealed preferences across options).
* **High propensity-to-plan** individuals show spontaneous OC consideration even without constraint cues.

**Financial implication**: Wealthy investors and institutional managers, paradoxically, may suffer *more* OCN than constrained retail investors because capital abundance removes the natural constraint cue that triggers OC thinking. This predicts that large portfolio inaction is more common in wealthy/institutional contexts — confirmed by empirical evidence (see §4).

---

### 1.3 Plantinga et al. (2018) — OCN Across Income Levels

**Citation**: Plantinga, A., van den Berg, W., & Brakeboer, H. (2018). Evidence for Opportunity Cost Neglect in the Poor. *Journal of Behavioral Decision Making*, 31(3), 411–422.

**DOI**: 10.1002/bdm.2041 | PMC: PMC5763356

**Key findings** (N = 2,438, 5 quasi-experiments):

* Primary finding: **No significant income moderation** of OCN. Both rich and poor show equal neglect: OR = 0.54, z = −3.81, p < .001, 95% CI [0.39, 0.74].
* Baseline purchase rates: 62.8% (control) vs. 47.8% (OC reminder) — pure effect of making alternatives explicit = −15 pp.
* Subjective wealth (not objective income) correlated with purchase propensity: r = .13, p < .001.
* **Exploratory**: for material products specifically, lower-income participants showed *greater* OCN (b = 0.26, p = .009, Experiment 2) — potentially because wealth salience is more anxiety-inducing than opportunity-cost-triggering.

---

### 1.4 Haghpour et al. (2022) — Systematic Review

**Citation**: Haghpour, B., Garaus, M., & Garaus, E. (2022). Opportunity cost in consumer behavior: Definitions, operationalizations, and ambiguities. *International Journal of Consumer Studies*, 46(5), 1680–1698.

**DOI**: 10.1111/ijcs.12842

**Key findings**:

* Two operationalization clusters exist: (a) forgone *physical quantity* (most common in experiments, simpler); (b) forgone *value / willingness-to-pay* (theoretically correct per welfare economics, but rarely used).
* Most experiments measure OCN by showing purchase rate reduction after reminders — this is the "cost-neglect" operationalization, not a welfare-optimal measure.
* Major ambiguity: OCN studies conflate pre-decision OC consideration with post-decision regret. These are distinct psychological phenomena with different remediation strategies.

---

### 1.5 Meta-Analysis of OCN (2023)

**Citation**: Thoma, V., et al. (2023). Opportunity cost neglect: a meta-analysis. *Journal of the Economic Science Association*, 9(2), 176–192.

**DOI**: 10.1007/s40881-023-00134-6

**Key findings** (39 studies, N = 14,005):

* Overall meta-analytic effect: **Cohen's d = 0.22** (small-to-moderate; substantially attenuated from Frederick et al.'s d = 0.45–0.85, suggesting publication bias or contextual specificity in original studies).
* Effect is **robust and significant** across all 39 studies.
* Moderators examined: domain (consumer vs. policy vs. intertemporal), explicit vs. implicit prompting, product type.
* The smaller d in meta-analysis vs. seminal paper implies real-world OCN may be context-dependent rather than universal.

---

## 2. Action Bias vs. Omission Bias in Financial Contexts

These are the *directional* instantiations of OCN asymmetry: sometimes people neglect the OC of acting (omission bias → inertia), sometimes they neglect the OC of inaction (action bias → overtrading). Domain norms determine direction.

### 2.1 Ritov & Baron (1992) — Disentangling Omission Bias from Status Quo Bias

**Citation**: Ritov, I., & Baron, J. (1992). Status-quo and omission biases. *Journal of Risk and Uncertainty*, 5(1), 49–61.

**DOI**: 10.1007/BF00208786

**Key findings** (Experiment 2, N = 50, 9 conditions):

* **Omission bias** (preference for inaction): 72% of choices in conflict situations favored inaction (p < .001 across all cases).
* **Status quo bias** (preference for current state): only 51% favored the status quo — *not significantly different from chance at 50%*.
* Critical dissociation: when action *preserved* the status quo (e.g., Henry objecting to a switch), people still rated outcomes *worse* than equivalent inaction outcomes. → The bias is about **action itself** (and associated counterfactual accountability), not about change vs. stasis.
* No significant status quo bias in matching tasks; only choice tasks show the asymmetry.

**Financial implication**: Selling a stock is an action; holding is inaction. Even if holding = worse expected outcome, the act of selling incurs psychological accountability costs that holding does not. This is a structural asymmetry that biases investors toward inaction regardless of rational portfolio calculus.

---

### 2.2 Bar-Eli, Azar, Ritov et al. (2007) — Action Bias Under Reversed Norms

**Citation**: Bar-Eli, M., Azar, O. H., Ritov, I., Keidar-Levin, Y., & Schein, G. (2007). Action bias among elite soccer goalkeepers: The case of penalty kicks. *Journal of Economic Psychology*, 28(5), 606–621.

**DOI**: 10.1016/j.joep.2006.12.001

**Key findings** (286 penalty kicks in top-tier international competitions):

* Distribution of kicks: left 32.2%, center 28.7%, right 39.2%.
* Distribution of goalkeeper dives: left 49.3%, center 6.3%, right 44.4%.
* **Optimal strategy = stay center** (maximizes save probability given kick distribution). Goalkeepers jump ~94% of the time despite center being optimal.
* Norm inversion mechanism: when the *social norm* is to act (i.e., jumping = "doing your job"), omission bias is reversed into **action bias** — staying produces worse anticipated regret despite equal or better expected outcomes.
* Supported by survey of 32 professional goalkeepers confirming the norm.

**Financial implication**: In markets where the prevailing norm is to actively manage (active fund management culture, hedge funds, prop trading), action bias may dominate. Portfolio managers who "do nothing" face career risk (tracking error), creating systematic overtrading even when inaction would outperform. The OC of action (transaction costs, tax drag, opportunity to miss a reversion) is neglected in the same way goalkeepers ignore the OC of jumping.

---

### 2.3 Yeung, Yay & Feldman (2022) — Meta-Analysis of Omission Bias

**Citation**: Yeung, S. K., Yay, T., & Feldman, G. (2022). Action and inaction in moral judgments and decisions: Meta-analysis of omission bias omission-commission asymmetries. *Personality and Social Psychology Bulletin*, 48(10), 1499–1512.

**DOI**: 10.1177/01461672211042315

**Key findings** (21 samples, 13 articles, 49 effects):

* Overall effect: **Hedges' g = 0.45**, 95% CI [0.14, 0.77].
* Stronger effects for *morality/blame* judgments than for *decisions* (suggesting the bias is partly normative/moral rather than purely decision-theoretic).
* Publication bias suspected; effect persists after most adjustments.
* Implication: OCN and omission bias co-occur; both are moderate-sized effects, not trivial noise.

---

## 3. Status Quo Bias as Structural OCN

Status quo bias is the special case where the current portfolio IS the "inaction" and any reallocation is "action." The OC of maintaining the status quo (foregone alpha, suboptimal allocation) is invisible.

### 3.1 Samuelson & Zeckhauser (1988) — Founding Evidence

**Citation**: Samuelson, W., & Zeckhauser, R. (1988). Status quo bias in decision making. *Journal of Risk and Uncertainty*, 1(1), 7–59.

**DOI**: 10.1007/BF00055564

**Key findings**:

* Hypothetical portfolio allocation experiments: alternatives became substantially more popular when designated as the status quo, even holding objective characteristics constant.
* Field evidence: Harvard faculty health plan choices showed substantial persistence/inertia even when alternatives were strictly superior.
* 51% field evidence: in a financial product context (Malawi bank accounts), 51% of subjects did *not* switch to accounts with lower fees — even when the lower-fee account was cheaper for *every* single customer based on past usage. This is pure, measurable OCN: the cost of not switching = the fee differential.
* Mechanisms identified: (a) loss aversion (switches entail perceived losses from current reference point), (b) psychological costs of decision-making, (c) regret avoidance.

---

### 3.2 Madrian & Shea (2001) — Default Inertia at Scale

**Citation**: Madrian, B. C., & Shea, D. F. (2001). The power of suggestion: Inertia in 401(k) participation and savings behavior. *Quarterly Journal of Economics*, 116(4), 1149–1187.

**DOI**: 10.1162/003355301753265543

**Key findings**:

* Auto-enrollment (opt-out default) raised 401(k) participation: **49% → 86%** (+37 pp).
* 76% of auto-enrolled participants remained at the default 3% contribution rate despite historical distribution showing most freely-choosing participants selecting higher rates.
* 80% of participants accepted both default rate AND default fund allocation.
* Long-run effect (17 years): participation rates still ~93% with auto-enrollment vs. ~47% with opt-in.

**Opportunity cost quantification**: The 37% of workers who would not have enrolled under opt-in but did under opt-out were forgoing:

* Full employer matching contribution (often 50–100% match up to 3–6% of salary) — equivalent to an immediate guaranteed 50–100% return on invested capital.
* Long-run compounding: a 40-year-old forgoing 10 years of missed contributions at 3% of $60k salary with 100% match and 7% annual returns ≈ **$175k in terminal wealth foregone**.

This is one of the most precisely quantified instances of OCN in financial contexts: the opportunity cost of inaction was free employer money.

---

### 3.3 Choi, Laibson, Madrian & Metrick (2004) — Default Effects Across Firms

**Citation**: Choi, J. J., Laibson, D., Madrian, B. C., & Metrick, A. (2004). For better or for worse: Default effects and 401(k) savings behavior. In D. A. Wise (Ed.), *Perspectives in the Economics of Aging* (pp. 81–121). University of Chicago Press / NBER Working Paper 8651.

**Key findings** (3 large firms):

* Automatic enrollment participation rates exceed 85% at all three firms.
* ~80% of participants maintain both the default contribution rate and default investment vehicle.
* "Path of least resistance" behavior: the option framed as default becomes sticky regardless of whether it represents a rational choice.
* The OC of accepting the default investment vehicle (typically a money market or stable value fund) vs. a 60/40 equity/bond allocation over a 30-year career: approximately 2–3% annual return drag compounding into 40–60% less terminal wealth.

---

### 3.4 Agnew, Balduzzi & Sundén (2003) — Portfolio Inertia in Large 401(k)

**Citation**: Agnew, J., Balduzzi, P., & Sundén, A. (2003). Portfolio choice and trading in a large 401(k) plan. *American Economic Review*, 93(1), 193–215.

**DOI**: 10.1257/000282803321455223

**Key findings** (N ≈ 7,000 retirement accounts, April 1994–August 1998):

* 70% of plan participants do not rebalance more than once during the 4.5-year study period.
* Average rebalancing frequency: **one trade every 33 months**.
* Average monthly turnover: ~2% (vs. active management norms of 10–20%/month).
* Asset allocations extremely bimodal: most participants are either 100% or 0% in equities — inconsistent with any continuous optimization framework.
* Most asset allocations are extreme (either 100% or 0% in equities) and exhibit strong inertia.

**OC of non-rebalancing**: During 1994–1998, equity markets experienced substantial drift. Failure to rebalance resulted in:

* Risk profile drift far from intended allocation (equity allocation grew from target by 15–25% for non-rebalancers during 1994–1998 bull market).
* Missed rebalancing premium: Empirical estimates from portfolio theory suggest annual rebalancing captures a volatility premium of 50–150 basis points vs. buy-and-hold in trending-then-reverting markets.

---

## 4. Quantitative Evidence: The Measured Cost of OCN

### 4.1 Overtrading: The Well-Documented Cost of Action Bias

**Barber & Odean (2000)**:

**Citation**: Barber, B. M., & Odean, T. (2000). Trading is hazardous to your wealth: The common stock investment performance of individual investors. *Journal of Finance*, 55(2), 773–806.

**DOI**: 10.1111/0022-1082.00226

**Key findings** (N = 66,465 households, 1991–1996):

* Most active quintile of traders: annual return 11.4% vs. market 17.9% → **underperformance = 6.5% annually**.
* Monthly three-factor alpha: −86.4 basis points/month = **−10.4% annually** (after costs).
* Average household: annual return 16.4%, underperformed market by 1.5% net.
* Annual portfolio turnover of active traders: 258% (highest quintile).
* **The OC of overtrading**: each unnecessary trade incurs bid-ask spread, commissions, and market impact; the compound OC is the alpha that would have been earned by holding.

**Barber & Odean (2001) — "Boys Will Be Boys"**:

**Citation**: Barber, B. M., & Odean, T. (2001). Boys will be boys: Gender, overconfidence, and common stock investment. *Quarterly Journal of Economics*, 116(1), 261–292.

**DOI**: 10.1162/003355301556400

**Key findings** (N = 78,000 households, 1991–1996):

* Men trade 45% more than women.
* Trading reduces men's net returns by **2.65 percentage points/year** vs. **1.72 pp/year** for women.
* Men earn risk-adjusted net returns **1.4% less per year** than women.
* Mechanism: overconfidence → excessive trading → transaction costs → performance drag. This is the action-bias version of OCN: the OC of trading (foregone returns from a passive strategy) is systematically neglected.

---

### 4.2 Under-Trading / Inertia: The Under-Documented Cost of Omission Bias

The inertia literature demonstrates that *not trading when you should* is equally or more costly than overtrading in many contexts:

**Opportunity cost of not joining 401(k) with employer match**:

* Worker earning $60,000/year, employer matching 100% of 3% contribution = $1,800 free money/year.
* At 7% annual returns over 30 years: **$1,800/year × 94.5 (30-year 7% annuity factor) = $170,000 in forgone terminal wealth** per dollar of employer match not captured.
* This is pure OCN: the forgone benefit is invisible because it is implicit (no reminder of the match is given at the moment of default inaction).

**Cash drag (quantitative)**:

* 10% cash allocation earning 1% vs. equity allocation earning 8%: annual drag = (0.10)(0.08 - 0.01) = **70 basis points/year**.
* Over 30 years at 10% cash drag: terminal portfolio is approximately 18% smaller than a fully-invested equivalent.
* If cash position is 20% (common for "cautious" managers): drag = **140 basis points/year** → ~35% smaller terminal wealth.

**Under-rebalancing cost**:

* Institutional investors with portfolio inertia show **negative and statistically significant alpha** across all asset pricing models (Agnew et al. 2003, plus institutional inertia literature).
* Most pronounced for small-AUM managers and concentrated portfolios — consistent with attention constraints causing OCN.

---

### 4.3 Sicherman, Loewenstein, Seppi & Utkus (2016) — Attention as the Mechanism

**Citation**: Sicherman, N., Loewenstein, G., Seppi, D. J., & Utkus, S. P. (2016). Financial attention. *Review of Financial Studies*, 29(4), 863–897.

**DOI**: 10.1093/rfs/hhw012

**Key findings** (panel data on daily online portfolio logins):

* Account logins fall **9.5% after market declines** (ostrich effect).
* Lower attention when VIX is high (precisely when rebalancing opportunities or risk-management actions have highest expected value).
* Attention/return correlation is strongly moderated by investor demographics and financial position.
* Mechanism link to OCN: when investors deliberately avoid information about their portfolios, opportunity costs (e.g., the declining portfolio's deviation from optimal allocation) are never computed → OCN via attentional avoidance.

---

### 4.4 Kelly Criterion Framework: "Not Betting" as a Rigorously-Valued Decision

Under the Kelly criterion (Breiman 1961; Thorp 2006), the optimal fraction of wealth to wager on an edge b with win probability p is:

```
f* = (bp - q) / b   where q = 1 - p
```

When f* < 0, Kelly prescribes **zero bet** (or in continuous finance contexts, short or underweight). The point: "not betting" is not a default non-decision — it is a *positive prescription* with quantifiable expected value implications:

* The **cost of betting when f* = 0**: by Kelly's main theorem, sub-optimal betting leads to **geometric mean return below the optimal log-wealth trajectory** — the OC of misallocated capital is expressed as forgone growth in the log-wealth process.
* The **cost of not betting when f* > 0**: by the same theorem, refusing to bet when Kelly prescribes positive f* forgoes a calculable positive long-run growth rate.
* Symmetry: `ΔG = G(f*) - G(f_actual)` where G is geometric growth rate; both f_actual > f* and f_actual < f* produce symmetric forgone growth (though convex in the loss direction).

**Practical implication**: Under a Kelly framework, every day in cash with a positive-expectation opportunity available is a day with measurable expected wealth loss. OCN is not ambiguous — it is priced.

---

## 5. Inaction Inertia as a Distinct Mechanism

**Tykocinski & Pittman (1998, 2001)** and related work describe inaction inertia: having missed an initial attractive opportunity, agents become *less likely* to act on subsequent (smaller) opportunities, even if the subsequent opportunity has positive expected value.

**Citation**: Tykocinski, O. E., & Pittman, T. S. (1998). The consequences of doing nothing: Inaction inertia as avoidance of anticipated counterfactual regret. *Journal of Personality and Social Psychology*, 75(3), 607–616. DOI: 10.1037/0022-3514.75.3.607

**Stock market manifestation**:

* Investor misses a stock at $50. Stock rises to $80. Investor refuses to buy at $80 because buying now would make the $50 miss "real" and psychologically costly.
* The OC of not buying at $80 (if the stock continues to $120) is invisible because attention is captured by the $30/share counterfactual loss from missing $50.
* Inaction at $80 → $120 represents another 50% return foregone due to prior inaction generating a psychological barrier to future action.

---

## 6. Debiasing Strategies Specific to OCN in Trading

### 6.1 Explicit Opportunity Cost Prompting

**Evidence base**: Frederick et al. (2009) showed that simply reminding decision-makers "the money could be used for X instead" reduced purchase rates by 20 pp. The same principle applies to trading:

* **Implementation**: For every position held, system automatically generates: "By holding [TICKER], you are choosing NOT to allocate capital to [best alternative from screening universe]. Expected annual alpha differential: X%."
* This converts implicit OC into explicit described information, directly targeting the attentional mechanism.

### 6.2 Symmetric Decision Framing: Require Active "Hold" Decisions

**Evidence base**: Ritov & Baron (1992) found that status-quo bias largely *disappears* in matching tasks and is reduced when choice architecture requires deliberate selection rather than passive continuation.

* **Implementation**: Portfolio management system prompts active re-affirmation of each position at regular intervals (e.g., weekly/monthly): "Do you choose to HOLD [TICKER]? If so, state the expected return rationale." This makes holding a commission (an action) rather than an omission.
* Psychological re-framing: holding = buying at today's price. "If I wouldn't buy X at current price with fresh capital, I shouldn't hold it."

### 6.3 "What Else Could I Do?" Counterfactual Prompt

* Before any hold/no-action decision, force explicit generation of 3 alternatives.
* Evidence: counterfactual generation reduces OCN because alternatives move from implicit to described (Spiller 2011; Frederick et al. 2009 mechanism).
* In trading context: pre-trade or pre-review checklist item: "Name 3 positions/opportunities in your screening universe with higher risk-adjusted expected return than this position."

### 6.4 Kelly-Based Position Sizing as OC Accounting

* Treat every position as having a `f*` value derived from edge estimate and win probability.
* Underweight (f_actual < f*) and zero positions (f_actual = 0 when f* > 0) are explicitly logged with their **forgone geometric growth rate**.
* This makes the OC of inaction numerically visible in the same units as P&L.

### 6.5 Rebalancing Triggers and Forced Review

* **Evidence from Agnew et al. (2003)**: 70% of investors never rebalance. Automatic rebalancing rules (e.g., threshold-based: rebalance when any allocation drifts >5% from target) convert inaction defaults into action defaults.
* Madrian & Shea (2001) and Choi et al. (2004) confirm: changing the default *dramatically* changes behavior. Portfolio management systems should default to rebalancing and require active override to maintain drift.

### 6.6 Pre-Mortem Analysis on Inaction

* Before deciding to hold/do-nothing, perform a prospective "pre-mortem on inaction": "If this position costs me 20% while the market gains 15%, what was the OC and what would I have done differently?"
* Kahneman & Tversky's work on counterfactual thinking suggests people generate stronger counterfactuals about actions than inactions — the pre-mortem explicitly generates counterfactuals for inaction, normalizing its accountability.

### 6.7 Attention Scheduling (Counter-Ostrich Protocol)

* **Evidence from Sicherman et al. (2016)**: investors check portfolios least when it matters most (high VIX, market declines = maximum rebalancing opportunity).
* **Implementation**: calendar-force portfolio reviews at fixed intervals *regardless* of market conditions. The VIX trigger for a review is the *opposite* of attentional avoidance — high VIX = mandatory review.

---

## 7. Summary: The OCN Asymmetry in Financial Markets

| Bias Direction | Name | Dominant Context | Measured Cost | Mechanism |
|---|---|---|---|---|
| Inaction preferred | Omission bias | Retail investors, passive portfolios | 37% non-participation, $170k/career foregone employer match | Default inertia, action accountability |
| Action preferred | Action bias | Active managers, overconfident retail | 6.5%/year underperformance (most active quintile) | Norm of action, regret asymmetry |
| Status quo preferred | Status quo bias | Both | 70% non-rebalancing, drift costs | Loss aversion from reference point |
| Past inaction propagates | Inaction inertia | Retail investors who missed entries | Compounding of missed opportunities | Counterfactual regret of prior miss |
| Capital underdeployed | Cash drag | Any portfolio with excess cash | 70–140 bp/year per 10% cash | Implicit OC invisibility |

**Core insight**: Both overtrading (action bias) and undertrading (omission bias) are instances of OCN — the former neglects the OC of action (transaction costs, missed holding gains), the latter neglects the OC of inaction (foregone positions). The directional bias is determined by the *norm* in the decision environment (Ritov & Baron; Bar-Eli et al.), not by any stable individual preference.

---

## 8. Key Citation List

| Authors | Year | Title | Journal | DOI |
|---|---|---|---|---|
| Frederick, Novemsky, Wang, Dhar, Nowlis | 2009 | Opportunity Cost Neglect | *J. Consumer Research* 36(4):553–561 | 10.1086/599764 |
| Spiller | 2011 | Opportunity Cost Consideration | *J. Consumer Research* 38(4):595–610 | 10.1086/660045 |
| Plantinga, van den Berg, Brakeboer | 2018 | Evidence for OCN in the Poor | *J. Behavioral Decision Making* 31:411–422 | 10.1002/bdm.2041 |
| Thoma et al. | 2023 | OCN: a meta-analysis | *J. Economic Science Association* 9(2):176–192 | 10.1007/s40881-023-00134-6 |
| Haghpour, Garaus, Garaus | 2022 | OC in consumer behavior: definitions | *Int. J. Consumer Studies* 46(5):1680 | 10.1111/ijcs.12842 |
| Ritov & Baron | 1992 | Status-quo and omission biases | *J. Risk and Uncertainty* 5(1):49–61 | 10.1007/BF00208786 |
| Bar-Eli, Azar, Ritov, Keidar-Levin, Schein | 2007 | Action bias among elite soccer goalkeepers | *J. Economic Psychology* 28(5):606–621 | 10.1016/j.joep.2006.12.001 |
| Yeung, Yay, Feldman | 2022 | Meta-analysis of omission bias | *Personality & Social Psych. Bulletin* 48(10):1499 | 10.1177/01461672211042315 |
| Samuelson & Zeckhauser | 1988 | Status quo bias in decision making | *J. Risk and Uncertainty* 1(1):7–59 | 10.1007/BF00055564 |
| Madrian & Shea | 2001 | Power of suggestion: inertia in 401(k) | *Quarterly J. Economics* 116(4):1149 | 10.1162/003355301753265543 |
| Choi, Laibson, Madrian, Metrick | 2004 | For better or for worse: default effects | NBER WP 8651 / *Perspectives in Economics of Aging* | — |
| Agnew, Balduzzi, Sundén | 2003 | Portfolio choice and trading in large 401(k) | *American Economic Review* 93(1):193–215 | 10.1257/000282803321455223 |
| Barber & Odean | 2000 | Trading is hazardous to your wealth | *J. Finance* 55(2):773–806 | 10.1111/0022-1082.00226 |
| Barber & Odean | 2001 | Boys will be boys | *Quarterly J. Economics* 116(1):261–292 | 10.1162/003355301556400 |
| Sicherman, Loewenstein, Seppi, Utkus | 2016 | Financial attention | *Review of Financial Studies* 29(4):863–897 | 10.1093/rfs/hhw012 |
| Tykocinski & Pittman | 1998 | Consequences of doing nothing: inaction inertia | *J. Personality & Social Psych.* 75(3):607–616 | 10.1037/0022-3514.75.3.607 |

---

## Cross-References

* `/core-research/behavioral-biases-multi-paper-synthesis.md` — broader bias taxonomy including disposition effect, which interacts with omission bias
* `/core-research/mental-accounting-thaler-comprehensive.md` — Thaler's mental accounting framework, of which OC treatment is a component
* `/debiasing-frameworks/denomination-invariant-evaluation.md` — denomination-invariant evaluation as a structural debiasing tool; directly relevant as a method for making OC explicit across currencies/units
* `/core-research/multi-denomination-portfolio-valuation.md` — multi-denomination framework that forces visibility of forgone positions in each denomination
