# ----------------------------------------------------
# Topic: String Methods
#
# Description:
# This program checks whether a string
# contains double spaces.
#
# Question:
# Write a Python program to detect
# double spaces in a string.
# ----------------------------------------------------

text = input("Enter a sentence: ")

if "  " in text:
    print("Double spaces found.")
else:
    print("No double spaces found.")