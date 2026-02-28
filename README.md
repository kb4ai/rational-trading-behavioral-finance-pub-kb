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

**The Debiasing Solutions:**

* **Kelly Criterion** - Mathematically optimal position sizing: f* = (bp - q) / b. Use Half-Kelly for reduced volatility.
* **Systematic Rebalancing** - Calendar or threshold-based rules that enforce buy-low/sell-high mechanically.
* **State-Space Formulation** - Portfolio optimization as pure MDP where historical entry prices never enter state representation.
* **Pre-commitment Devices** - Automatic stop-losses, take-profit orders, written decision trees.
* **Bayesian Updating** - Formal structure for incorporating new information without overweighting recent data.

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

## Navigation

* **[KB-ROUTING.md](KB-ROUTING.md)** — Full document index, research sources by AI provider, bias taxonomy, debiasing frameworks, cross-KB navigation
* **[BIBLIOGRAPHY.md](BIBLIOGRAPHY.md)** — Central reference for all 55+ academic papers with DOI links and cross-reference index

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

## Status

**WIP** — Core research and philosophical foundations complete. Debiasing implementation guides and market microstructure analysis pending.

---

*This repository applies quantitative rigor to behavioral finance, targeting readers who approach trading as applied mathematics and game theory.*
