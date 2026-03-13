# KB-ROUTING: Navigation & Discovery Guide

## Quick Reference by Topic

### Bias Taxonomy

| Bias | Key Finding | Source | External Reference |
|------|-------------|--------|-------------------|
| Disposition Effect | PGR 14.8% vs PLR 9.8% - 50% more likely to sell winners | [claude-opus](research-artifacts/claude-opus-4-5-deep-research.md), [Odean 1998](core-research/behavioral-biases-multi-paper-synthesis.md#odean-1998--the-disposition-effect-sell-winners-hold-losers) | [Wikipedia](https://en.wikipedia.org/wiki/Disposition_effect) |
| [Loss Aversion](https://en.wikipedia.org/wiki/Loss_aversion) | λ ≈ 2.25 (losses felt 2.25x as painful as gains) | [perplexity](research-artifacts/perplexity-deep-research.md) | [Wikipedia](https://en.wikipedia.org/wiki/Loss_aversion) |
| [Anchoring](https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias)) | 20-40% valuation shift from initial price exposure | [perplexity](research-artifacts/perplexity-deep-research.md) | [Wikipedia](https://en.wikipedia.org/wiki/Anchoring_(cognitive_bias)) |
| [Confirmation Bias](https://en.wikipedia.org/wiki/Confirmation_bias) | 85% disposed to accepting confirming opinions | [claude-opus-clarif](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md) | [Wikipedia](https://en.wikipedia.org/wiki/Confirmation_bias) |
| [Sunk Cost Fallacy](https://yourlogicalfallacyis.com/sunk-cost) | 124% longer holding periods for losers vs winners | [perplexity](research-artifacts/perplexity-deep-research.md) | [YLFI](https://yourlogicalfallacyis.com/sunk-cost) |
| [Mental Accounting](https://en.wikipedia.org/wiki/Mental_accounting) | Money mentally labeled reduces fungibility; house money g=0.37; payment decoupling drives overspending | [Thaler 1985](core-research/behavioral-biases-multi-paper-synthesis.md#thaler-1985-mental-accountingmoney-gets-labels), [**Comprehensive Analysis**](core-research/mental-accounting-thaler-comprehensive.md) | [Wikipedia](https://en.wikipedia.org/wiki/Mental_accounting) |
| [Status Quo Bias](https://en.wikipedia.org/wiki/Status_quo_bias) | Disproportionate preference for default/current state; WTA/WTP ratio ≈ 2.1–2.3; 401k default inertia: 76% stick at 3% vs optimal 6%+ | [Samuelson & Zeckhauser 1988](core-research/behavioral-biases-multi-paper-synthesis.md#samuelson--zeckhauser-1988-status-quo-biasdoing-nothing-is-a-powerful-option), [**Full Analysis**](core-research/omission-status-quo-inaction-inertia-trading.md) | [Wikipedia](https://en.wikipedia.org/wiki/Status_quo_bias) |
| Omission Bias | Harmful omissions rated less blameworthy than equivalent commissions; d = 0.40–0.53; omission preference 72% vs status quo 51% — distinct constructs (Ritov & Baron 1992) | [**Full Analysis**](core-research/omission-status-quo-inaction-inertia-trading.md) | [Spranca et al. 1991](https://www.sciencedirect.com/science/article/pii/002210319190011T) |
| Inaction Inertia | Missed superior opportunity → reduced probability of acting on still-positive inferior opportunity; stock market: missed gain exit → less likely to exit at grave loss | [**Full Analysis**](core-research/omission-status-quo-inaction-inertia-trading.md) | [Tykocinski 2004](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1559-1816.2004.tb02001.x) |
| Single-Denominator Bias | 60-80% evaluate in nominal terms; 15-30% spending errors from face value anchoring; denomination choice flips disposition effect direction | [**Core Paper**](core-research/multi-denomination-portfolio-valuation.md), [**Debiasing Framework**](debiasing-frameworks/denomination-invariant-evaluation.md) | [Money Illusion (Wikipedia)](https://en.wikipedia.org/wiki/Money_illusion) |
| Opportunity Cost Neglect | Forgone alternatives underweighted because implicit; d=0.22 meta-analytic (d=0.45–0.85 seminal); 20pp purchase-rate shift on OC reminder; both overtrading (−6.5%/yr) and under-trading ($170k/career missed match) are OCN instantiations | [**Full Analysis**](core-research/opportunity-cost-neglect-in-trading.md) | [Frederick et al. 2009](https://doi.org/10.1086/599764) |

### Debiasing Frameworks

| Framework | Formula/Rule | Source |
|-----------|--------------|--------|
| Kelly Criterion | f* = (bp - q) / b, use Half-Kelly | [claude-opus](research-artifacts/claude-opus-4-5-deep-research.md) |
| Position Sizing | Size = (Balance × Risk%) / (Entry - Stop) | [claude-opus](research-artifacts/claude-opus-4-5-deep-research.md) |
| VPIN | Order flow toxicity = Σ\|V_buy - V_sell\| / Σ(V_buy + V_sell) | [perplexity](research-artifacts/perplexity-deep-research.md) |
| Bayesian Updating | P(H\|E) = P(E\|H) × P(H) / P(E) | [claude-opus-clarif](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md) |
| Denomination-Invariant Evaluation | G(t₀,t₁) = min_d{V_d(t₁)/V_d(t₀)}; alert when spread S > 0.10 | [**Framework**](debiasing-frameworks/denomination-invariant-evaluation.md), [**Python impl**](debiasing-frameworks/examples/multi-denomination-tracker.py) |
| Hypothetical Cash Reframe | Converts hold/sell (omission framing) to buy/not-buy (commission framing); eliminates act-omit asymmetry; restores WTA/WTP ratio → 1.0 | [**Omission/Inaction Framework**](core-research/omission-status-quo-inaction-inertia-trading.md#71-the-hypothetical-cash-reframe-highest-empirical-support) | KKT 1991 |
| Inaction Justification Log | Forces documented active commission decision for each held position; symmetric dual-path checklist | [**Protocol**](core-research/omission-status-quo-inaction-inertia-trading.md#72-forced-periodic-review-with-inaction-justification-requirement) | |
| Pre-Mortem for Non-Action | "Imagine I did NOT act; portfolio -15%: what mechanism?" — prospective hindsight improves outcome identification 30% (Klein 1998) | [**Protocol**](core-research/omission-status-quo-inaction-inertia-trading.md#73-pre-mortem-for-non-action-decisions) | |

### Neurodivergent Advantage Evidence

| Finding | Metric | Source | Details |
|---------|--------|--------|---------|
| Reduced framing effects | 65-80% smaller preference reversals | [De Martino et al. 2008](https://doi.org/10.1523/JNEUROSCI.2895-08.2008) | [Detailed explanation](core-research/de-martino-2008-framing-effects-autism-explained.md), [Multi-paper synthesis](core-research/behavioral-biases-multi-paper-synthesis.md) |
| IQ-performance link | 4.9% higher annual returns (top decile) | [Grinblatt et al. 2012](https://doi.org/10.1016/j.jfineco.2011.05.016) | [Multi-paper synthesis](core-research/behavioral-biases-multi-paper-synthesis.md) |
| Algorithm advantage | PGR ≈ PLR (no disposition effect) | Norges Bank 2025 | |
| Ultimatum Game rationality | 85-90% accept positive-EV offers | [perplexity](research-artifacts/perplexity-deep-research.md) | |

### Institutional Exploitation Tools

| Tool | Purpose | Source |
|------|---------|--------|
| Volume Profile / POC | Identify retail entry clusters | [claude-opus](research-artifacts/claude-opus-4-5-deep-research.md) |
| Liquidity Heatmaps | Locate stop-loss concentrations | [perplexity](research-artifacts/perplexity-deep-research.md) |
| VPIN | Measure order flow toxicity | [perplexity](research-artifacts/perplexity-deep-research.md) |
| Footprint Charts | Reveal buy/sell imbalances | [claude-opus-clarif](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md) |
| Social Sentiment NLP | Quantify retail bullishness extremes | [perplexity](research-artifacts/perplexity-deep-research.md) |

## Bibliography

**[BIBLIOGRAPHY.md](BIBLIOGRAPHY.md)** — Central reference for all academic papers cited in this knowledge base, including DOI links, full citations, and cross-reference index showing where each paper is discussed.

---

## Core Research Documents

### Synthesized Analyses

1. **[de-martino-2008-framing-effects-autism-explained.md](core-research/de-martino-2008-framing-effects-autism-explained.md)**
   - Focus: Detailed breakdown of De Martino et al. (2008) framing effects study
   - Key sections: Methodology, actual effect sizes (46% behavioral vs 65-80% physiological), SCR analysis
   - Best for: Understanding exactly what the "reduced framing effects" claim means
   - Source: ChatGPT 5.2 research conversation

2. **[behavioral-biases-multi-paper-synthesis.md](core-research/behavioral-biases-multi-paper-synthesis.md)**
   - Focus: Comprehensive overview of 7 foundational papers on framing, disposition effect, mental accounting
   - Papers covered: De Martino 2008, Grinblatt 2012, Odean 1998, Barber & Odean 2000, Thaler 1985, Samuelson & Zeckhauser 1988, Yafai 2014
   - Key sections: Framing effects correction (46% vs 65-80%), disposition effect mechanics, IQ-trading link, status quo bias
   - Best for: Understanding the interconnected family of cognitive biases affecting trading decisions
   - Source: ChatGPT 5.2 research conversation

3. **[mental-accounting-thaler-comprehensive.md](core-research/mental-accounting-thaler-comprehensive.md)**
   - Focus: Complete academic treatment of Thaler's mental accounting framework (1985, 1999)
   - Papers covered: Thaler 1985/1999, Kahneman & Tversky 1979/1992, Thaler & Johnson 1990, Prelec & Loewenstein 1998, Arkes & Blumer 1985, Benartzi & Thaler 1995, Paul et al. 2023
   - Key sections: Formal mathematical model (value function, hedonic editing rules), house money meta-analysis (g=0.37), fungibility violation analysis, institutional exploitation mechanisms, debiasing strategies
   - Best for: Rigorous formal treatment with complete citation apparatus; understanding how mental accounting drives trading pathologies
   - Source: Claude Sonnet 4.6 web research, 2026-02-27

4. **[fungibility-asset-transformation-rational-framework.md](core-research/fungibility-asset-transformation-rational-framework.md)**
   - Focus: Radical rational-mathematical perspective on why "spending" is a cognitive illusion and mental labels are formally incoherent
   - Papers covered: Hohfeld 1917 (ownership as bundle of rights), Rosch 1978 (prototype categorization), Shefrin & Thaler 1988 (behavioral life-cycle), Baron-Cohen 2009 (systematizing), Rabin & Weizsäcker 2009 (narrow bracketing → dominated choices), Gul & Pesendorfer 2001 (temptation axiomatics), Kőszegi & Matejka 2020 (rational inattention), Barberis et al. 2001 (asset pricing), Knutson et al. 2007 (neuroscience), Rozenkrantz et al. 2021 (ASD enhanced rationality)
   - Key sections: Ownership as set theory, spending as asset transformation (conservation law), thermodynamic analogy, partition welfare loss, game-theoretic exploitation of mental accountants, autistic advantage hypothesis, linguistic markers, philosophical perspectives (Stoic/Buddhist), neuroscience of pain-of-paying
   - Best for: The mathematically rigorous "polymath's view" — why rational entities see no distinction between "savings" and "spending money"; why every voluntary exchange is a neutral transformation, not a loss
   - Source: Claude Opus 4.6 synthesis, 2026-02-27

5. **[omission-status-quo-inaction-inertia-trading.md](core-research/omission-status-quo-inaction-inertia-trading.md)**
   - Focus: Empirical synthesis of omission bias, status quo bias, and inaction inertia in trading/investment contexts
   - Papers covered: Spranca et al. (1991), Ritov & Baron (1990, 1992), Samuelson & Zeckhauser (1988), KKT (1991), Madrian & Shea (2001), Choi et al. (2004), Tykocinski & Pittman (1998, 2001), Tykocinski (2004), Benartzi & Thaler (1995), French & Poterba (1991), Barber & Odean (2000)
   - Key sections: Formal separation of omission vs status quo bias (72% vs 51%); 401(k) inertia quantification; inaction inertia stock market mechanism; aggregate cost table; six debiasing protocols including hypothetical cash reframe, inaction justification log, pre-mortem for non-action
   - Best for: Understanding why holding/not-acting is cognitively asymmetric; practical debiasing protocols for inaction-type biases
   - Source: Claude Sonnet 4.6 web research, 2026-03-13

6. **[mental-accounting-cognitive-science-parallels.md](core-research/mental-accounting-cognitive-science-parallels.md)**
   - Focus: Mental accounting grounded in 7 major cognitive science frameworks
   - Frameworks covered: Dual-process theory (Kahneman, Evans, Stanovich tripartite model), bounded rationality (Simon satisficing), ecological rationality (Gigerenzer adaptive toolbox), cognitive load (Miller 7±2, Sweller), attention economics (Kahneman 1973, Sims rational inattention, Kőszegi-Matejka water-filling), construal level theory (Trope & Liberman), schema theory (Bartlett, Zelizer), embodied cognition (Lakoff & Johnson conceptual metaphor, Barsalou grounded cognition)
   - Key sections: Integrated 6-level mechanistic model, MONEY IS WATER metaphor analysis, debiasing implications across all levels
   - Best for: Understanding WHY mental accounting exists mechanistically — not just what it is, but the computational, attentional, embodied, and cultural architecture that produces it
   - Source: Claude Sonnet 4.6 synthesis, 2026-02-27

### Philosophical Foundations (Ramblings)

6. **[spending-as-ontological-error-semiotics-language.md](ramblings/2026-02-27--spending-as-ontological-error-semiotics-language.md)**
   - Focus: "Spending" as category error at 5 levels: etymology, semiotic, ontological, cognitive, linguistic
   - Key coverage: Peirce sign taxonomy, Baudrillard hyperreal money, Chen (2013) Sapir-Whorf savings data, Wittgenstein language games, Ryle category mistakes, Searle institutional facts, category theory morphisms, dual coding theory, Grandin visual taxonomy, Bourdieu linguistic capital
   - Best for: Understanding why "spending" is not merely biased but ontologically incoherent

7. **[platonic-formalist-economics-beyond-keynesian.md](ramblings/2026-02-27--platonic-formalist-economics-beyond-keynesian.md)**
   - Focus: Maps 6 philosophical positions on economic "ground truth"
   - Key coverage: Debreu-Bourbaki program, Austrian praxeology, Keynesian animal spirits, Veblen institutional habits, Marx commodity fetishism, Georgescu-Roegen thermodynamics, Arthur complexity economics
   - Best for: Understanding the philosophical landscape our framework sits within

8. **[artificial-partitioning-work-leisure-watts-krishnamurti.md](ramblings/2026-02-27--artificial-partitioning-work-leisure-watts-krishnamurti.md)**
   - Focus: Structural isomorphism between work/leisure and savings/spending partitions
   - Key coverage: Watts (Taoist integration), Krishnamurti (thought-as-fragmentation), Csikszentmihalyi (flow), Heidegger (das Man), Illich (shadow work), Graeber (bullshit jobs)
   - Best for: Seeing the savings/spending partition as one instance of a universal cognitive partitioning error

---

## Research Sources by AI Provider

| Provider | Model/Service | Focus | File |
|----------|---------------|-------|------|
| Claude | Opus 4.5 | Cognitive architecture of trading failure | [claude-opus-4-5-deep-research.md](research-artifacts/claude-opus-4-5-deep-research.md) |
| Claude | Opus 4.5 | Quantitative framework for rational exploitation | [claude-opus-4-5-deep-research-with-clarifications.md](research-artifacts/claude-opus-4-5-deep-research-with-clarifications.md) |
| Perplexity | Deep Research | Neurodivergent advantage, institutional exploitation | [perplexity-deep-research.md](research-artifacts/perplexity-deep-research.md) |
| ChatGPT | 5.2 Deep Research | Cognitive/emotional biases in retail trading | [chatgpt-5.2-deep-research.md](research-artifacts/chatgpt-5.2-deep-research.md) |
| ChatGPT | 5.2 | Multi-paper synthesis: 7 foundational behavioral bias studies | [behavioral-biases-multi-paper-synthesis.md](core-research/behavioral-biases-multi-paper-synthesis.md) |
| Claude | Sonnet 4.6 | Mental accounting comprehensive: Thaler framework, hedonic editing, institutional exploitation | [mental-accounting-thaler-comprehensive.md](core-research/mental-accounting-thaler-comprehensive.md) |
| Claude | Opus 4.6 | Fungibility axiom: spending as asset transformation, rational entity model, game theory | [fungibility-asset-transformation-rational-framework.md](core-research/fungibility-asset-transformation-rational-framework.md) |
| Claude | Sonnet 4.6 | Mental accounting grounded in 7 cognitive science frameworks | [mental-accounting-cognitive-science-parallels.md](core-research/mental-accounting-cognitive-science-parallels.md) |
| Claude | Sonnet 4.6 | Omission bias, status quo bias, inaction inertia: empirical synthesis + debiasing protocols | [omission-status-quo-inaction-inertia-trading.md](core-research/omission-status-quo-inaction-inertia-trading.md) |
| Claude | Sonnet 4.6 | Opportunity cost neglect: full academic synthesis, 16 papers, action/omission asymmetry, quantified costs, debiasing protocols | [opportunity-cost-neglect-in-trading.md](core-research/opportunity-cost-neglect-in-trading.md) |

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
| claude-opus-4-5-deep-research.md | 2026-01-22 | Anthropic | Claude Opus 4.5 |
| claude-opus-4-5-deep-research-with-clarifications.md | 2026-01-22 | Anthropic | Claude Opus 4.5 |
| perplexity-deep-research.md | 2026-01-22 | Perplexity | Deep Research |
| chatgpt-5.2-deep-research.md | 2026-01-22 | OpenAI | ChatGPT 5.2 |
| de-martino-2008-framing-effects-autism-explained.md | 2026-01-23 | OpenAI | ChatGPT 5.2 |
| behavioral-biases-multi-paper-synthesis.md | 2026-01-23 | OpenAI | ChatGPT 5.2 |
| mental-accounting-thaler-comprehensive.md | 2026-02-27 | Anthropic | Claude Sonnet 4.6 |
| fungibility-asset-transformation-rational-framework.md | 2026-02-27 | Anthropic | Claude Opus 4.6 |
| mental-accounting-cognitive-science-parallels.md | 2026-02-27 | Anthropic | Claude Sonnet 4.6 |
| omission-status-quo-inaction-inertia-trading.md | 2026-03-13 | Anthropic | Claude Sonnet 4.6 |
| opportunity-cost-neglect-in-trading.md | 2026-03-13 | Anthropic | Claude Sonnet 4.6 |

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
