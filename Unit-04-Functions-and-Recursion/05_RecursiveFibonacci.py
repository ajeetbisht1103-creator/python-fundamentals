# ----------------------------------------------------
# Description:
# This program generates the Fibonacci sequence
# using a recursive function.
# ----------------------------------------------------

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter number of terms: "))

if terms <= 0:
    print("Enter a positive number.")
else:
    print("Fibonacci Sequence:")

    for i in range(terms):
        print(fibonacci(i), end=" ")