# ----------------------------------------------------
# Description:
# This program calculates the product of all elements
# in a list using recursion.
# ----------------------------------------------------

def list_product(numbers, index):
    if index == len(numbers):
        return 1

    return numbers[index] * list_product(numbers, index + 1)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if numbers:
    print("Product of Elements:", list_product(numbers, 0))
else:
    print("List cannot be empty.")