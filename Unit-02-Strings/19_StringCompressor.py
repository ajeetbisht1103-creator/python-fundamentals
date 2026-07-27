# ----------------------------------------------------
# Description:
# This program compresses a string by
# replacing consecutive repeated characters
# with the character followed by its count.
#
# Example:
# aaabbcccc -> a3b2c4
# ----------------------------------------------------

text = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

print("Compressed String:")
print(compressed)