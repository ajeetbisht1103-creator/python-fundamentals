# ----------------------------------------------------
# Description:
# This program rotates a list to the
# right by a specified number of positions.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
k = int(input("Enter number of rotations: "))

k = k % len(numbers)

rotated_list = numbers[-k:] + numbers[:-k]

print("Rotated List:")
print(rotated_list)