# ----------------------------------------------------
# Description:
# This program calculates the electricity bill
# based on the number of units consumed.
#
# Rate:
# ₹7.50 per unit
# ----------------------------------------------------

RATE_PER_UNIT = 7.5

units = float(input("Enter electricity units consumed: "))

bill = units * RATE_PER_UNIT

print(f"Electricity Bill: ₹{bill:.2f}")