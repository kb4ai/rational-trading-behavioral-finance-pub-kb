# Mental Accounting: Cognitive Science Parallels and Theoretical Extensions

[Collected 2026-02-27] [AI Provider: Anthropic, Claude Sonnet 4.6]

---

## Overview

Mental accounting (Thaler, 1985, 1999) does not exist in theoretical isolation. It sits at the intersection of seven major cognitive science research programs, each offering a distinct mechanistic explanation for *why* humans construct non-fungible financial categories and what functional role those categories serve. This document synthesizes those parallels, with full citations, to ground mental accounting in the broader architecture of bounded rationality, dual-process cognition, and embodied financial reasoning.

**Central claim**: Mental accounting is not merely a "bias" but a partially adaptive solution to genuine computational constraints — one that can be exploited or debiased once its mechanistic substrate is understood.

---

## 1. Dual-Process Theory Parallels

### 1.1 Kahneman's System 1 / System 2 Framework

The dual-process framework posits two interacting computational systems (Kahneman, 2011; *Thinking, Fast and Slow*):

* **System 1 (Type 1 processes)**: automatic, associative, fast, parallel, evolutionarily ancient, opaque to introspection, high-bandwidth but low-precision
* **System 2 (Type 2 processes)**: deliberate, rule-governed, serial, slow, cognitively costly, correlated with measured intelligence

Mental accounting maps onto this architecture as a **System 1 default** with partial System 2 endorsement:

* Account *creation* is largely automatic — money received as a windfall is coded as belonging to a different category than earned income before deliberate reasoning engages (Thaler, 1999, p. 196)
* Account *boundaries* resist System 2 override even when the agent is explicitly informed of the fungibility violation — demonstrating that the bias is not simply ignorance but a low-level representational commitment
* Temporal evaluation frequency (narrow bracketing) is set by System 1 at short intervals; System 2 can consciously adopt long-horizon evaluation but this requires sustained working-memory allocation

**Key study**: Kahneman & Tversky (1984) demonstrated that identical monetary outcomes produce different choices depending on framing, and the effect persists even when subjects are warned — evidence that System 1 coding precedes System 2 evaluation.

**Recent critique**: Evans & Stanovich (2013) argue that the System 1/System 2 dichotomy oversimplifies — they prefer *Type 1* (autonomous, fast) vs. *Type 2* (cognitively demanding, controlled) processes to avoid the implication of two fully separate systems. Under this refined nomenclature, mental accounting involves Type 1 default coding that Type 2 processing may or may not successfully intervene upon.

