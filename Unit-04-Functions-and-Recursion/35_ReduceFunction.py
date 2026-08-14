# ----------------------------------------------------
# Description:
# This program uses the reduce() function to
# calculate the product of all elements in a list.
# ----------------------------------------------------

from functools import reduce

numbers = list(map(int, input("Enter numbers: ").split()))

product = reduce(lambda x, y: x * y, numbers)

print("Numbers:", numbers)
print("Product:", product)