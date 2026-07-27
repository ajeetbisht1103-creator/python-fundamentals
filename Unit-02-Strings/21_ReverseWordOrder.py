# ----------------------------------------------------
# Description:
# This program reverses the order
# of words in a sentence.
#
# Example:
# I love Python
# Python love I
# ----------------------------------------------------

sentence = input("Enter a sentence: ")

words = sentence.split()

reversed_sentence = " ".join(words[::-1])

print("Reversed Sentence:")
print(reversed_sentence)