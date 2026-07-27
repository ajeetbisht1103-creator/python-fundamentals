# ----------------------------------------------------
# Description:
# This program removes all punctuation
# characters from a sentence.
# ----------------------------------------------------

import string

sentence = input("Enter a sentence: ")

cleaned = ""

for ch in sentence:
    if ch not in string.punctuation:
        cleaned += ch

print("Sentence without punctuation:")
print(cleaned)