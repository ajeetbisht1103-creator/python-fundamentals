# ----------------------------------------------------
# Description:
# This program reads a text file and calculates
# the number of lines, words and characters in it.
# ----------------------------------------------------

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("\n----- File Statistics -----")
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", characters)

except FileNotFoundError:
    print("File not found.")