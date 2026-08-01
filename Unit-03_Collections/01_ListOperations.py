# ----------------------------------------------------
# Description:
# This program demonstrates basic list
# operations such as append, insert,
# remove, pop and display.
# ----------------------------------------------------

numbers = [10, 20, 30, 40]

print("Original List:", numbers)

numbers.append(50)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.remove(20)
print("After remove:", numbers)

removed_element = numbers.pop()

print("Popped Element:", removed_element)
print("Final List:", numbers)