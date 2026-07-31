# ----------------------------------------------------
# Description:
# This program searches for an element
# in a list using the Linear Search algorithm.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the element to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Element found at index {i}.")
        found = True
        break

if not found:
    print("Element not found.")