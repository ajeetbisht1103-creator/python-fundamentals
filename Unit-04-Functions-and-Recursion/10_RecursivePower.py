# ----------------------------------------------------
# Description:
# This program calculates the power of a number
# using recursion without using the ** operator.
# ----------------------------------------------------

def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


base = float(input("Enter base: "))
exponent = int(input("Enter non-negative exponent: "))

if exponent < 0:
    print("Exponent must be non-negative.")
else:
    print(f"Result: {power(base, exponent)}")