# ----------------------------------------------------
# Description:
# This program separates even and odd
# numbers into two different lists.
# ----------------------------------------------------

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even Numbers:")
print(even_numbers)

print("Odd Numbers:")
print(odd_numbers)