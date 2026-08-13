# ----------------------------------------------------
# Description:
# This program reverses the digits of an integer
# using recursion.
# ----------------------------------------------------

def reverse_number(number, reversed_number=0):
    if number == 0:
        return reversed_number

    digit = number % 10
    reversed_number = reversed_number * 10 + digit

    return reverse_number(number // 10, reversed_number)


number = int(input("Enter a positive integer: "))

if number < 0:
    print("Please enter a positive integer.")
else:
    print("Reversed Number:", reverse_number(number))