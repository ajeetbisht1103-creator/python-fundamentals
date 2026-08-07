# ----------------------------------------------------
# Description:
# This program calculates the factorial of
# a number using a recursive function.
# ----------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {number}: {factorial(number)}")