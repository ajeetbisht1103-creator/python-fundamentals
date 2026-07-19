# ----------------------------------------------------
# Topic: Strings
#
# Description:
# This program replaces placeholders in a
# letter template with the user's name and date.
#
# Question:
# Write a Python program to fill in a
# letter template using name and date.
# ----------------------------------------------------

name = input("Enter your name: ")
date = input("Enter today's date: ")

letter = f"""
Dear {name},

You are selected!

Date: {date}
"""

print(letter)