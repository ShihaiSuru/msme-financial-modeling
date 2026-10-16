#!/usr/bin/env python3
"""NPV and IRR calculations."""
from numpy_financial import npv, irr

def project_npv(cashflows, discount_rate=0.12):
    return npv(discount_rate, cashflows)

def project_irr(cashflows):
    return irr(cashflows)

if __name__ == "__main__":
    # Capex + 4 years of free cash flow
    cfs = [-500000, 120000, 150000, 180000, 200000]
    print(f"NPV: ₹{project_npv(cfs):,.0f}")
    print(f"IRR: {project_irr(cfs)*100:.1f}%")
