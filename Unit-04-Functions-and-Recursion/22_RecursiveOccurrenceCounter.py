# ----------------------------------------------------
# Description:
# This program counts how many times a given element
# occurs in a list using recursion.
# ----------------------------------------------------

def count_occurrences(numbers, target, index):
    if index == len(numbers):
        return 0

    count = 1 if numbers[index] == target else 0

    return count + count_occurrences(numbers, target, index + 1)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter element to count: "))

count = count_occurrences(numbers, target, 0)

print(f"{target} occurs {count} time(s).")