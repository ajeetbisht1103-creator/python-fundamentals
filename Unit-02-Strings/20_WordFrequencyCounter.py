# ----------------------------------------------------
# Description:
# This program counts the frequency
# of every word in a sentence.
# ----------------------------------------------------

sentence = input("Enter a sentence: ").lower()

words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequencies:")

for word, count in frequency.items():
    print(f"{word} : {count}")