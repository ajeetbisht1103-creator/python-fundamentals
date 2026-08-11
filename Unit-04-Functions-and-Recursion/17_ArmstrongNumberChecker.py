# ----------------------------------------------------
# Description:
# This program checks whether a number is an
# Armstrong number using a user-defined function.
# ----------------------------------------------------

def is_armstrong(number):
    original = number
    digits = len(str(number))
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** digits
        number //= 10

    return total == original


number = int(input("Enter a number: "))

if is_armstrong(number):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
