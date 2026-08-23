# ----------------------------------------------------
# Description:
# This program reads a text file and counts how many
# times each word occurs in the file.
# ----------------------------------------------------

filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        text = file.read().lower()

    words = text.split()
    frequency = {}

    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        frequency[word] = frequency.get(word, 0) + 1

    print("\n----- Word Frequency -----")

    for word, count in sorted(frequency.items()):
        print(f"{word}: {count}")

except FileNotFoundError:
    print("File not found.")