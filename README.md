# Rational Trading & Behavioral Finance

> **Mathematical frameworks for eliminating cognitive biases from portfolio decisions**

[Initiated 2026-01-22, ongoing — see commit history]

## TL;DR

**The 6 Biases That Destroy Trading Performance:**

1. **Disposition Effect** - Selling winners too early, holding losers too long. Costs ~4-6% annually. Measured by PGR/PLR ratio (14.8% vs 9.8% in Odean's study).

2. **[Anchoring](https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias))/Reference Dependence** - Entry price contaminating forward-looking decisions. The purchase price is mathematically irrelevant to optimal future action.

3. **[Loss Aversion](https://en.wikipedia.org/wiki/Loss_aversion)** - Losses felt ~2.25x more intensely than equivalent gains. Creates asymmetric risk preferences that violate stochastic dominance.

4. **[Sunk Cost Fallacy](https://yourlogicalfallacyis.com/sunk-cost)** - Continuing to hold (or add to) losing positions because of resources already committed. Entry price is sunk cost with zero information content.

5. **[Confirmation Bias](https://en.wikipedia.org/wiki/Confirmation_bias)** - 85% of investors disposed to accepting confirming opinions. Creates echo chambers where flawed theses go unchallenged.

6. **[Mental Accounting](https://en.wikipedia.org/wiki/Mental_accounting)** - Labeling money into non-fungible "accounts" (savings, spending, emergency) when mathematically W_total = Σ assets. Causes 20pp/year wealth destruction (holding 2% savings while carrying 22% debt). "Spending" is actually asset transformation (cash → goods → utility), not loss. [Comprehensive analysis](core-research/mental-accounting-thaler-comprehensive.md) | [Rational framework](core-research/fungibility-asset-transformation-rational-framework.md)

7. **[Single-Denominator Bias](https://en.wikipedia.org/wiki/Money_illusion)** - Evaluating portfolio in one unit of account (USD, BTC, gold) when the denomination choice is itself a frame that distorts perception. 60-80% evaluate nominally (Shafir et al., 1997); 15-30% spending errors from face value anchoring (Raghubir & Srivastava, 2002). A portfolio +15% in USD but -8% in BTC is the *same state* with two contradictory narratives. The denomination frame can flip the disposition effect's direction. [Core framework](core-research/multi-denomination-portfolio-valuation.md) | [Debiasing protocol](debiasing-frameworks/denomination-invariant-evaluation.md) | [Python implementation](debiasing-frameworks/examples/multi-denomination-tracker.py)

8. **[Omission Bias](https://en.wikipedia.org/wiki/Omission_bias) / [Opportunity Cost Neglect](https://doi.org/10.1086/599764)** - Treating "hold" / "do nothing" as a costless default when it carries quantifiable opportunity cost. 72% prefer harmful inaction over equivalent harmful action (Ritov & Baron, 1992). Forgone alternatives are systematically underweighted because they're implicit, not described (Frederick et al., 2009: 20pp purchase-rate shift when OC made explicit, d=0.45–0.85). Both overtrading (−6.5%/yr, Barber & Odean 2000) and under-trading ($170k/career missed 401k match) are OCN — the neglected OC differs. Inaction inertia compounds: missed entry at $50 → psychological barrier at $80 → misses $80→$120 run (Tykocinski, 2004). **Stoic philosophy** (Epictetus's prohairesis) treats every non-action as an exercise of rational will requiring equal scrutiny; Sartre: "not deciding" is bad faith concealing continuous choice. [OCN analysis](core-research/opportunity-cost-neglect-in-trading.md) | [Omission/inaction empirics](core-research/omission-status-quo-inaction-inertia-trading.md) | [Stoic framework](core-research/stoic-inaction-as-action-framework.md) | [Symmetric evaluator](debiasing-frameworks/symmetric-action-inaction-evaluator.md)

**The Debiasing Solutions:**

* **Kelly Criterion** - Mathematically optimal position sizing: f* = (bp - q) / b. Use Half-Kelly for reduced volatility.
* **Systematic Rebalancing** - Calendar or threshold-based rules that enforce buy-low/sell-high mechanically.
* **State-Space Formulation** - Portfolio optimization as pure MDP where historical entry prices never enter state representation.
* **Pre-commitment Devices** - Automatic stop-losses, take-profit orders, written decision trees.
* **Bayesian Updating** - Formal structure for incorporating new information without overweighting recent data.
* **Denomination-Invariant Evaluation** - Evaluate portfolio value simultaneously in N denominations (USD, BTC, gold, CPI). The min-growth metric G(t₀,t₁) = min_d{V_d(t₁)/V_d(t₀)} mechanically overrides subjective denomination preference. If G > 1, growth is genuine across all frames. [Framework](debiasing-frameworks/denomination-invariant-evaluation.md)
* **Symmetric Action-Inaction Evaluator** - Treats "hold" as a first-class action with its own cost function: C(hold) = opportunity_cost + drift_from_optimal + option_value_decay. The Reversal Test (Bostrom & Ord 2006): "Would I buy this position today?" If No → holding is status quo bias. Integrates Kelly growth-rate accounting for inaction, real options theory for rational waiting, and minimax regret across N dimensions. [Framework](debiasing-frameworks/symmetric-action-inaction-evaluator.md)

**The Neurodivergent Advantage:**

* Autistic individuals show 65-80% reduced susceptibility to framing effects ([De Martino et al., 2008](https://doi.org/10.1523/JNEUROSCI.2895-08.2008)) — [detailed explanation](core-research/de-martino-2008-framing-effects-autism-explained.md)
* High-IQ investors achieve 4.9% higher annual returns through reduced disposition effect and superior market timing ([Grinblatt et al., 2012](https://doi.org/10.1016/j.jfineco.2011.05.016))
* Algorithms exhibit virtually zero disposition effect vs. human traders' 15-20pp gap
* See also: [Multi-paper synthesis](core-research/behavioral-biases-multi-paper-synthesis.md) | [Cognitive science parallels](core-research/mental-accounting-cognitive-science-parallels.md)

**Key Insight:** Awareness alone is insufficient. Knowing about biases does not prevent them. Only systems that mechanically override human intuition can achieve rational outcomes.

## The Deeper Thesis: Beyond "Bias Correction"

Standard behavioral economics says: *"Humans are biased. Here's how to fix them."*

This repository develops a stronger claim: **the mathematical description is the ground truth. Human experience is the distortion.**

"Spending" is not merely a biased frame — it is an [ontological category error](ramblings/2026-02-27--spending-as-ontological-error-semiotics-language.md) baked into language itself. The word *expendere* (Latin: "to weigh out") encodes unidirectional destruction of a substance. What actually happens in exchange is a bidirectional morphism — a structure-preserving transformation where total value is conserved, merely rearranged. Category theory, not psychology, provides the [corrective ontology](core-research/fungibility-asset-transformation-rational-framework.md).

This same partitioning error — imposing artificial boundaries on continuous flows — appears across domains:

* **Savings vs. spending** → money is one fungible resource; labels carry zero information
* **Work vs. leisure** → [the same structural error](ramblings/2026-02-27--artificial-partitioning-work-leisure-watts-krishnamurti.md), diagnosed by Watts, Krishnamurti, Csikszentmihalyi, Heidegger, Illich, and Graeber
* **Gains vs. losses** → prospect theory's reference-dependent framing of what are, mathematically, portfolio state transitions

The [philosophical landscape](ramblings/2026-02-27--platonic-formalist-economics-beyond-keynesian.md) maps where this framework sits: modified mathematical Platonism in the Debreu tradition, with Georgescu-Roegen's thermodynamic realism (conservation law as physical constraint) and Veblen's insight that economic categories are "habits of thought," not natural kinds.

Visual/pattern thinkers and autistic cognitive profiles show [structural immunity](ramblings/2026-02-27--spending-as-ontological-error-semiotics-language.md#6-visual-thinking-vs-linguistic-thinking) to the category error because they bypass the verbal representation where the error lives (Grandin 2022, Rozenkrantz et al. 2021, Paivio dual coding theory).

## Key Concepts

### Mathematical Irrelevance of Entry Prices

The optimal portfolio rebalancing problem at time t is:

```
max E[U(W_{t+1})] subject to constraints
```

**Historical entry prices P₀ do not appear in this function.** They are sunk costs conveying zero information about future probability distributions.

### The "Neurotypical Tax"

Behavioral biases function as wealth transfer mechanisms from neurotypical retail to algorithmic/institutional actors. High-IQ investors avoid ~5% annual "neurotypical tax" through:

* Pure cognitive edge (avoiding biases): +2.2% annually
* Market timing from rational discipline: +2.7% annually

### Linguistic Markers of Biased Reasoning

**Red flags:**

* "I'm underwater on this position" - reference point fixation
* "Waiting to get back to even" - anchoring + sunk cost
* "Diamond hands" / "Paper hands" - identity-linked bias
* "Averaging down" - commitment escalation
* "It has to come back" - [mean reversion fallacy](https://yourlogicalfallacyis.com/the-gamblers-fallacy)
* "I'm broke" (while holding savings) - mental accounting partition creating artificial scarcity
* "I have to dip into my life savings" - as though prior expenditures came from a different owner
* "I spent all my money" - framing asset transformation (cash → goods) as destruction
* "I'm up in USD!" - denomination bias hiding BTC/gold-denominated losses
* "My BTC stack is growing" - single-denominator view masking purchasing power decline
* "I haven't decided to sell yet" - Sartrean bad faith: concealing continuous hold-decision as non-decision
* "I missed the entry at $X, can't buy now" - inaction inertia: prior miss blocking positive-EV action
* "I'm just holding, not doing anything" - omission bias: treating inaction as costless default
* "I'll think about it later" - opportunity cost neglect: implicit alternatives invisible

## Navigation

* **[KB-ROUTING.md](KB-ROUTING.md)** — Full document index, research sources by AI provider, bias taxonomy, debiasing frameworks, cross-KB navigation
* **[BIBLIOGRAPHY.md](BIBLIOGRAPHY.md)** — Central reference for all 55+ academic papers with DOI links and cross-reference index

### For Quantitative Traders

* **[Quant Models of Inaction Cost](core-research/quant-models-inaction-cost-systematic-trading.md)** — The full formal-model treatment: Almgren-Chriss execution frontier, Perold IS decomposition, Davis-Norman no-trade zone (formula for band width), Garleanu-Pedersen aim portfolio (closed-form optimal trading rate), alpha decay empirics (5.6% US / 9.9% EU annual cost of delay), RL portfolio management, momentum alpha supply, Kelly under-betting cost, Renaissance/AQR/López de Prado practitioner perspectives. This is the most important document for the target audience.

## External Resources

### Logical Fallacies & Cognitive Biases

* **[Your Logical Fallacy Is](https://yourlogicalfallacyis.com/)** — Visual poster-style reference. Particularly relevant: [sunk cost](https://yourlogicalfallacyis.com/sunk-cost), [appeal to authority](https://yourlogicalfallacyis.com/appeal-to-authority), [anecdotal](https://yourlogicalfallacyis.com/anecdotal), [the gambler's fallacy](https://yourlogicalfallacyis.com/the-gamblers-fallacy)
* **[List of Fallacies (Wikipedia)](https://en.wikipedia.org/wiki/List_of_fallacies)** — Comprehensive taxonomy of formal and informal logical fallacies
* **[Cognitive Biases (Wikipedia)](https://en.wikipedia.org/wiki/Cognitive_bias)** — Overview and categorization; see also the [full list](https://en.wikipedia.org/wiki/List_of_cognitive_biases)

### Key Fallacy-Bias Mappings for Trading

| Trading Pattern | Related Fallacy/Bias | Reference |
|-----------------|---------------------|-----------|
| "It has to come back" | [Gambler's Fallacy](https://yourlogicalfallacyis.com/the-gamblers-fallacy) | Independent events treated as dependent |
| "I've held this long, can't sell now" | [Sunk Cost Fallacy](https://yourlogicalfallacyis.com/sunk-cost) | Past costs affecting future decisions |
| "This guru predicted the last crash" | [Appeal to Authority](https://yourlogicalfallacyis.com/appeal-to-authority) | Expert opinion ≠ truth |
| "My friend made 10x on crypto" | [Anecdotal Evidence](https://yourlogicalfallacyis.com/anecdotal) | Survivorship-biased samples |
| "Markets fell because of [news]" | [Post Hoc](https://yourlogicalfallacyis.com/false-cause) | Correlation ≠ causation |
| "Either HODL or you're weak" | [False Dilemma](https://yourlogicalfallacyis.com/black-or-white) | Excluding rational middle ground |
| "I'm not doing anything, just holding" | [Omission Bias](https://en.wikipedia.org/wiki/Omission_bias) | Inaction ≠ neutral; holding is active choice |
| "I missed the dip, too late now" | [Inaction Inertia](https://doi.org/10.1037/0022-3514.75.3.607) | Prior miss blocking current positive-EV action |

## Status

**WIP** — Core research, philosophical foundations, denomination-invariant evaluation, and symmetric action-inaction evaluation frameworks complete. Market microstructure analysis pending.

---

*This repository applies quantitative rigor to behavioral finance, targeting readers who approach trading as applied mathematics and game theory.*
