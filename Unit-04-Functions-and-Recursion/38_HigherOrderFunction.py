# ----------------------------------------------------
# Description:
# This program demonstrates a higher-order function
# that accepts another function as an argument.
# ----------------------------------------------------

def calculate(a, b, operation):
    return operation(a, b)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

print("Sum:", calculate(first, second, add))
print("Product:", calculate(first, second, multiply))