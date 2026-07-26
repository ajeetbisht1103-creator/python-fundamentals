# ----------------------------------------------------
# Description:
# This program checks whether a password
# is Strong, Medium, or Weak based on
# its length and character composition.
# ----------------------------------------------------

password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_characters:
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong Password")
elif len(password) >= 6 and has_lower and has_digit:
    print("Medium Password")
else:
    print("Weak Password")