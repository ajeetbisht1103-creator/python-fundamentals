# ----------------------------------------------------
# Description:
# This program counts the number of
# characters in a given string,
# excluding spaces.
# ----------------------------------------------------

text = input("Enter a string: ")

character_count = len(text.replace(" ", ""))

print(f"Number of characters (excluding spaces): {character_count}")