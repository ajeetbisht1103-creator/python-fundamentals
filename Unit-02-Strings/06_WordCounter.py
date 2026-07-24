# ----------------------------------------------------
# Description:
# This program counts the total number
# of words present in a sentence.
# ----------------------------------------------------

sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"Total Words: {len(words)}")