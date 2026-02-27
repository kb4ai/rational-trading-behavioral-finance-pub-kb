# Behavioral Biases: Multi-Paper Synthesis

> **A comprehensive overview of foundational papers on framing effects, disposition effect, mental accounting, and cognitive biases in trading**

[Collected 2026-01-23 via ChatGPT 5.2]

## Research Conversations

* <https://chatgpt.com/s/t_6973612511e4819199d76226b8e9f5b7>
* <https://chatgpt.com/share/69735fcb-956c-8007-bd48-5e652b186cbc>

---

## Papers Covered

| Citation | DOI |
|----------|-----|
| De Martino et al. 2008 | <https://doi.org/10.1523/JNEUROSCI.2895-08.2008> |
| Grinblatt et al. 2012 | <https://doi.org/10.1016/j.jfineco.2011.05.016> |
| Odean 1998 | <https://doi.org/10.1111/0022-1082.00072> |
| Barber & Odean 2000 | <https://doi.org/10.1111/0022-1082.00226> |
| Thaler 1985 | <https://doi.org/10.1287/mksc.4.3.199> |
| Samuelson & Zeckhauser 1988 | <https://doi.org/10.1007/BF00055564> |
| Yafai, Verrier & Reidy 2014 | <https://doi.org/10.1177/1362361313508023> |

---

## The Big Picture (Why Anyone Should Care)

Imagine two signs pointing to the **same** door, but one sign says "KEEP £20" and the other says "LOSE £30," and—annoyingly—people often walk through different doors depending on which sign they read.
In decision theory terms, that's a **framing effect**: preferences change when you re-describe identical outcomes as gains versus losses, violating description invariance.

Some autistic people, on average, seem **less tugged around by the wording** and more likely to make the same choice across frames.
In De Martino et al. (2008), the autism-spectrum group showed a smaller shift in risk-taking between gain vs loss wording than controls, meaning **more logical consistency** across equivalent descriptions. ([PubMed][1])

