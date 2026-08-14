# ----------------------------------------------------
# Description:
# This program uses the map() function to
# calculate the square of every number in a list.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers: ").split()))

squares = list(map(lambda x: x ** 2, numbers))

print("Original List:", numbers)
print("Squared List:", squares)