# ----------------------------------------------------
# Description:
# This program uses the filter() function to
# extract all even numbers from a list.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original List:", numbers)
print("Even Numbers:", even_numbers)