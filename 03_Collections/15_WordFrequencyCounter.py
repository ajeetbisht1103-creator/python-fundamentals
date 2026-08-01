# ----------------------------------------------------
# Description:
# This program counts the frequency
# of every word in a sentence using
# a dictionary.
# ----------------------------------------------------

sentence = input("Enter a sentence: ").lower()

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")

for word, count in frequency.items():
    print(f"{word} : {count}")