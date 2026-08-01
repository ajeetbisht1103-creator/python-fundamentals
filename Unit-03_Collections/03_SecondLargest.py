# ----------------------------------------------------
# Description:
# This program finds the second largest
# unique element in a list.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second Largest Element:", unique_numbers[-2])
else:
    print("Second largest element does not exist.") 