# ----------------------------------------------------
# Description:
# This program finds the first occurrence of an element
# in a sorted list using recursive binary search.
# ----------------------------------------------------

def first_occurrence(numbers, target, low, high):
    if low > high:
        return -1

    middle = (low + high) // 2

    if numbers[middle] == target:
        left_result = first_occurrence(
            numbers, target, low, middle - 1
        )

        if left_result != -1:
            return left_result

        return middle

    if target < numbers[middle]:
        return first_occurrence(
            numbers, target, low, middle - 1
        )

    return first_occurrence(
        numbers, target, middle + 1, high
    )


numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter element to search: "))

index = first_occurrence(
    numbers, target, 0, len(numbers) - 1
)

if index == -1:
    print("Element not found.")
else:
    print(f"First occurrence found at index {index}.")