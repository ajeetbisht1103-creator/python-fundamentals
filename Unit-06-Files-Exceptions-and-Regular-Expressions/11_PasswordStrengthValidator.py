# ----------------------------------------------------
# Description:
# This program validates password strength using
# regular expressions.
#
# Requirements:
# - At least 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit
# - At least one special character
# ----------------------------------------------------

import re

password = input("Enter password: ")

has_upper = re.search(r"[A-Z]", password)
has_lower = re.search(r"[a-z]", password)
has_digit = re.search(r"\d", password)
has_special = re.search(r"[^A-Za-z0-9]", password)
has_length = len(password) >= 8

if all([has_upper, has_lower, has_digit, has_special, has_length]):
    print("Strong password.")
else:
    print("Weak password.")

    if not has_length:
        print("- Must contain at least 8 characters.")

    if not has_upper:
        print("- Must contain an uppercase letter.")

    if not has_lower:
        print("- Must contain a lowercase letter.")

    if not has_digit:
        print("- Must contain a digit.")

    if not has_special:
        print("- Must contain a special character.")