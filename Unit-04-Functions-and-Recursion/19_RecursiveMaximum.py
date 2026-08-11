# ----------------------------------------------------
# Description:
# This program finds the largest element in a list
# using recursion.
# ----------------------------------------------------

def find_max(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]

    maximum = find_max(numbers, index + 1)

    if numbers[index] > maximum:
        return numbers[index]

    return maximum


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if numbers:
    print("Largest Element:", find_max(numbers, 0))
else:
    print("List cannot be empty.")