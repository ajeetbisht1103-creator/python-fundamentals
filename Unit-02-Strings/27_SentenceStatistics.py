# ----------------------------------------------------
# Description:
# This program displays useful statistics
# about a sentence.
# ----------------------------------------------------

sentence = input("Enter a sentence: ")

characters = len(sentence)
words = len(sentence.split())
spaces = sentence.count(" ")

print(f"Characters : {characters}")
print(f"Words      : {words}")
print(f"Spaces     : {spaces}")