# ----------------------------------------------------
# Description:
# This program demonstrates object-oriented
# programming by calculating the area and perimeter
# of a rectangle using a class.
# ----------------------------------------------------

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("\nRectangle Details")
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


length = float(input("Enter length: "))
width = float(input("Enter width: "))

rectangle = Rectangle(length, width)

rectangle.display()