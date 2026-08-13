# ----------------------------------------------------
# Description:
# This program counts the number of even elements
# in a list using recursion.
# ----------------------------------------------------

def count_even(numbers, index):
    if index == len(numbers):
        return 0

    count = 1 if numbers[index] % 2 == 0 else 0

    return count + count_even(numbers, index + 1)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Number of Even Elements:", count_even(numbers, 0))