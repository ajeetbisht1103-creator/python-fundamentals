# ----------------------------------------------------
# Description:
# This program calculates Compound Interest
# using the standard compound interest formula.
# ----------------------------------------------------

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (years): "))

amount = principal * ((1 + rate / 100) ** time)
compound_interest = amount - principal

print(f"Compound Interest: {compound_interest:.2f}")
print(f"Total Amount: {amount:.2f}")