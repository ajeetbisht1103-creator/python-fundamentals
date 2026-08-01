# ----------------------------------------------------
# Description:
# This program reverses a list without
# using the reverse() method.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed List:")
print(reversed_list)