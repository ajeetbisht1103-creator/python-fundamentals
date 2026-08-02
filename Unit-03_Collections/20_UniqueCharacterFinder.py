# ----------------------------------------------------
# Description:
# This program finds all unique
# characters present in a string.
# ----------------------------------------------------

text = input("Enter a string: ")

unique_characters = set(text)

print("Unique Characters:")

for character in sorted(unique_characters):
    if character != " ":
        print(character)