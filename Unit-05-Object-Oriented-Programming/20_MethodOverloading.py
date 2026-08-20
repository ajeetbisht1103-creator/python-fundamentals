# ----------------------------------------------------
# Description:
# This program demonstrates method overloading
# behavior in Python using default arguments.
# The same method can calculate the area of a
# square or rectangle depending on the arguments.
# ----------------------------------------------------

class Shape:

    def area(self, length, width=None):
        if width is None:
            return length * length

        return length * width


shape = Shape()

print("1. Calculate area of square")
print("2. Calculate area of rectangle")

choice = int(input("Enter choice: "))

if choice == 1:
    side = float(input("Enter side: "))
    print("Area of Square:", shape.area(side))

elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of Rectangle:", shape.area(length, width))

else:
    print("Invalid choice.")