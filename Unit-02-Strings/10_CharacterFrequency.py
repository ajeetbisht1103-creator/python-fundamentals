# ----------------------------------------------------
# Description:
# This program counts the frequency of
# each character in a string.
# ----------------------------------------------------

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch != " ":
        frequency[ch] = frequency.get(ch, 0) + 1

print("\nCharacter Frequencies:")

for key, value in frequency.items():
    print(f"{key} : {value}")