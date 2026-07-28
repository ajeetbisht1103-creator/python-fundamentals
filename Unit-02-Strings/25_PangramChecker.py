# ----------------------------------------------------
# Description:
# This program checks whether a sentence
# is a pangram (contains every letter
# of the English alphabet).
# ----------------------------------------------------

sentence = input("Enter a sentence: ").lower()

letters = set()

for ch in sentence:
    if ch.isalpha():
        letters.add(ch)

if len(letters) == 26:
    print("The sentence is a Pangram.")
else:
    print("The sentence is not a Pangram.")