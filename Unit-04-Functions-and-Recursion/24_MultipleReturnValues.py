# ----------------------------------------------------
# Description:
# This program demonstrates how a function can
# return multiple values such as sum, average,
# maximum and minimum.
# ----------------------------------------------------

def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

total, average, maximum, minimum = analyze_numbers(numbers)

print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)