#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# ///
"""
Multi-Denomination Portfolio Tracker
=====================================
Implementation of the N-dimensional valuation method from:
  core-research/multi-denomination-portfolio-valuation.md

Demonstrates denomination-invariant growth metric G(t₀,t₁) and
per-denominator growth vector diagnostics.

Part of: https://github.com/kb4ai/rational-trading-behavioral-finance-pub-kb/issues/5

Mathematical Framework
----------------------
For a portfolio containing assets, evaluate total portfolio value
projected into every denominator:

  V_d(t) = Σᵢ (qᵢ × price_i(t)) / price_d(t)

Denomination-invariant growth metric:

  G(t₀, t₁) = min_d { V_d(t₁) / V_d(t₀) }   for all d ∈ D

Per-denominator growth vector:

  g(t₀, t₁) = [ V_d₁(t₁)/V_d₁(t₀), ..., V_dₙ(t₁)/V_dₙ(t₀) ]

If G > 1: genuine growth across all dimensions.
If G < 1: at least one denomination shows contraction.
Divergence between growth vector components signals denomination-dependent
performance — a red flag for single-denomination bias.

Key Insight
-----------
For a *static* long-only portfolio denominated in its own constituents,
G ≤ 1 always holds (the portfolio return is a weighted average of individual
asset returns, bounded by the maximum).  G > 1 requires either:
  (a) active trading that generates alpha, or
  (b) denominators external to the portfolio.
Scenario 1 demonstrates (a); scenarios 2-3 use static portfolios where G < 1
reveals denomination-dependent illusions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Portfolio:
    """Holdings: mapping of asset symbol to quantity held."""
    holdings: Dict[str, float] = field(default_factory=dict)

    def describe(self) -> str:
        parts = [f"  {sym}: {qty}" for sym, qty in sorted(self.holdings.items())]
        return "\n".join(parts)


@dataclass
class MarketSnapshot:
    """Prices of every asset at a single point in time (quoted in a common
    numeraire, e.g. USD, but any consistent unit works)."""
    label: str                         # human-readable timestamp / label
    prices: Dict[str, float] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Core computations
# ---------------------------------------------------------------------------

def compute_denominated_values(
    portfolio: Portfolio,
    snapshot: MarketSnapshot,
    denominators: List[str],
) -> Dict[str, float]:
    """Compute V_d(t) for each denominator d.

    V_d(t) = Σᵢ (qᵢ × price_i(t)) / price_d(t)

    Returns a dict  {denominator_symbol: portfolio_value_in_that_denom}.
    """
    # Total portfolio value in the raw numeraire of the snapshot
    raw_value = sum(
        qty * snapshot.prices[sym]
        for sym, qty in portfolio.holdings.items()
    )
    return {
        d: raw_value / snapshot.prices[d]
        for d in denominators
    }


def growth_vector(
    values_t0: Dict[str, float],
    values_t1: Dict[str, float],
) -> Dict[str, float]:
    """Per-denominator growth vector g(t₀, t₁).

    g_d = V_d(t₁) / V_d(t₀)  for each denominator d.
    """
    return {
        d: values_t1[d] / values_t0[d]
        for d in values_t0
    }


def min_growth_metric(growth_vec: Dict[str, float]) -> float:
    """Denomination-invariant growth metric.

    G(t₀, t₁) = min_d { V_d(t₁) / V_d(t₀) }

    G > 1  →  genuine growth in every denomination.
    G < 1  →  at least one denomination shows contraction.
    """
    return min(growth_vec.values())


def divergence_alert(
    growth_vec: Dict[str, float],
    threshold: float = 0.05,
) -> List[str]:
    """Flag denomination pairs whose growth rates diverge beyond *threshold*.

    Large divergence means performance is denomination-dependent — the trader
    may be fooled by choosing a flattering denominator.
    """
    alerts: List[str] = []
    symbols = sorted(growth_vec.keys())
    for i, a in enumerate(symbols):
        for b in symbols[i + 1:]:
            diff = abs(growth_vec[a] - growth_vec[b])
            if diff > threshold:
                alerts.append(
                    f"  {a} vs {b}: growth differs by {diff:+.4f} "
                    f"({a}={growth_vec[a]:.4f}, {b}={growth_vec[b]:.4f})"
                )
    return alerts


# ---------------------------------------------------------------------------
# Scenario runner
# ---------------------------------------------------------------------------

def run_scenario(
    title: str,
    portfolio_t0: Portfolio,
    portfolio_t1: Optional[Portfolio],
    snap_t0: MarketSnapshot,
    snap_t1: MarketSnapshot,
    denominators: List[str],
    interpretation: str,
) -> None:
    """Execute one scenario and print full diagnostics.

    If portfolio_t1 is None, the portfolio is static (same holdings at both
    times).  If provided, it represents the result of active trading.
    """
    if portfolio_t1 is None:
        portfolio_t1 = portfolio_t0

    sep = "=" * 60
    print(f"\n{sep}")
    print(f"SCENARIO: {title}")
    print(sep)

    # Portfolio composition
    print(f"\nPortfolio at {snap_t0.label}:\n{portfolio_t0.describe()}")
    if portfolio_t1 is not portfolio_t0:
        print(f"\nPortfolio at {snap_t1.label} (after trading):\n{portfolio_t1.describe()}")

    # Denominated values at t₀ and t₁
    vals_t0 = compute_denominated_values(portfolio_t0, snap_t0, denominators)
    vals_t1 = compute_denominated_values(portfolio_t1, snap_t1, denominators)

    print(f"\nValues at {snap_t0.label}:")
    for d in denominators:
        print(f"  In {d}: {vals_t0[d]:>12.4f}")

    print(f"\nValues at {snap_t1.label}:")
    for d in denominators:
        print(f"  In {d}: {vals_t1[d]:>12.4f}")

    # Growth vector
    gv = growth_vector(vals_t0, vals_t1)
    print("\nPer-denominator growth rates:")
    for d in denominators:
        pct = (gv[d] - 1) * 100
        arrow = "+" if pct >= 0 else ""
        print(f"  {d}: {gv[d]:.4f}  ({arrow}{pct:.2f}%)")

    # Min-growth metric
    g = min_growth_metric(gv)
    print(f"\nMin-growth metric G = {g:.4f}", end="")
    if g > 1:
        print("  --> GENUINE GROWTH (G > 1)")
    elif g == 1.0:
        print("  --> FLAT (G = 1)")
    else:
        print("  --> CONTRACTION detected (G < 1)")

    # Divergence alerts
    alerts = divergence_alert(gv)
    if alerts:
        print("\nDivergence alerts (threshold=5%):")
        for a in alerts:
            print(a)
    else:
        print("\nNo significant divergence between denominators.")

    # Interpretation
    print(f"\nInterpretation:\n  {interpretation}")
    print()


# ---------------------------------------------------------------------------
# Sample scenarios with hardcoded data
# ---------------------------------------------------------------------------

def main() -> None:
    print("Multi-Denomination Portfolio Tracker")
    print("=" * 60)
    print("Demonstrates denomination-invariant growth analysis.")
    print("Reference: core-research/multi-denomination-portfolio-valuation.md")

    denominators = ["USD", "BTC", "ETH"]

    # ------------------------------------------------------------------
    # Scenario 1: Genuine Growth (active trading)
    #
    # The trader correctly rotated from USD into crypto before a rally.
    # Because quantities changed (active alpha), G > 1 is achievable.
    # Note: for a *static* portfolio denominated in its own assets,
    # G ≤ 1 always (portfolio return ≤ max component return).
    # ------------------------------------------------------------------
    run_scenario(
        title="Genuine Growth — active trading yields alpha across all denominators",
        portfolio_t0=Portfolio(holdings={"BTC": 1.0, "ETH": 10.0, "USD": 50_000.0}),
        portfolio_t1=Portfolio(holdings={"BTC": 3.0, "ETH": 12.0, "USD": 5_000.0}),
        snap_t0=MarketSnapshot(
            label="t₀ (Jan)",
            prices={"BTC": 40_000, "ETH": 2_500, "USD": 1.0},
        ),
        snap_t1=MarketSnapshot(
            label="t₁ (Jun)",
            # BTC +30%, ETH +28%
            prices={"BTC": 52_000, "ETH": 3_200, "USD": 1.0},
        ),
        denominators=denominators,
        interpretation=(
            "The trader actively rotated from USD into crypto before the "
            "rally, growing the portfolio in EVERY denomination — USD, BTC, "
            "and ETH. G > 1 confirms genuine alpha from skill, not just "
            "riding a single asset's appreciation. Note: for a static "
            "(buy-and-hold) portfolio, G > 1 is mathematically impossible "
            "when denominating in the portfolio's own assets; active trading "
            "is required to beat every denominator simultaneously."
        ),
    )

    # ------------------------------------------------------------------
    # Scenario 2: Denomination Divergence
    # USD value up, but BTC-denominated value down — riding USD
    # appreciation relative to BTC, not generating alpha.
    # ------------------------------------------------------------------
    run_scenario(
        title="Denomination Divergence — USD up, BTC down",
        portfolio_t0=Portfolio(holdings={"BTC": 0.5, "ETH": 5.0, "USD": 80_000.0}),
        portfolio_t1=None,
        snap_t0=MarketSnapshot(
            label="t₀ (Jan)",
            prices={"BTC": 40_000, "ETH": 2_500, "USD": 1.0},
        ),
        snap_t1=MarketSnapshot(
            label="t₁ (Jun)",
            # BTC doubles, ETH +80%, USD stable.
            # Portfolio is heavily USD-weighted, so in USD terms it looks
            # okay, but in BTC/ETH terms it badly underperformed.
            prices={"BTC": 80_000, "ETH": 4_500, "USD": 1.0},
        ),
        denominators=denominators,
        interpretation=(
            "A USD-only trader sees the portfolio as roughly flat or slightly "
            "up and feels fine. But measured in BTC the portfolio LOST value — "
            "holding mostly USD while BTC doubled is a massive opportunity "
            "cost. The divergence alert flags that 'growth' is denomination-"
            "dependent, not genuine alpha."
        ),
    )

    # ------------------------------------------------------------------
    # Scenario 3: Hidden Loss
    # Portfolio appears up in one denomination but is actually down in
    # most others — denomination bias masks underperformance.
    # ------------------------------------------------------------------
    run_scenario(
        title="Hidden Loss — appears up in USD, down in BTC and ETH",
        portfolio_t0=Portfolio(holdings={"BTC": 0.1, "ETH": 2.0, "USD": 90_000.0}),
        portfolio_t1=None,
        snap_t0=MarketSnapshot(
            label="t₀ (Jan)",
            prices={"BTC": 50_000, "ETH": 3_000, "USD": 1.0},
        ),
        snap_t1=MarketSnapshot(
            label="t₁ (Jun)",
            # Crypto rallies hard: BTC +100%, ETH +133%.
            # Portfolio is 90% USD, so USD value barely budges up,
            # but in BTC/ETH terms it collapses.
            prices={"BTC": 100_000, "ETH": 7_000, "USD": 1.0},
        ),
        denominators=denominators,
        interpretation=(
            "The portfolio's USD value rose slightly (crypto holdings "
            "appreciated), giving a false sense of security. But in BTC "
            "and ETH terms, the portfolio's value roughly halved — the "
            "trader missed a massive crypto rally by sitting in fiat. "
            "G < 1 correctly flags this as a loss. A single-denomination "
            "(USD) view completely masks the underperformance."
        ),
    )


if __name__ == "__main__":
    main()
