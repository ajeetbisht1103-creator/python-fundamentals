# ----------------------------------------------------
# Description:
# This program converts a sentence into
# a URL-friendly slug.
#
# Example:
# Python Programming Basics
# python-programming-basics
# ----------------------------------------------------

title = input("Enter a title: ")

slug = "-".join(title.lower().split())

print("URL Slug:")
print(slug)