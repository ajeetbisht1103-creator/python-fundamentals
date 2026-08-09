# ----------------------------------------------------
# Description:
# This program calculates the Least Common Multiple
# of two numbers using a user-defined function.
# ----------------------------------------------------

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return abs(a)


def lcm(a, b):
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("LCM:", lcm(first, second))