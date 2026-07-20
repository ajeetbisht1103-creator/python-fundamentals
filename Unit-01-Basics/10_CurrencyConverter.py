# ----------------------------------------------------
# Description:
# This program converts Indian Rupees (INR)
# to US Dollars (USD) using a fixed
# exchange rate.
# ----------------------------------------------------

EXCHANGE_RATE = 87.0

inr = float(input("Enter amount in INR: "))

usd = inr / EXCHANGE_RATE

print(f"Equivalent USD: ${usd:.2f}")