That sounds like a superpower—until you notice that in real life, "the frame" often *is* part of the social world (tone, implication, what's *meant*).
The authors argue the reduced framing sensitivity may reflect **reduced incorporation of emotional context** during choice, which can be helpful in some tasks and costly in others. ([PubMed][1])

And this isn't just about money gambles: a related pattern shows up in a social setting too.
In a child-friendly Asch-style conformity task, autistic children were **less likely to conform** when misled about the "majority answer," and autism traits (AQ) correlated negatively with conformity in the typically-developing group. ([PubMed][2])

So, if you zoom out: these papers collectively paint a theme—**context pressure** (emotional framing, majority opinion, defaults) can steer human choice, but people differ a lot in how strongly they're steered.
Behavioral economics and finance then show what these nudges can do at scale: they affect trading decisions, taxes, risk exposure, and long-run returns. ([Haas Faculty][3])

---

## First Important Correction (About That "65–80% Reduced" Claim)

If someone says "autistic individuals show **65–80% reduced susceptibility**," your brain should do a quick sanity check: "Reduced compared to what measure?"
In De Martino et al. (2008), the paper reports a framing-susceptibility index (difference in gambling between loss and gain frames) of **7.66% (ASD) vs 14.24% (controls)**, which is roughly a **46% reduction** (because 7.66 is about 54% of 14.24). ([PubMed][1])

That doesn't mean the 65–80% statement is always malicious—it may come from a different way of computing effect size, a subgroup comparison, or a secondary summary that used a different denominator.
But if you're quoting De Martino (2008) directly, the headline numbers they print support "about half as large," not "down to a fifth." ([PubMed][1])

---

## What De Martino et al. (2008) Actually Did (Slowly Unfolding the Mechanics)

They used a **simple money-choice task**: on each trial you start with an amount (e.g., "you receive £50") and choose between a **sure option** and a **gamble**.
Formally, the key trick is that the **sure option** is framed either as what you **keep** (gain frame) or what you **lose** (loss frame), while the **gamble option stays identical** in both frames (same probabilities), so any shift is due to framing, not math. ([PubMed][1])

If you're listening with a "practical" brain: the task is basically testing whether your choice follows the *numbers* or follows the *story the wording suggests*.
If you're listening with a "stats" brain: they analyzed choices with ANOVAs showing a strong main effect of frame and a **group × frame interaction**, meaning the ASD group's frame-driven shift was significantly smaller. ([PubMed][1])

They quantified "susceptibility" as **how much more often you gamble in the loss frame than in the gain frame**.
Concretely, controls gambled **43.75%** in gain frame vs **57.99%** in loss frame, while the ASD group gambled **34.52%** vs **42.19%**, respectively. ([PubMed][1])

So both groups still show the classic pattern—more risk-seeking when a sure option is described as a loss—but the ASD group shows **less swing**.
Statistically, that critical interaction was significant (reported as **F(1,27)=6.56, p<0.02** for the 2×2 ANOVA), consistent with "reduced susceptibility," not zero susceptibility. ([PubMed][1])

Now the "neuro-ish / body" layer: they also recorded **skin conductance response (SCR)** as a physiological proxy for emotional arousal.
They found the control group showed a positive differential SCR to loss vs gain framing (about **0.071 μS**), whereas the ASD group did not (about **−0.019 μS**), and the group difference was significant in their reported ANOVA (e.g., **F(1,23)=4.86, p<0.05**). ([PubMed][1])

If you prefer an intuitive translation: the wording "loss" vs "keep" changed not only choices but also bodies in controls, and it changed bodies much less in the ASD group.
If you prefer a mechanistic translation: the authors interpret this as reduced coupling between **affective context signals** and decision policy, yielding higher description invariance but potentially less use of socially meaningful context. ([PubMed][1])

**Who were the participants?** Fourteen autistic and fifteen control participants, matched on age/sex/IQ, and they also used clinical/trait measures like ADOS plus cognitive-style questionnaires (Need for Cognition, Cognitive Reflection Test) in the associated study description. ([imfar.confex.com][4])

---

## Social Pressure Version: Yafai, Verrier & Reidy (2014)

They translated the classic conformity setup into something kids can do without actors in a room: a **line-length judgment task**.
Method-wise: **15 autistic children** and **15 typically-developing children** (matched for age, gender, numeracy, literacy) chose which of three lines matched a target line. ([PubMed][2])

On some trials, the child was misled about what "most people" supposedly answered.
The main result is straightforward: autistic children were **much less likely to conform** to the misleading "majority" than typically-developing children, and higher autism traits predicted less conformity in the TD group too. ([PubMed][2])

If you connect this to framing: "the crowd says X" is another kind of frame—social, not financial.
Technically, it's a manipulation of **informational/normative influence**, and the result suggests reduced weighting of that social-context cue (on average). ([PubMed][2])

---

## The Finance Papers: The Same *Family* of Effects, but in Markets

### Odean (1998): The Disposition Effect (Sell Winners, Hold Losers)

In real brokerage data, many investors behave as if realizing a loss "makes it real," so they postpone it.
Odean operationalizes this with **PGR vs PLR**: proportion of gains realized vs proportion of losses realized, using **10,000 accounts** at a large discount broker (trades from 1987–1993 in the paper's description). ([Haas Faculty][3])

The signature finding: **PGR ≈ 0.148** and **PLR ≈ 0.098**, so people realize gains more readily than losses, and the difference is highly significant (he reports a very large t-statistic). ([Haas Faculty][3])

If you want the link back to framing: a paper gain feels like a "win account," a paper loss feels like a "don't look at it account," and that mental labeling changes action even when taxes would recommend the opposite.
In the paper's interpretation, the behavior is inconsistent with simple rebalancing stories and not justified by later performance; it also interacts with **tax-loss selling**, especially around December. ([Haas Faculty][3])

### Barber & Odean (2000): Trading Too Much Is Costly

This one is about a different bias-family: action bias/overconfidence—trading feels productive even when it quietly bleeds returns.
They analyze **66,465 households** at a discount broker (1991–1996) and show that the most active traders earn **~11.4%** annual return while the market earns **~17.9%** over the same period; the average household turns over **~75%** of its portfolio annually.

So: even if you're "right sometimes," costs and timing errors stack up.
Mechanistically, the story is that excessive trading plus transaction costs plus poor selection/timing can dominate any small edge, consistent with overconfidence-driven volume.

### Grinblatt et al. (2012): IQ and Bias-Susceptibility in the Wild

This paper asks: do cognitive differences predict *who* is more prone to these mistakes?
They combine Finnish conscription **IQ scores** (administered to nearly all Finnish males of draft age) with trading/limit-order-book data, and report that higher-IQ investors are less subject to the **disposition effect**, more engaged in **tax-loss trading**, and more likely to **supply liquidity** (e.g., around one-month highs). ([ScienceDirect][5])

They also report superior market timing, stock picking, and trade execution for higher-IQ investors, after controls.
Technically, it's an observational design with extensive controls; it does not prove IQ "causes" good trading, but it strongly supports that cognitive variation tracks systematic differences in bias exposure and performance. ([ScienceDirect][5])

---

## The "Defaults and Labels" Layer: Thaler (1985) and Samuelson & Zeckhauser (1988)

### Thaler (1985): Mental Accounting—Money Gets Labels

Think of mental accounting like folders in your brain: "windfall," "savings," "treat," "rent," even though money is physically interchangeable.
Thaler builds a model where choices depend on **how gains/losses are coded** (using ideas from prospect theory), introduces **transaction utility** (how good a deal feels relative to a reference price), and discusses budgeting/self-control. ([Bear Warrington][6])

He starts with vivid anecdotes: a "lost fish" reimbursement gets spent on a fancy dinner, or people carry expensive debt while holding "savings" untouched—because the accounts are psychologically separate.
That's the same core pattern as framing: not just *what* you get, but *what mental category it lands in* changes the choice. ([Bear Warrington][6])

### Samuelson & Zeckhauser (1988): Status Quo Bias—Doing Nothing Is a Powerful Option

Many real decisions include a "keep things as they are" option, and people disproportionately stick with it.
They report a series of experiments showing status quo bias, and point to real-world choices like health plans and retirement programs where defaults/status quo have substantial pull. ([IDEAS/RePEc][7])

If you translate it into the framing family: the default makes alternatives feel like potential losses or regrets.
In decision-theory terms, the status quo becomes the **reference point**, and deviations are evaluated as changes that risk loss, effort, or blame. ([IDEAS/RePEc][7])

---

## So What's the Shared "Mechanism Idea" Across All These?

A very human pattern is: the brain often uses **context cues** (wording, social consensus, default options, category labels) as shortcuts that shape value and action.
In De Martino (2008) and Yafai (2014), autistic groups showed **reduced weighting** of particular context cues (emotional framing; majority pressure), which can look like increased consistency or independence. ([PubMed][1])

In the market papers, those same kinds of cues can become expensive: "this is a winner," "this is a loser," "I should do something," "I'll wait," "that gain is mine," "that loss isn't real yet."
And the empirical finance literature shows these patterns at scale—measurable in trade logs and returns, not just lab tasks. ([Haas Faculty][3])

One caution that matters for autistic listeners: these are **group averages** from specific samples and tasks, not a statement about any individual's destiny.
Even in De Martino's data, the ASD group still shows some framing effect (just smaller), and the interpretation includes both potential advantages (consistency) and disadvantages (reduced use of emotional/social context). ([PubMed][1])

---

## "Mechanical Details" Cheat-Sheet (What Was Measured, Exactly)

### De Martino et al. (2008) — Framing in Risky Choice + Physiology

* Task: choose **sure vs gamble** after being given an endowment; sure option framed as "keep £X" (gain) vs "lose £Y" (loss); gamble identical across frames. ([PubMed][1])
* Participants: **14 autistic, 15 controls**, matched on age/sex/IQ (per study description). ([imfar.confex.com][4])
* Primary behavioral metric: "susceptibility" = (gambling% loss frame − gambling% gain frame). ([PubMed][1])
* Key numbers: susceptibility **7.66% ±1.95** (ASD) vs **14.24% ±1.68** (controls); group×frame interaction significant. ([PubMed][1])
* Physiology: **SCR** difference loss vs gain present in controls (~0.071 μS) but absent in ASD (~−0.019 μS), interpreted as reduced emotional-context incorporation. ([PubMed][1])

### Yafai, Verrier & Reidy (2014) — Social Conformity

* Task: line-length matching; on some trials participants are misled about "what most people answered." ([PubMed][2])
* Participants: **15 autistic children, 15 typically-developing**, matched on age/gender/numeracy/literacy. ([PubMed][2])
* Outcome: autistic children **conformed less** in misleading condition; AQ traits negatively correlated with conformity in TD group. ([PubMed][2])

### Odean (1998) — Disposition Effect in Brokerage Records

* Data: trades from **10,000 accounts** at a discount broker. ([Haas Faculty][3])
* Metric: **PGR vs PLR** (proportion of gains realized vs losses realized). ([Haas Faculty][3])
* Key result: PGR **0.148** > PLR **0.098**, strong preference for realizing winners. ([Haas Faculty][3])

### Barber & Odean (2000) — Overtrading and Performance

* Data: **66,465 households** (1991–1996) at a discount broker.
* Key results: most-active traders ~**11.4%** annual return vs market ~**17.9%**; average household turnover ~**75%** annually.

### Grinblatt et al. (2012) — IQ and Trading Behavior/Performance

* Data: Finnish conscription **IQ test scores** + trading and limit order book data; extensive controls. ([ScienceDirect][5])
* Findings (reported in abstract/preview): higher IQ → less disposition effect, more tax-loss trading, more liquidity provision; plus better timing/picking/execution. ([ScienceDirect][5])

### Thaler (1985) — Mental Accounting (Conceptual + Evidence Snippets)

* Core idea: people violate fungibility because money is mentally labeled; model uses prospect-theory coding and introduces **transaction utility**. ([Bear Warrington][6])
* Evidence style: anecdotes and choice questions showing preferences depend on how gains/losses are grouped or labeled. ([Bear Warrington][6])

### Samuelson & Zeckhauser (1988) — Status Quo Bias

* Claim: people disproportionately stick with the **status quo**; supported by experiments and real-world plan selection contexts. ([IDEAS/RePEc][7])

---

## Presentation Note

> If you tell me the setting (talk at a meetup? classroom? therapy group? finance/tech audience?) and the target length (3 minutes vs 30 minutes), I can reshape this into a spoken script with timing, pauses, and "audience check-in" questions—without losing the alternating accessible/technical rhythm.

---

## References

[1]: https://pubmed.ncbi.nlm.nih.gov/18923049/ "Explaining enhanced logical consistency during decision making in autism - PubMed"
[2]: https://pubmed.ncbi.nlm.nih.gov/24126871/ "Social conformity and autism spectrum disorder: a child-friendly take on a classic study - PubMed"
[3]: https://faculty.haas.berkeley.edu/odean/papers%20current%20versions/areinvestorsreluctant.pdf "No Job Name"
[4]: https://imfar.confex.com/imfar/2008/techprogram/P2468.HTM?utm_source=chatgpt.com "Enhanced Rationality & Behavioral Invariance in Autism"
[5]: https://www.sciencedirect.com/science/article/abs/pii/S0304405X1100211X "IQ, trading behavior, and performance - ScienceDirect"
[6]: https://bear.warrington.ufl.edu/brenner/mar7588/Papers/thaler-mktsci1985.pdf "Mental Accounting and Consumer Choice"
[7]: https://ideas.repec.org/a/kap/jrisku/v1y1988i1p7-59.html "Status Quo Bias in Decision Making"

* De Martino, B., Harrison, N.A., Knafo, S., Bird, G., & Dolan, R.J. (2008). Explaining Enhanced Logical Consistency during Decision Making in Autism. *Journal of Neuroscience*, 28(42), 10746-10750. [DOI: 10.1523/JNEUROSCI.2895-08.2008](https://doi.org/10.1523/JNEUROSCI.2895-08.2008)
* Yafai, A.F., Verrier, D., & Reidy, L. (2014). Social conformity and autism spectrum disorder: A child-friendly take on a classic study. *Autism*, 18(8), 1007-1013. [DOI: 10.1177/1362361313508023](https://doi.org/10.1177/1362361313508023)
* Odean, T. (1998). Are Investors Reluctant to Realize Their Losses? *Journal of Finance*, 53(5), 1775-1798. [DOI: 10.1111/0022-1082.00072](https://doi.org/10.1111/0022-1082.00072)
* Barber, B.M., & Odean, T. (2000). Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors. *Journal of Finance*, 55(2), 773-806. [DOI: 10.1111/0022-1082.00226](https://doi.org/10.1111/0022-1082.00226)
* Thaler, R. (1985). Mental Accounting and Consumer Choice. *Marketing Science*, 4(3), 199-214. [DOI: 10.1287/mksc.4.3.199](https://doi.org/10.1287/mksc.4.3.199)
* Samuelson, W., & Zeckhauser, R. (1988). Status quo bias in decision making. *Journal of Risk and Uncertainty*, 1(1), 7-59. [DOI: 10.1007/BF00055564](https://doi.org/10.1007/BF00055564)
* Grinblatt, M., Keloharju, M., & Linnainmaa, J. (2012). IQ, trading behavior, and performance. *Journal of Financial Economics*, 104(2), 339-362. [DOI: 10.1016/j.jfineco.2011.05.016](https://doi.org/10.1016/j.jfineco.2011.05.016)
