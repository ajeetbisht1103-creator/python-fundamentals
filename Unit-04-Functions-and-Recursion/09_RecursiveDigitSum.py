# ----------------------------------------------------
# Description:
# This program calculates the sum of all digits
# of a number using recursion.
#
# Example:
# 12345 -> 1 + 2 + 3 + 4 + 5 = 15
# ----------------------------------------------------

def digit_sum(number):
    if number == 0:
        return 0

    return number % 10 + digit_sum(number // 10)


number = int(input("Enter a positive integer: "))

if number < 0:
    number = abs(number)

print("Sum of Digits:", digit_sum(number))