# ----------------------------------------------------
# Description:
# This program demonstrates polymorphism by using
# the same area() method with different shape classes.
# ----------------------------------------------------

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


rectangle = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(8, 6)

shapes = [rectangle, circle, triangle]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")