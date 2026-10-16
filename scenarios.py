#!/usr/bin/env python3
"""Scenario analysis for revenue and costs."""

def scenario_model(base_revenue, base_cost, growth_rates):
    results = {}
    for name, growth in growth_rates.items():
        rev = base_revenue * (1 + growth)
        profit = rev - base_cost
        margin = profit / rev if rev else 0
        results[name] = {"revenue": rev, "profit": profit, "margin": round(margin, 3)}
    return results

if __name__ == "__main__":
    rates = {"Optimistic": 0.20, "Base": 0.10, "Pessimistic": -0.05}
    print(scenario_model(1_000_000, 700_000, rates))
