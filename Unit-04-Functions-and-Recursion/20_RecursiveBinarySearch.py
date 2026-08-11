# ----------------------------------------------------
# Description:
# This program searches for an element in a sorted
# list using the recursive Binary Search algorithm.
# ----------------------------------------------------

def binary_search(numbers, target, low, high):
    if low > high:
        return -1

    middle = (low + high) // 2

    if numbers[middle] == target:
        return middle

    if target < numbers[middle]:
        return binary_search(numbers, target, low, middle - 1)

    return binary_search(numbers, target, middle + 1, high)


numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter element to search: "))

index = binary_search(numbers, target, 0, len(numbers) - 1)

if index == -1:
    print("Element not found.")
else:
    print(f"Element found at index {index}.")