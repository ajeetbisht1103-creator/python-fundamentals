# ----------------------------------------------------
# Description:
# This program calculates the sum of all elements
# in a list using recursion.
# ----------------------------------------------------

def list_sum(numbers, index):
    if index == len(numbers):
        return 0

    return numbers[index] + list_sum(numbers, index + 1)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if numbers:
    print("Sum of Elements:", list_sum(numbers, 0))
else:
    print("List cannot be empty.")