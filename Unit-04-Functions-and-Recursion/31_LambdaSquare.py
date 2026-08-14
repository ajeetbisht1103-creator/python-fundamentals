# ----------------------------------------------------
# Description:
# This program demonstrates the use of a lambda
# function to calculate the square of a number.
# ----------------------------------------------------

number = float(input("Enter a number: "))

square = lambda x: x ** 2

print("Square:", square(number))