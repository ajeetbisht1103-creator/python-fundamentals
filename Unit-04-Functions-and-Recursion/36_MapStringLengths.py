# ----------------------------------------------------
# Description:
# This program uses map() to calculate the length
# of every word in a list.
# ----------------------------------------------------

words = input("Enter words separated by spaces: ").split()

lengths = list(map(len, words))

print("Words:", words)
print("Lengths:", lengths)