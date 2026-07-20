# ----------------------------------------------------
# Description:
# This program converts temperature from Celsius
# to Fahrenheit.
#
# Formula:
# Fahrenheit = (Celsius × 9/5) + 32
# ----------------------------------------------------

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")