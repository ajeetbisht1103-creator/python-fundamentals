# ----------------------------------------------------
# Description:
# This program finds the most frequently
# occurring character in a string.
# ----------------------------------------------------

text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch != " ":
        frequency[ch] = frequency.get(ch, 0) + 1

most_frequent = max(frequency, key=frequency.get)

print(f"Most Frequent Character: {most_frequent}")
print(f"Occurrences: {frequency[most_frequent]}")