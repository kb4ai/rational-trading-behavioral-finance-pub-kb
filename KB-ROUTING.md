# KB-ROUTING: Navigation & Discovery Guide

## Quick Reference by Topic

### Bias Taxonomy

| Bias | Key Finding | Source |
|------|-------------|--------|
| Disposition Effect | PGR 14.8% vs PLR 9.8% - 50% more likely to sell winners | [claude-opus](research-artifacts/claude-opus-4-5-deep-research.md) |
| Loss Aversion | λ ≈ 2.25 (losses felt 2.25x as painful as gains) | [perplexity](research-artifacts/perplexity-deep-research.md) |
| Anchoring | 20-40% valuation shift from initial price exposure | [perplexity](research-artifacts/perplexity-deep-research.md) |
| Confirmation Bias | 85% disposed to accepting confirming opinions | [claude-opus-clarif](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md) |
| Sunk Cost | 124% longer holding periods for losers vs winners | [perplexity](research-artifacts/perplexity-deep-research.md) |

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
* [ ] `debiasing-frameworks/kelly-criterion-position-sizing.md` - Implementation guide
* [ ] `debiasing-frameworks/systematic-rebalancing-rules.md` - Calendar + threshold approaches
* [ ] `market-microstructure/institutional-exploitation-patterns.md` - VPIN, volume profile analysis
* [ ] `market-microstructure/volume-profile-analysis.md` - Technical implementation

### Research Gaps

* Empirical backtesting of debiasing frameworks
* Comparison of robo-advisor vs manual rebalancing outcomes
* Neurodiversity-specific trading platform design
* Real-time bias detection systems
