# ----------------------------------------------------
# Description:
# This program generates the initials
# of a person's full name.
#
# Example:
# Virat Kohli
# VK
# ----------------------------------------------------

name = input("Enter your full name: ")

words = name.split()

initials = ""

for word in words:
    initials += word[0].upper()

print("Initials:", initials)