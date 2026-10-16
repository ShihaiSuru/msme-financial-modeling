#!/usr/bin/env python3
"""Sensitivity analysis on key drivers."""
import numpy as np

def sensitivity(base_value, drivers):
    """drivers = dict of name -> percentage change"""
    results = {}
    for name, change in drivers.items():
        results[name] = base_value * (1 + change)
    return results

if __name__ == "__main__":
    print(sensitivity(200000, {"Revenue +10%": 0.10, "Cost +5%": -0.05, "Price -3%": -0.03}))
