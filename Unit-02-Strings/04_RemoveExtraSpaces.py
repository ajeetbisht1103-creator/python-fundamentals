# ----------------------------------------------------
# Description:
# This program removes all extra spaces
# from a sentence while preserving a
# single space between words.
# ----------------------------------------------------

sentence = input("Enter a sentence: ")

cleaned_sentence = " ".join(sentence.split())

print("\nOriginal Sentence:")
print(sentence)

print("\nCleaned Sentence:")
print(cleaned_sentence)