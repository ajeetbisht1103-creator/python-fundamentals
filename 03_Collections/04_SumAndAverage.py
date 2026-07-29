# ----------------------------------------------------
# Description:
# This program calculates the sum
# and average of all elements in a list.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)