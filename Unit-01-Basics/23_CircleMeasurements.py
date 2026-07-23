# ----------------------------------------------------
# Description:
# This program calculates the area and
# circumference of a circle.
# ----------------------------------------------------

import math

radius = float(input("Enter the radius: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
