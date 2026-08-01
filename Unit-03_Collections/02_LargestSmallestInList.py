# ----------------------------------------------------
# Description:
# This program finds the largest and
# smallest element in a list entered
# by the user.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = max(numbers)
smallest = min(numbers)

print("Largest Element:", largest)
print("Smallest Element:", smallest)