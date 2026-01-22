# Rational Trading & Behavioral Finance

> **Mathematical frameworks for eliminating cognitive biases from portfolio decisions**

[Collected 2025-01-22]

## TL;DR

**The 5 Biases That Destroy Trading Performance:**

1. **Disposition Effect** - Selling winners too early, holding losers too long. Costs ~4-6% annually. Measured by PGR/PLR ratio (14.8% vs 9.8% in Odean's study).

2. **Anchoring/Reference Dependence** - Entry price contaminating forward-looking decisions. The purchase price is mathematically irrelevant to optimal future action.

3. **Loss Aversion** - Losses felt ~2.25x more intensely than equivalent gains. Creates asymmetric risk preferences that violate stochastic dominance.

4. **Sunk Cost Fallacy** - Continuing to hold (or add to) losing positions because of resources already committed. Entry price is sunk cost with zero information content.

5. **Confirmation Bias** - 85% of investors disposed to accepting confirming opinions. Creates echo chambers where flawed theses go unchallenged.

**The Debiasing Solutions:**

* **Kelly Criterion** - Mathematically optimal position sizing: f* = (bp - q) / b. Use Half-Kelly for reduced volatility.
* **Systematic Rebalancing** - Calendar or threshold-based rules that enforce buy-low/sell-high mechanically.
* **State-Space Formulation** - Portfolio optimization as pure MDP where historical entry prices never enter state representation.
* **Pre-commitment Devices** - Automatic stop-losses, take-profit orders, written decision trees.
* **Bayesian Updating** - Formal structure for incorporating new information without overweighting recent data.

**The Neurodivergent Advantage:**

* Autistic individuals show 65-80% reduced susceptibility to framing effects (De Martino et al., 2008)
* High-IQ investors achieve 4.9% higher annual returns through reduced disposition effect and superior market timing (Grinblatt et al., 2012)
* Algorithms exhibit virtually zero disposition effect vs. human traders' 15-20pp gap

**Key Insight:** Awareness alone is insufficient. Knowing about biases does not prevent them. Only systems that mechanically override human intuition can achieve rational outcomes.

## Directory Structure

```
rational-trading-behavioral-finance-pub-kb/
├── README.md                    # This file
├── KB-ROUTING.md                # Navigation & cross-references
├── CLAUDE.md                    # AI assistant instructions
├── core-research/               # Synthesized key findings
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
* "It has to come back" - mean reversion fallacy

## Cross-References

* **Cognitive Science:** See `cognitive-kb/` for neuroscience foundations
* **Formal Methods:** Mathematical frameworks in `formal-methods-kb/`
* **Related Markets:** Private credit analysis in `financial-markets-kb/private-credit-markets-pub-kb/`

## Status

**WIP** - Core research complete, synthesis documents pending development.

---

*This repository applies quantitative rigor to behavioral finance, targeting readers who approach trading as applied mathematics and game theory.*
