# Rational Trading & Behavioral Finance

> **Mathematical frameworks for eliminating cognitive biases from portfolio decisions**

[Collected 2025-01-22]

## TL;DR

**The 5 Biases That Destroy Trading Performance:**

1. **Disposition Effect** - Selling winners too early, holding losers too long. Costs ~4-6% annually. Measured by PGR/PLR ratio (14.8% vs 9.8% in Odean's study).

2. **[Anchoring](https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias))/Reference Dependence** - Entry price contaminating forward-looking decisions. The purchase price is mathematically irrelevant to optimal future action.

3. **[Loss Aversion](https://en.wikipedia.org/wiki/Loss_aversion)** - Losses felt ~2.25x more intensely than equivalent gains. Creates asymmetric risk preferences that violate stochastic dominance.

4. **[Sunk Cost Fallacy](https://yourlogicalfallacyis.com/sunk-cost)** - Continuing to hold (or add to) losing positions because of resources already committed. Entry price is sunk cost with zero information content.

5. **[Confirmation Bias](https://en.wikipedia.org/wiki/Confirmation_bias)** - 85% of investors disposed to accepting confirming opinions. Creates echo chambers where flawed theses go unchallenged.

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
* See also: [Multi-paper synthesis](core-research/behavioral-biases-multi-paper-synthesis.md) covering 7 foundational studies (De Martino, Grinblatt, Odean, Barber & Odean, Thaler, Samuelson & Zeckhauser, Yafai)
* **[Full Bibliography](BIBLIOGRAPHY.md)** — Central reference for all 30+ academic papers cited in this knowledge base with DOI links

**Key Insight:** Awareness alone is insufficient. Knowing about biases does not prevent them. Only systems that mechanically override human intuition can achieve rational outcomes.

## Directory Structure

```
rational-trading-behavioral-finance-pub-kb/
├── README.md                    # This file
├── KB-ROUTING.md                # Navigation & cross-references
├── BIBLIOGRAPHY.md              # Central academic paper references
├── CLAUDE.md                    # AI assistant instructions
├── core-research/               # Synthesized key findings
│   ├── de-martino-2008-framing-effects-autism-explained.md
│   └── behavioral-biases-multi-paper-synthesis.md
├── debiasing-frameworks/        # Mathematical solutions
├── market-microstructure/       # Institutional exploitation patterns
├── research-artifacts/          # Original AI research outputs
│   ├── claude-opus-4-5-deep-research.md
│   ├── claude-opus-4-5-deep-research-with-clarifications.md
│   ├── perplexity-deep-research.md
│   ├── chatgpt-5.2-deep-research.md
│   ├── chatgpt deep research *.pdf/docx
│   └── prompts/                 # Original research prompts
└── ramblings/                   # Development notes
```

## Research Sources

| Provider | Model/Service | Focus | File |
|----------|---------------|-------|------|
| Claude | Opus 4.5 | Cognitive architecture of trading failure | [claude-opus-4-5-deep-research.md](research-artifacts/claude-opus-4-5-deep-research.md) |
| Claude | Opus 4.5 | Quantitative framework for rational exploitation | [claude-opus-4-5-deep-research-with-clarifications.md](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md) |
| Perplexity | Deep Research | Neurodivergent advantage, institutional exploitation | [perplexity-deep-research.md](research-artifacts/perplexity-deep-research.md) |
| ChatGPT | 5.2 Deep Research | Cognitive/emotional biases in retail trading | [chatgpt-5.2-deep-research.md](research-artifacts/chatgpt-5.2-deep-research.md) |
| ChatGPT | 5.2 | Multi-paper synthesis: 7 foundational behavioral bias studies | [behavioral-biases-multi-paper-synthesis.md](core-research/behavioral-biases-multi-paper-synthesis.md) |

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

## Cross-References

* **Cognitive Science:** See `cognitive-kb/` for neuroscience foundations
* **Formal Methods:** Mathematical frameworks in `formal-methods-kb/`
* **Related Markets:** Private credit analysis in `financial-markets-kb/private-credit-markets-pub-kb/`

## Status

**WIP** - Core research complete, synthesis documents pending development.

## External Resources

### Logical Fallacies & Cognitive Biases

These reference sites provide comprehensive catalogs of logical fallacies and cognitive biases—many directly applicable to trading discourse and market narratives:

* **[Your Logical Fallacy Is](https://yourlogicalfallacyis.com/)** — Visual poster-style reference for common logical fallacies. Particularly relevant: [sunk cost](https://yourlogicalfallacyis.com/sunk-cost), [appeal to authority](https://yourlogicalfallacyis.com/appeal-to-authority), [anecdotal](https://yourlogicalfallacyis.com/anecdotal), [the gambler's fallacy](https://yourlogicalfallacyis.com/the-gamblers-fallacy)
* **[List of Fallacies (Wikipedia)](https://en.wikipedia.org/wiki/List_of_fallacies)** — Comprehensive taxonomy of formal and informal logical fallacies
* **[Cognitive Biases (Wikipedia)](https://en.wikipedia.org/wiki/Cognitive_bias)** — Overview and categorization of systematic cognitive biases; see also the [List of Cognitive Biases](https://en.wikipedia.org/wiki/List_of_cognitive_biases) for exhaustive catalog

### Key Fallacy-Bias Mappings for Trading

| Trading Pattern | Related Fallacy/Bias | Reference |
|-----------------|---------------------|-----------|
| "It has to come back" | [Gambler's Fallacy](https://yourlogicalfallacyis.com/the-gamblers-fallacy) | Independent events treated as dependent |
| "I've held this long, can't sell now" | [Sunk Cost Fallacy](https://yourlogicalfallacyis.com/sunk-cost) | Past costs affecting future decisions |
| "This guru predicted the last crash" | [Appeal to Authority](https://yourlogicalfallacyis.com/appeal-to-authority) | Expert opinion ≠ truth |
| "My friend made 10x on crypto" | [Anecdotal Evidence](https://yourlogicalfallacyis.com/anecdotal) | Survivorship-biased samples |
| "Markets fell because of [news]" | [Post Hoc](https://yourlogicalfallacyis.com/false-cause) | Correlation ≠ causation |
| "Either HODL or you're weak" | [False Dilemma](https://yourlogicalfallacyis.com/black-or-white) | Excluding rational middle ground |

---

*This repository applies quantitative rigor to behavioral finance, targeting readers who approach trading as applied mathematics and game theory.*
