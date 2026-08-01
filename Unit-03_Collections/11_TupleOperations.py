# ----------------------------------------------------
# Description:
# This program demonstrates basic tuple
# operations such as indexing, slicing,
# length and membership testing.
# ----------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Slice (1:4):", numbers[1:4])
print("Length:", len(numbers))

value = int(input("Enter a number to search: "))

if value in numbers:
    print("Element found in tuple.")
else:
    print("Element not found.")