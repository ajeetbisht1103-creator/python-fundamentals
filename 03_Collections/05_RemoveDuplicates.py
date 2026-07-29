# ----------------------------------------------------
# Description:
# This program removes duplicate
# elements from a list while
# preserving their original order.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("List after removing duplicates:")
print(unique_numbers)