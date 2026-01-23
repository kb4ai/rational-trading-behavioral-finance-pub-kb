# KB-ROUTING: Navigation & Discovery Guide

## Quick Reference by Topic

### Bias Taxonomy

| Bias | Key Finding | Source | External Reference |
|------|-------------|--------|-------------------|
| Disposition Effect | PGR 14.8% vs PLR 9.8% - 50% more likely to sell winners | [claude-opus](research-artifacts/claude-opus-4-5-deep-research.md) | [Wikipedia](https://en.wikipedia.org/wiki/Disposition_effect) |
| [Loss Aversion](https://en.wikipedia.org/wiki/Loss_aversion) | λ ≈ 2.25 (losses felt 2.25x as painful as gains) | [perplexity](research-artifacts/perplexity-deep-research.md) | [Wikipedia](https://en.wikipedia.org/wiki/Loss_aversion) |
| [Anchoring](https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias)) | 20-40% valuation shift from initial price exposure | [perplexity](research-artifacts/perplexity-deep-research.md) | [Wikipedia](https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias)) |
| [Confirmation Bias](https://en.wikipedia.org/wiki/Confirmation_bias) | 85% disposed to accepting confirming opinions | [claude-opus-clarif](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md) | [Wikipedia](https://en.wikipedia.org/wiki/Confirmation_bias) |
| [Sunk Cost Fallacy](https://yourlogicalfallacyis.com/sunk-cost) | 124% longer holding periods for losers vs winners | [perplexity](research-artifacts/perplexity-deep-research.md) | [YLFI](https://yourlogicalfallacyis.com/sunk-cost) |

### Debiasing Frameworks

| Framework | Formula/Rule | Source |
|-----------|--------------|--------|
| Kelly Criterion | f* = (bp - q) / b, use Half-Kelly | [claude-opus](research-artifacts/claude-opus-4-5-deep-research.md) |
| Position Sizing | Size = (Balance × Risk%) / (Entry - Stop) | [claude-opus](research-artifacts/claude-opus-4-5-deep-research.md) |
| VPIN | Order flow toxicity = Σ\|V_buy - V_sell\| / Σ(V_buy + V_sell) | [perplexity](research-artifacts/perplexity-deep-research.md) |
| Bayesian Updating | P(H\|E) = P(E\|H) × P(H) / P(E) | [claude-opus-clarif](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md) |

### Neurodivergent Advantage Evidence

| Finding | Metric | Source |
|---------|--------|--------|
| Reduced framing effects | 65-80% smaller preference reversals | De Martino et al. 2008 |
| IQ-performance link | 4.9% higher annual returns (top decile) | Grinblatt et al. 2012 |
| Algorithm advantage | PGR ≈ PLR (no disposition effect) | Norges Bank 2025 |
| Ultimatum Game rationality | 85-90% accept positive-EV offers | [perplexity](research-artifacts/perplexity-deep-research.md) |

### Institutional Exploitation Tools

| Tool | Purpose | Source |
|------|---------|--------|
| Volume Profile / POC | Identify retail entry clusters | [claude-opus](research-artifacts/claude-opus-4-5-deep-research.md) |
| Liquidity Heatmaps | Locate stop-loss concentrations | [perplexity](research-artifacts/perplexity-deep-research.md) |
| VPIN | Measure order flow toxicity | [perplexity](research-artifacts/perplexity-deep-research.md) |
| Footprint Charts | Reveal buy/sell imbalances | [claude-opus-clarif](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md) |
| Social Sentiment NLP | Quantify retail bullishness extremes | [perplexity](research-artifacts/perplexity-deep-research.md) |

## Research Artifacts Index

### Primary Research Outputs

1. **[claude-opus-4-5-deep-research.md](research-artifacts/claude-opus-4-5-deep-research.md)**
   - Focus: Cognitive architecture of trading failure
   - Key sections: Why entry price haunts decisions, bias taxonomy, neurodivergent advantage, institutional exploitation
   - Best for: Understanding the "why" of biased trading

2. **[claude-opus-4-5-deep-research-with-clarifications.md](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md)**
   - Focus: Systematic catalog for quantitative minds
   - Key sections: Linguistic markers, differential susceptibility, PFOF exploitation, debiasing frameworks
   - Best for: Practical implementation details

3. **[perplexity-deep-research.md](research-artifacts/perplexity-deep-research.md)**
   - Focus: Quantitative framework for rational exploitation
   - Key sections: Mathematical formalization, game-theoretic exploitation, Bayesian inference, stat arb
   - Best for: Mathematical rigor and formal models
   - Note: Contains extensive references section

4. **[chatgpt-5.2-deep-research.md](research-artifacts/chatgpt-5.2-deep-research.md)**
   - Focus: Cognitive/emotional biases in retail trading
   - Format: PDF/DOCX outputs with links
   - Best for: Visual presentation format

### Research Prompts

* [prompt-shorter.md](research-artifacts/prompts/prompt-shorter.md) - Core research question
* [prompt-shorter-with-clarificatoin-questions.md](research-artifacts/prompts/prompt-shorter-with-clarificatoin-questions.md) - With Q&A clarifications

## Logical Fallacy Resources

### External Reference Sites

| Resource | Description | Best Use |
|----------|-------------|----------|
| [Your Logical Fallacy Is](https://yourlogicalfallacyis.com/) | Visual poster-style fallacy reference | Quick identification, sharing |
| [List of Fallacies (Wikipedia)](https://en.wikipedia.org/wiki/List_of_fallacies) | Comprehensive taxonomy | Formal categorization |
| [Cognitive Bias (Wikipedia)](https://en.wikipedia.org/wiki/Cognitive_bias) | Bias overview and links | Deep research |
| [List of Cognitive Biases](https://en.wikipedia.org/wiki/List_of_cognitive_biases) | Exhaustive bias catalog | Completeness |

### Trading-Relevant Fallacies

| Fallacy | Trading Manifestation | Link |
|---------|----------------------|------|
| [Sunk Cost](https://yourlogicalfallacyis.com/sunk-cost) | "Can't sell—I've held too long" | Classic disposition effect driver |
| [Gambler's Fallacy](https://yourlogicalfallacyis.com/the-gamblers-fallacy) | "It has to revert to mean" | Independent events ≠ dependent |
| [Appeal to Authority](https://yourlogicalfallacyis.com/appeal-to-authority) | "This guru predicted 2008" | Expert != always correct |
| [Anecdotal](https://yourlogicalfallacyis.com/anecdotal) | "My friend 10x'd on memes" | Survivorship bias in stories |
| [False Cause (Post Hoc)](https://yourlogicalfallacyis.com/false-cause) | "Markets fell because of X" | Correlation ≠ causation |
| [Black-or-White](https://yourlogicalfallacyis.com/black-or-white) | "HODL or you're paper hands" | False dichotomy |
| [Bandwagon](https://yourlogicalfallacyis.com/bandwagon) | "Everyone is buying this" | Herding behavior |
| [Burden of Proof](https://yourlogicalfallacyis.com/burden-of-proof) | "Prove it won't moon" | Shifting proof requirements |

---

## Cross-KB Navigation

### Related Knowledge Bases

| KB | Relevance | Path |
|----|-----------|------|
| Cognitive Science | Neuroscience foundations, neurotypes | `cognitive-kb/` |
| Formal Methods | Mathematical verification, theorem proving | `formal-methods-kb/` |
| Private Credit Markets | Alternative finance, market dynamics | `financial-markets-kb/private-credit-markets-pub-kb/` |

### Conceptual Links

**From Cognitive Science:**

* Dual-process theory (System 1 vs System 2) → Trading heuristics vs deliberation
* Autism spectrum research → Enhanced rationality in financial decisions
* Prospect Theory (Kahneman & Tversky) → Reference-dependent valuation

**From Formal Methods:**

* Constraint programming → Portfolio optimization
* Symbolic computation → Bias-free decision systems
* Monte Carlo methods → Scenario evaluation

**From Market Microstructure:**

* Order flow analysis → Retail position detection
* Liquidity dynamics → Exploitation mechanisms
* Game theory → Multi-agent market modeling

## Data Freshness Tracking

| File | Collected | AI Provider | Model |
|------|-----------|-------------|-------|
| claude-opus-4-5-deep-research.md | 2025-01-22 | Anthropic | Claude Opus 4.5 |
| claude-opus-4-5-deep-research-with-clarifications.md | 2025-01-22 | Anthropic | Claude Opus 4.5 |
| perplexity-deep-research.md | 2025-01-22 | Perplexity | Deep Research |
| chatgpt-5.2-deep-research.md | 2025-01-22 | OpenAI | ChatGPT 5.2 |

## Future Development

### Planned Synthesis Documents

* [ ] `core-research/cognitive-architecture-of-trading-failure.md` - Unified bias taxonomy
* [ ] `core-research/taxonomy-of-behavioral-biases.md` - Formal categorization
* [ ] `core-research/logical-fallacies-in-trading-discourse.md` - Mapping classical fallacies to market narratives
* [ ] `debiasing-frameworks/kelly-criterion-position-sizing.md` - Implementation guide
* [ ] `debiasing-frameworks/systematic-rebalancing-rules.md` - Calendar + threshold approaches
* [ ] `market-microstructure/institutional-exploitation-patterns.md` - VPIN, volume profile analysis
* [ ] `market-microstructure/volume-profile-analysis.md` - Technical implementation

### Research Gaps

* Empirical backtesting of debiasing frameworks
* Comparison of robo-advisor vs manual rebalancing outcomes
* Neurodiversity-specific trading platform design
* Real-time bias detection systems
* Logical fallacy analysis in financial media narratives (post-hoc, appeal to authority)
* Formal logic training as debiasing intervention