**Citation**: Evans JSTB, Stanovich KE. Dual-Process Theories of Higher Cognition: Advancing the Debate. *Perspectives on Psychological Science*. 2013;8(3):223-241. [DOI: 10.1177/1745691612460685](https://doi.org/10.1177/1745691612460685)

---

### 1.2 Stanovich's Tripartite Mind Model

Stanovich (2009, 2011) decomposed "System 2" into two sub-levels, yielding a tripartite architecture:

* **Autonomous mind** (TASS — The Autonomous Set of Systems): modular, encapsulated, fast Type 1 processes. Corresponds to Kahneman's System 1.
* **Algorithmic mind**: sustained working-memory operations, executive function, fluid intelligence (g_f). Determines *capacity* for cognitive decoupling and simulation.
* **Reflective mind**: epistemic metacognition, goal prioritization, disposition to engage in rational override. Determines *tendency* to engage Type 2 processing even when capacity exists.

**Mental accounting under the tripartite model**:

* The **autonomous mind** auto-generates account labels (windfall vs. income, gains vs. losses) using associative cues — source of money, physical form (cash vs. card), category label
* The **algorithmic mind** could in principle override non-fungibility if given sufficient working memory and time — but this is computationally expensive
* The **reflective mind** determines whether the agent *wants* to engage in fungibility correction — crucially, Stanovich's empirical work shows that many intelligent agents (high algorithmic capacity) still fail to correct for biases because reflective disposition is orthogonal to IQ

**Implication for trading**: An investor with high analytical IQ (algorithmic capacity) who lacks epistemic rationality training (reflective mind calibration) will construct mental accounts just as readily as a naive investor. This explains why professional traders exhibit mental accounting despite quantitative sophistication.

**Citation**: Stanovich KE. *Rationality and the Reflective Mind*. Oxford University Press; 2011. [ISBN: 9780195341140](https://global.oup.com/academic/product/rationality-and-the-reflective-mind-9780195341140)

**Citation**: Stanovich KE. Distinguishing the reflective, algorithmic, and autonomous minds: Is it time for a tri-process theory? In Evans JSTB, Frankish K, eds. *In Two Minds: Dual Processes and Beyond*. Oxford University Press; 2009:55-88. [ResearchGate](https://www.researchgate.net/publication/237337356_Distinguishing_the_reflective_algorithmic_and_autonomous_minds_Is_it_time_for_a_tri-process_theory)

---

### 1.3 Evans' Default-Interventionist Architecture

Evans (2008) proposed the **default-interventionist** model, which clarifies the *temporal* relationship between Type 1 and Type 2 processing:

1. Type 1 processes generate an initial default response *immediately*
2. Type 2 processes may *subsequently* intervene to revise that default — but only if:
   * Sufficient cognitive resources are available
   * The system detects a reason to override (metacognitive monitoring)
   * The agent has the appropriate override tendency (reflective mind in Stanovich's terms)

**Mental accounting as default**: Account categorization is the default output of Type 1 cognition. The intervention (fungibility calculation) requires Type 2 engagement. Since Type 2 intervention is effortful and often incomplete, mental accounting persists as the dominant operative representation in most real-world financial decisions — especially under time pressure, cognitive load, or emotional arousal.

**Important asymmetry**: Default-interventionist theory predicts that mental accounting effects will be *stronger* under:

* High cognitive load (less Type 2 capacity available for intervention)
* Time pressure (insufficient time for Type 2 processing)
* Emotional states that down-regulate prefrontal resources
* Decision fatigue (ego depletion depletes Type 2 override capacity)

**Citation**: Evans JSTB. Dual-Processing Accounts of Reasoning, Judgment, and Social Cognition. *Annual Review of Psychology*. 2008;59:255-278. [DOI: 10.1146/annurev.psych.59.103006.093629](https://doi.org/10.1146/annurev.psych.59.103006.093629)

---

## 2. Bounded Rationality (Simon) and Ecological Rationality (Gigerenzer)

### 2.1 Simon's Satisficing and Mental Accounting as Optimization Under Constraint

Herbert Simon (1955, 1956) introduced **bounded rationality** as the observation that economic agents face three types of cognitive limitations:

* **Computational complexity** of the decision problem itself
* **Cognitive capacity** limitations of the processing system
* **Time constraints** on deliberation

Given these bounds, Simon argued that agents **satisfice** — searching through the space of alternatives until one is found that meets an *aspiration level* (a threshold, not a maximum). Satisficing terminates search early and is rational given search costs.

**Mental accounting as satisficing strategy**: Thaler's account structure implements exactly this logic at the portfolio level:

* Instead of computing the global expected utility across all financial decisions simultaneously (NP-hard in realistic environments), an agent decomposes the problem into labeled sub-accounts
* Each account is managed to a local aspiration level (e.g., "don't touch the emergency fund," "keep vacation account above $2,000")
* Violations of these local targets trigger distress responses disproportionate to their global wealth significance — because the system is monitoring local account states, not global utility

This decomposition reduces the dimensionality of the decision problem from O(2^N) to O(N) in the number of financial categories.

**Citation**: Simon HA. A Behavioral Model of Rational Choice. *Quarterly Journal of Economics*. 1955;69(1):99-118. [DOI: 10.2307/1884852](https://doi.org/10.2307/1884852)

**Citation**: Simon HA. Rational Choice and the Structure of the Environment. *Psychological Review*. 1956;63(2):129-138. [DOI: 10.1037/h0042769](https://doi.org/10.1037/h0042769)

---

### 2.2 Gigerenzer's Ecological Rationality and the Adaptive Toolbox

Gigerenzer (2001, 2008) and colleagues directly challenged the "bias-and-error" framing of behavioral economics with **ecological rationality**: a heuristic is not irrational in itself — its rationality is an *environment-relative* property. A heuristic is ecologically rational if it exploits the statistical structure of the environment to produce good decisions with minimal computation.

The **adaptive toolbox** (Gigerenzer & Todd, 1999) is the collection of domain-specific heuristics available to a reasoner, each consisting of:

1. **Search rule**: which cues to attend to and in what order
2. **Stop rule**: when to terminate information search
3. **Decision rule**: how to map available information to a choice

**Mental accounting as an adaptive toolbox element**:

* **1/N heuristic**: Equal allocation of resources across N mental categories (naive diversification) — DeMiguel, Garlappi & Uppal (2009) showed that 1/N outperforms mean-variance optimization in out-of-sample prediction across 14 datasets when N ≥ 25 and estimation period is finite. [DOI: 10.1093/rfs/hhm075](https://doi.org/10.1093/rfs/hhm075)
* **Bucketing heuristics**: Partitioning financial resources into labeled buckets (consumption, savings, emergency) is adaptive in environments with self-control problems, because the labeling creates commitment devices that resist the time-inconsistent preferences documented by Laibson (1997)
* **Loss-frame account closure**: Refusing to close losing accounts (disposition effect) has the adaptive function of resisting panic selling in noisy environments where short-term losses are often mean-reverting

**The "less is more" principle**: In environments with high parameter uncertainty (stock return estimation), simple heuristics that use fewer parameters systematically outperform complex optimization models that overfit to historical data. Mental accounting's coarseness may be adaptive under parameter uncertainty.

**Citation**: Gigerenzer G, Todd PM, ABC Research Group. *Simple Heuristics That Make Us Smart*. Oxford University Press; 1999. [ISBN: 9780195143812](https://global.oup.com/academic/product/simple-heuristics-that-make-us-smart-9780195143812)

**Citation**: Gigerenzer G. Why Heuristics Work. *Perspectives on Psychological Science*. 2008;3(1):20-29. [DOI: 10.1111/j.1745-6916.2008.00058.x](https://doi.org/10.1111/j.1745-6916.2008.00058.x)

**Citation**: DeMiguel V, Garlappi L, Uppal R. Optimal Versus Naive Diversification: How Inefficient Is the 1/N Portfolio Strategy? *Review of Financial Studies*. 2009;22(5):1915-1953. [DOI: 10.1093/rfs/hhm075](https://doi.org/10.1093/rfs/hhm075)

---

## 3. Cognitive Load Theory and Chunking

### 3.1 Miller's Magical Number: Working Memory as the Binding Constraint

Miller (1956) identified that short-term memory capacity is limited to approximately **7 ± 2 chunks** of information. Crucially, the unit of storage is the *chunk* — a meaningful unit that can encode arbitrary amounts of lower-level information if the agent has appropriate schemas for compression.

**Citation**: Miller GA. The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information. *Psychological Review*. 1956;63(2):81-97. [DOI: 10.1037/h0043158](https://doi.org/10.1037/h0043158)

**Mental accounts as chunks**: A mental account is precisely a chunk — it encodes a large number of individual transactions into a single labeled category with an associated balance, aspiration level, and evaluation frequency. A household managing 6 mental accounts (income, housing, food, entertainment, savings, emergency) is tracking 6 chunks, well within Miller's capacity limit — whereas tracking every individual transaction would require hundreds of working-memory slots.

---

### 3.2 Sweller's Cognitive Load Theory

Sweller (1988, 1994) extended Miller's insight into a full taxonomy of cognitive load:

* **Intrinsic load**: Complexity inherent to the material itself (number of interacting elements)
* **Extraneous load**: Load imposed by poor representation or task structure
* **Germane load**: Load devoted to schema formation and automation

**Citation**: Sweller J. Cognitive Load During Problem Solving: Effects on Learning. *Cognitive Science*. 1988;12(2):257-285. [DOI: 10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)

**Mental accounting as load reduction**:

* By chunking transactions into accounts, agents *reduce intrinsic load* on working memory from O(transactions) to O(accounts)
* By using simple account-level rules ("don't spend savings on entertainment"), agents *reduce extraneous load* from complex multi-attribute optimization to single-attribute threshold checking
* Account schemas, once formed, become automated (germane load converts to schema), further reducing ongoing cognitive costs

**Prediction**: Mental accounting should be stronger (more rigid, more resistant to override) in agents with lower working-memory capacity — because those agents are closer to their cognitive limits and cannot afford the extraneous load of fungibility calculation. This is empirically testable and partially supported by Shamosh & Gray (2008)'s work on working memory and delay discounting.

**Citation**: Shamosh NA, Gray JR. Delay discounting and intelligence: A meta-analysis. *Intelligence*. 2008;36(4):289-305. [DOI: 10.1016/j.intell.2007.09.004](https://doi.org/10.1016/j.intell.2007.09.004)

---

## 4. Attention Economics

### 4.1 Kahneman's Capacity Theory of Attention (1973)

Before writing *Thinking, Fast and Slow*, Kahneman (1973) published *Attention and Effort*, which modeled attention as a **finite, undifferentiated resource** (a "mental energy pool") that can be allocated flexibly across concurrent tasks, but whose total supply is limited. Key findings:

* Pupil dilation (measured in real-time) tracks mental effort continuously — establishing that effort is a real, metabolically costly resource
* Arousal modulates the total capacity available — moderate arousal expands the pool; extreme arousal (stress, excitement) contracts it
* The allocation policy is only partly under voluntary control — salient stimuli automatically attract capacity away from deliberate tasks

**Citation**: Kahneman D. *Attention and Effort*. Prentice-Hall; 1973. [Archive.org](https://s3.amazonaws.com/knowen-production/big_attachments/fdf0161367c4801ac8b5a6cc42e8413d/Attention+and+Effort+-+Kahneman.pdf)

**Mental accounting as attention allocation**: If attention is scarce, an agent cannot monitor all financial positions simultaneously. Mental accounts function as **attention partitions** — by labeling categories and setting aspiration levels, the system allocates monitoring attention to accounts that are near their thresholds and reduces attention to accounts that are comfortably within bounds. This is analogous to hierarchical interrupt-driven processing: only accounts near thresholds generate attention-demanding signals.

---

### 4.2 Rational Inattention (Sims, 2003)

Sims (2003) formalized attention as a finite *information-processing capacity* measured in bits, drawing from Shannon information theory. The **rational inattention** framework models agents as choosing how to allocate their fixed channel capacity across signals, subject to an entropy cost:

```
max_{signal structure} E[U(action, state)] - κ · I(state; signal)
```

where κ > 0 is the cost per bit of mutual information acquired, and I(state; signal) is the mutual information between the true state and the observed signal.

Under rational inattention, agents *optimally choose* to remain ignorant about low-value signals — this is not a cognitive limitation but rational optimization over information acquisition costs.

**Citation**: Sims CA. Implications of Rational Inattention. *Journal of Monetary Economics*. 2003;50(3):665-690. [DOI: 10.1016/S0304-3932(03)00029-1](https://doi.org/10.1016/S0304-3932(03)00029-1)

---

### 4.3 Kőszegi & Matejka (2020): Attention-Based Mental Accounting

Kőszegi and Matejka (2020) provide the *direct formal derivation* of mental accounting from rational inattention. Their model: an agent faces multiple consumption goods with correlated price/quality shocks, and must allocate finite attention (measured as reduction in entropy) before making choices.

**Main results**:

1. **Budget formation**: When goods are sufficiently substitutable, the optimal attention allocation strategy generates *implicit budgets* — the agent pays attention to total expenditure on a category but not individual item prices, exactly replicating Thaler's budget-level mental accounting
2. **Naive diversification**: When goods are complements, the agent allocates a fixed mix without deliberating on exact quantities, generating the 1/N heuristic endogenously from rational inattention
3. **Water-filling algorithm**: The agent uses an information-theoretic water-filling allocation to direct attention toward signals with highest value (most uncertain, most consequential), completely ignoring signals below the threshold — producing the discontinuous, categorical structure of mental accounts

**Key equation** (water-filling): Attention allocated to dimension i is:

```
a_i = max(0, λ - 1/V_i)
```

where V_i is the value of information on dimension i and λ is a Lagrange multiplier on total attention budget. Dimensions with V_i < 1/λ receive zero attention — creating categorical boundaries from continuous utility.

**Citation**: Kőszegi B, Matejka F. Choice Simplification: A Theory of Mental Budgeting and Naive Diversification. *Quarterly Journal of Economics*. 2020;135(2):1153-1207. [DOI: 10.1093/qje/qjz043](https://doi.org/10.1093/qje/qjz043)

**Interpretation**: Mental accounting is not a bias imposed on an otherwise rational agent — it is the *optimal* information-processing strategy for an agent with finite attention who faces multiple correlated financial decisions. The account boundaries emerge endogenously from the water-filling solution.

---

## 5. Construal Level Theory (Trope & Liberman)

### 5.1 Core Theory

Construal Level Theory (CLT) posits that **psychological distance** on any dimension (temporal, spatial, social, hypothetical) systematically shifts the *level of abstraction* at which objects and events are mentally represented (Trope & Liberman, 2010):

* **Near construal (low level)**: Concrete, feasibility-focused, contextualized, idiosyncratic features salient
* **Far construal (high level)**: Abstract, desirability-focused, decontextualized, central/defining features salient

**Citation**: Trope Y, Liberman N. Construal-Level Theory of Psychological Distance. *Psychological Review*. 2010;117(2):440-463. [DOI: 10.1037/a0018963](https://doi.org/10.1037/a0018963). PMC: [PMC3152826](https://pmc.ncbi.nlm.nih.gov/articles/PMC3152826/)

---

### 5.2 CLT and Mental Account Time Horizons

The connection to mental accounting operates through *temporal distance*:

* **Current income account** (near): Low construal — concrete specific transactions, feasibility of spending, local context. Strong categorization of individual transactions as belonging to "this week's food budget" vs. "this week's entertainment."
* **Long-run savings account** (far): High construal — abstract representations of "security," "retirement," "financial freedom." Specific transactions within this account are not individually tracked; the category label dominates.
* **Windfall/exceptional account**: Windfalls are psychologically distant from normal income (different source, different causal history) — higher construal level, lower inhibition against spending. This mechanically explains Thaler's finding that windfall income is spent faster than earned income on non-necessities.

**Connection to narrow bracketing**: Kahneman's observation that investors evaluate portfolios at short intervals (narrow bracketing → myopic loss aversion; see Benartzi & Thaler, 1995) reflects dominance of near construal for active monitoring decisions. Adoption of annual rebalancing rules requires deliberate high-construal adoption — thinking abstractly about the portfolio as a whole rather than reacting to proximal price movements.

**CLT and account fungibility**: Two financial resources are more likely to be treated as fungible when both are psychologically distant (far construal, high abstraction). Psychological proximity differences (one current, one future; one local, one distant) generate non-fungibility as a construal-level artifact.

---

## 6. Schema Theory and Financial Cognition

### 6.1 Bartlett's Schema Theory

Bartlett (1932) introduced **schemata** as organized knowledge structures derived from past experience that actively shape the encoding, storage, and retrieval of new information. Schemata are:

* Reconstructive (not photographic): Memory is schema-driven inference, not storage
* Culturally transmitted: Acquired through social learning, vary across cultures
* Active during encoding: New information is assimilated to existing schemas, distorting it toward schema-consistent forms

**Citation**: Bartlett FC. *Remembering: A Study in Experimental and Social Psychology*. Cambridge University Press; 1932.

---

### 6.2 Financial Schemas as Mental Account Templates

Mental accounts are *instances* of financial schemata — culturally transmitted templates for categorizing money. Evidence for the schema basis:

* **Cross-cultural variation**: The specific accounts that are cognitively "natural" vary across cultures. In societies with strong gift-giving norms (East Asian contexts), "gift money" constitutes a separate mental account with distinct spending norms, whereas in Western contexts this categorization is weaker. Research by Darragh & Griskevicius (forthcoming) and related cross-cultural consumer research documents this variation.
* **Developmental acquisition**: Children acquire money schemata gradually — they first learn that money can be exchanged for goods (medium-of-exchange schema), then that money can be saved (store-of-value schema), then that different types of money have different norms (wage vs. gift vs. found money). This developmental sequence matches the structure of Thaler's accounts.
* **Schematic distortion**: Just as Bartlett's subjects reconstructed stories to fit cultural schemas, agents reconstruct financial histories to fit account boundaries. Expenses are mentally re-categorized post-hoc to maintain account balance integrity.

**Cultural variation example**: Studies of Indian households (Munshi, 2004; related to caste-based credit networks) document that social remittances follow different mental accounting rules than private income, and that the account categories themselves are socially regulated. Similarly, Zelizer (1994) in *The Social Meaning of Money* documented that earmarked money (e.g., household money controlled by women in 19th-century households) operated under distinct non-fungibility norms that were socially enforced.

**Citation**: Zelizer VA. *The Social Meaning of Money*. Basic Books; 1994. [Princeton University Press paperback: ISBN 9780691044590](https://press.princeton.edu/books/paperback/9780691044590/the-social-meaning-of-money)

---

## 7. Embodied Cognition and Conceptual Metaphor

### 7.1 Lakoff & Johnson: Conceptual Metaphor Theory

Lakoff and Johnson (1980, 1999) argued that abstract concepts are not primarily represented propositionally but are structured by **conceptual metaphors** — systematic mappings from concrete, embodied source domains to abstract target domains. These mappings are:

* **Grounded in sensorimotor experience**: Primary metaphors arise from recurring correlations between sensory-motor experience and abstract concepts (e.g., MORE IS UP grounds "rising prices," "elevated costs")
* **Productive**: Novel metaphorical inferences can be generated by extension of the mapping
* **Partially unconscious**: Speakers use conceptual metaphors without awareness

**Citation**: Lakoff G, Johnson M. *Metaphors We Live By*. University of Chicago Press; 1980. [Chicago Press](https://press.uchicago.edu/ucp/books/book/chicago/M/bo3637992.html)

**Citation**: Lakoff G, Johnson M. *Philosophy in the Flesh: The Embodied Mind and Its Challenge to Western Thought*. Basic Books; 1999.

---

### 7.2 MONEY IS WATER (Liquidity Metaphor)

The most pervasive financial conceptual metaphor maps money onto fluid dynamics:

| Linguistic Expression | Metaphorical Mapping |
|------------------------|----------------------|
| "cash flow" | money moves like water |
| "liquidity" / "liquid assets" | ability to flow freely |
| "frozen assets" | money in solid state, immobilized |
| "drowning in debt" | submerged by fluid accumulation |
| "capital pool" | money as contained volume |
| "dried up credit" | cessation of flow |
| "flood of money" | excess volume overwhelms container |

**Implication for mental accounting**: If money is cognitively represented as a *fluid contained in vessels*, then mental accounts are naturally conceived as *containers* — each with walls, capacity limits, and distinct contents. This embodied schema generates:

* **Non-fungibility**: Different containers hold different types of fluid — mixing them violates the schema (feels "wrong" even when economically neutral)
* **Account closure resistance**: Emptying a container is a salient event requiring justification; this maps to the psychological resistance against closing positions at a loss
* **Budget saturation**: A container that is "full" (account exhausted) blocks further spending even if other containers have surplus — the bucket-level evaluation documented by Thaler

---

### 7.3 WEALTH IS WEIGHT / ECONOMIC DIFFICULTY IS BURDEN

Secondary financial metaphors map onto physical weight experience:

* "heavy debt burden"
* "weighed down by financial obligations"
* "light on cash"
* "carrying a lot of financial risk"

Embodied simulation research (Jostmann et al., 2009) demonstrated that *physical weight primes importance-related cognition* — participants holding heavy clipboards rated currencies and decisions as more important. This suggests the metaphor is not merely linguistic but computationally active.

**Citation**: Jostmann NB, Lakens D, Schubert TW. Weight as an Embodiment of Importance. *Psychological Science*. 2009;20(9):1169-1174. [DOI: 10.1111/j.1467-9280.2009.02426.x](https://doi.org/10.1111/j.1467-9280.2009.02426.x)

---

### 7.4 Grounded Cognition Account of Financial Decision-Making

The grounded cognition framework (Barsalou, 2008) predicts that financial representations partially consist of **perceptual simulations** — reactivations of sensorimotor patterns from prior experience with money-related objects:

* Handling physical cash activates tactile and weight representations; credit card transactions lack this grounding → pain-of-paying is attenuated for cards (Prelec & Simester, 2001; [DOI: 10.1023/A:1008196717017](https://doi.org/10.1023/A:1008196717017))
* Digital numbers on a screen are even more decontextualized → further pain-of-paying reduction → increased spending relative to equivalent cash transactions
* The source-of-funds tagging in mental accounting may partially reflect grounded simulations of *how the money was obtained* (physical labor = embodied memory of effort = higher retention threshold)

**Citation**: Barsalou LW. Grounded Cognition. *Annual Review of Psychology*. 2008;59:617-645. [DOI: 10.1146/annurev.psych.59.103006.093629](https://doi.org/10.1146/annurev.psych.59.103006.093629)

---

## 8. Integrated Mechanistic Model

The seven frameworks above are not competing explanations but complementary mechanistic layers operating at different levels of description:

```
Level 1 (Embodied substrate):
  MONEY IS WATER metaphor → container schema → account boundaries feel natural

Level 2 (Cognitive architecture):
  Type 1 default assigns money to containers; Type 2 can override at cost
  Stanovich autonomous mind: immediate categorization
  Stanovich algorithmic mind: capacity for fungibility calculation
  Stanovich reflective mind: disposition to engage Type 2

Level 3 (Attention allocation):
  Finite attention (Kahneman 1973) → cannot monitor all positions
  Rational inattention (Sims 2003) → optimal to ignore low-value signals
  Water-filling solution (Kőszegi & Matejka 2020) → categorical budgets emerge

Level 4 (Computational constraint):
  Simon's bounded rationality → satisficing over account-level aspiration levels
  Sweller's cognitive load → accounts reduce working-memory demand from O(N) to O(K)
  Miller's 7±2 → K accounts fits in working memory, N transactions does not

Level 5 (Psychological distance):
  CLT (Trope & Liberman 2010) → near vs. far construal creates fungibility discontinuities
  Time horizon of account matches construal level of representation

Level 6 (Cultural transmission):
  Bartlett schemas → account categories are culturally transmitted templates
  Zelizer → social norms enforce non-fungibility of earmarked money
```

**Debiasing implication**: An intervention that operates at only one level will be partially effective at best. For example:

* Financial education (Level 4 — adding cognitive resources) reduces but does not eliminate mental accounting because the Type 1 defaults (Level 2) and embodied metaphors (Level 1) remain active
* Forcing System 2 engagement via cooling-off periods reduces mental accounting in low-cognitive-load contexts but not under stress (Level 3 — attention constraint dominates under arousal)
* Portfolio aggregation displays (reduce CLT distance, Level 5) reduce narrow bracketing but do not eliminate it because the underlying container schema (Level 1) generates account reconstruction

The most powerful debiasing combines: (a) explicit fungibility instruction that engages the reflective mind, (b) portfolio-level displays that reduce construal distance, and (c) pre-commitment devices that use mental account structure *with* rather than against the agent's goals (e.g., labeled savings accounts for specific goals exploit the container schema productively).

---

## Cross-References

* Core framework: `core-research/mental-accounting-thaler-comprehensive.md`
* Rational inattention application: `core-research/fungibility-asset-transformation-rational-framework.md`
* Disposition effect and loss aversion: `core-research/behavioral-biases-multi-paper-synthesis.md`
* Debiasing implementations: `debiasing-frameworks/`

---

## Bibliography (New Citations from This Document)

| Citation | Reference | DOI |
|----------|-----------|-----|
| Evans & Stanovich (2013) | Evans JSTB, Stanovich KE. Dual-Process Theories of Higher Cognition: Advancing the Debate. *Perspectives on Psychological Science* 8(3):223-241. | [10.1177/1745691612460685](https://doi.org/10.1177/1745691612460685) |
| Evans (2008) | Evans JSTB. Dual-Processing Accounts of Reasoning, Judgment, and Social Cognition. *Annual Review of Psychology* 59:255-278. | [10.1146/annurev.psych.59.103006.093629](https://doi.org/10.1146/annurev.psych.59.103006.093629) |
| Stanovich (2009) | Stanovich KE. Distinguishing the reflective, algorithmic, and autonomous minds. In Evans & Frankish, eds. *In Two Minds*. OUP. | — |
| Stanovich (2011) | Stanovich KE. *Rationality and the Reflective Mind*. Oxford University Press. | ISBN 9780195341140 |
| Simon (1955) | Simon HA. A Behavioral Model of Rational Choice. *Quarterly Journal of Economics* 69(1):99-118. | [10.2307/1884852](https://doi.org/10.2307/1884852) |
| Simon (1956) | Simon HA. Rational Choice and the Structure of the Environment. *Psychological Review* 63(2):129-138. | [10.1037/h0042769](https://doi.org/10.1037/h0042769) |
| Gigerenzer & Todd (1999) | Gigerenzer G, Todd PM, ABC Research Group. *Simple Heuristics That Make Us Smart*. OUP. | ISBN 9780195143812 |
| Gigerenzer (2008) | Gigerenzer G. Why Heuristics Work. *Perspectives on Psychological Science* 3(1):20-29. | [10.1111/j.1745-6916.2008.00058.x](https://doi.org/10.1111/j.1745-6916.2008.00058.x) |
| DeMiguel et al. (2009) | DeMiguel V, Garlappi L, Uppal R. Optimal Versus Naive Diversification. *Review of Financial Studies* 22(5):1915-1953. | [10.1093/rfs/hhm075](https://doi.org/10.1093/rfs/hhm075) |
| Miller (1956) | Miller GA. The Magical Number Seven, Plus or Minus Two. *Psychological Review* 63(2):81-97. | [10.1037/h0043158](https://doi.org/10.1037/h0043158) |
| Sweller (1988) | Sweller J. Cognitive Load During Problem Solving: Effects on Learning. *Cognitive Science* 12(2):257-285. | [10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4) |
| Shamosh & Gray (2008) | Shamosh NA, Gray JR. Delay Discounting and Intelligence: A Meta-Analysis. *Intelligence* 36(4):289-305. | [10.1016/j.intell.2007.09.004](https://doi.org/10.1016/j.intell.2007.09.004) |
| Kahneman (1973) | Kahneman D. *Attention and Effort*. Prentice-Hall. | — |
| Trope & Liberman (2010) | Trope Y, Liberman N. Construal-Level Theory of Psychological Distance. *Psychological Review* 117(2):440-463. | [10.1037/a0018963](https://doi.org/10.1037/a0018963) |
| Bartlett (1932) | Bartlett FC. *Remembering*. Cambridge University Press. | — |
| Zelizer (1994) | Zelizer VA. *The Social Meaning of Money*. Basic Books. | ISBN 9780691044590 |
| Lakoff & Johnson (1980) | Lakoff G, Johnson M. *Metaphors We Live By*. University of Chicago Press. | — |
| Lakoff & Johnson (1999) | Lakoff G, Johnson M. *Philosophy in the Flesh*. Basic Books. | — |
| Jostmann et al. (2009) | Jostmann NB, Lakens D, Schubert TW. Weight as an Embodiment of Importance. *Psychological Science* 20(9):1169-1174. | [10.1111/j.1467-9280.2009.02426.x](https://doi.org/10.1111/j.1467-9280.2009.02426.x) |
| Barsalou (2008) | Barsalou LW. Grounded Cognition. *Annual Review of Psychology* 59:617-645. | [10.1146/annurev.psych.59.103006.093629](https://doi.org/10.1146/annurev.psych.59.103006.093629) |

---

*This document is part of the rational-trading-behavioral-finance knowledge base. See BIBLIOGRAPHY.md for the complete citation registry.*
