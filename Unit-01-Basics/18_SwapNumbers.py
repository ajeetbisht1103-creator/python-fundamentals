# ----------------------------------------------------
# Description:
# This program swaps two numbers without
# using a third variable.
# ----------------------------------------------------

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"\nBefore Swapping: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After Swapping: a = {a}, b = {b}")