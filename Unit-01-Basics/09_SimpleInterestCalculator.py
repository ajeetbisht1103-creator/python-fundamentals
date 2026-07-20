# ----------------------------------------------------
# Description:
# This program calculates Simple Interest.
#
# Formula:
# SI = (P × R × T) / 100
# ----------------------------------------------------

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (years): "))

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest: {simple_interest:.2f}")