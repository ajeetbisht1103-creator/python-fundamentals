# ----------------------------------------------------
# Description:
# This program counts the occurrences of a specified
# character in a string using recursion.
# ----------------------------------------------------

def count_character(text, character, index):
    if index == len(text):
        return 0

    count = 1 if text[index] == character else 0

    return count + count_character(text, character, index + 1)


text = input("Enter a string: ")
character = input("Enter character to count: ")

if len(character) != 1:
    print("Please enter exactly one character.")
else:
    count = count_character(text, character, 0)
    print(f"'{character}' occurs {count} time(s).")