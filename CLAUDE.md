# CLAUDE.md - AI Assistant Instructions

## Repository Purpose

This repository contains research on cognitive biases in trading and mathematical frameworks for debiasing. Target audience: quantitative traders, high-IQ/autistic individuals seeking rational approaches to portfolio management.

## Content Guidelines

### Data Freshness

* All research artifacts MUST include collection date: `[Collected YYYY-MM-DD]`
* Note AI provider and model for each research output
* Mark stale research (>6 months) for refresh consideration

### Source Attribution

* Include source URLs for all claims
* Reference format: `[source_name](url)` in markdown
* Academic citations: Author et al. (Year)

### Mathematical Content

* Use LaTeX notation for formulas where appropriate
* Include both formal notation and plain-language explanation
* Provide implementation examples (Python/pseudocode) for algorithms

### Bias Catalog Standards

When documenting a bias, include:

1. **Name and aliases**
2. **Formal definition**
3. **Empirical evidence** (studies, effect sizes)
4. **Linguistic markers** (how it appears in trading discourse)
5. **Debiasing strategies**
6. **Exploitation patterns** (how institutions use it)

## File Organization

```
core-research/           # Synthesized findings, unified frameworks
debiasing-frameworks/    # Mathematical solutions, implementation guides
market-microstructure/   # Institutional patterns, order flow analysis
research-artifacts/      # Raw AI research outputs
  └── prompts/           # Original research prompts
ramblings/               # Development notes (YYYY-MM-DD--title.md)
```

## Cross-References

When adding new content, update:

* KB-ROUTING.md with new navigation entries
* README.md if it changes the TL;DR or structure
* Link to related KBs: `cognitive-kb/`, `formal-methods-kb/`

## Development Priorities

1. Maintain mathematical rigor
2. Preserve quantitative evidence
3. Avoid neurotypical bias language
4. Focus on actionable frameworks
5. Track data freshness

## Style Notes

* Audience assumes high cognitive ability - no oversimplification
* Prefer formal models over intuitive explanations
* Include both "what" (bias description) and "so what" (exploitation/debiasing)
* UTF-8 mathematical symbols encouraged (φ, ∈, λ, etc.)
