# ----------------------------------------------------
# Description:
# This program demonstrates variable-length
# positional arguments using *args.
# ----------------------------------------------------

def calculate_total(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = list(map(float, input("Enter numbers: ").split()))

total = calculate_total(*numbers)

print(f"Total: {total}")