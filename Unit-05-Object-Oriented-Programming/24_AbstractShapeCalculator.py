# ----------------------------------------------------
# Description:
# This program demonstrates abstraction by defining
# an abstract Shape class and implementing the area
# method differently for different shapes.
# ----------------------------------------------------

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


print("1. Rectangle")
print("2. Circle")
print("3. Triangle")

choice = int(input("Enter choice: "))

if choice == 1:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    shape = Rectangle(length, width)

elif choice == 2:
    radius = float(input("Enter radius: "))
    shape = Circle(radius)

elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    shape = Triangle(base, height)

else:
    shape = None
    print("Invalid choice.")

if shape:
    print(f"Area: {shape.area():.2f}")