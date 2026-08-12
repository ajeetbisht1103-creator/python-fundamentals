# ----------------------------------------------------
# Description:
# This program finds the smallest element in a list
# using recursion.
# ----------------------------------------------------

def find_min(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]

    minimum = find_min(numbers, index + 1)

    if numbers[index] < minimum:
        return numbers[index]

    return minimum


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if numbers:
    print("Smallest Element:", find_min(numbers, 0))
else:
    print("List cannot be empty.")