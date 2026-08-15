# ----------------------------------------------------
# Description:
# This program demonstrates a nested function
# where one function is defined inside another.
# ----------------------------------------------------

def calculate_result(number):

    def square(value):
        return value * value

    def cube(value):
        return value * value * value

    return square(number), cube(number)


number = int(input("Enter a number: "))

square, cube = calculate_result(number)

print("Square:", square)
print("Cube:", cube)