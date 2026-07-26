# ----------------------------------------------------
# Description:
# This program encrypts a message using
# the Caesar Cipher technique with a
# user-defined shift value.
# ----------------------------------------------------

message = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in message:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        encrypted += chr((ord(ch) - base + shift) % 26 + base)
    else:
        encrypted += ch

print("Encrypted Message:")
print(encrypted)