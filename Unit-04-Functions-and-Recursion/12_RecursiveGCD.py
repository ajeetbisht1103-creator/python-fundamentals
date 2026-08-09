# ----------------------------------------------------
# Description:
# This program calculates the Greatest Common
# Divisor (GCD) of two numbers using recursion.
# ----------------------------------------------------

def gcd(a, b):
    if b == 0:
        return abs(a)

    return gcd(b, a % b)


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("GCD:", gcd(first, second))