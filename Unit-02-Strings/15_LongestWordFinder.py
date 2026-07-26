# ----------------------------------------------------
# Description:
# This program finds the longest word
# in a given sentence.
# ----------------------------------------------------

sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = max(words, key=len)

print(f"Longest Word: {longest_word}")
print(f"Length: {len(longest_word)}")