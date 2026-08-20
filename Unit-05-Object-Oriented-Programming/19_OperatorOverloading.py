# ----------------------------------------------------
# Description:
# This program demonstrates operator overloading by
# defining how two objects of a custom class can be
# added using the + operator.
# ----------------------------------------------------

class Distance:

    def __init__(self, meters):
        self.meters = meters

    def __add__(self, other):
        return Distance(self.meters + other.meters)

    def display(self):
        print(f"Distance: {self.meters} meters")


first = float(input("Enter first distance in meters: "))
second = float(input("Enter second distance in meters: "))

distance1 = Distance(first)
distance2 = Distance(second)

total = distance1 + distance2

print("\nCombined Distance")
total.display()