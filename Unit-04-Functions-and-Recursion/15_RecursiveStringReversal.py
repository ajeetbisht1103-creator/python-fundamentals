# ----------------------------------------------------
# Description:
# This program reverses a string using
# a recursive function without using
# slicing or the reverse() method.
# ----------------------------------------------------

def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


text = input("Enter a string: ")

print("Reversed String:", reverse_string(text))