# ----------------------------------------------------
# Description:
# This program validates a username using regular
# expressions.
#
# Requirements:
# - 5 to 15 characters
# - Must start with a letter
# - Can contain letters, digits and underscores
# - No spaces or special characters
# ----------------------------------------------------

import re

username = input("Enter username: ")

pattern = r"^[A-Za-z][A-Za-z0-9_]{4,14}$"

if re.fullmatch(pattern, username):
    print("Valid username.")
else:
    print("Invalid username.")
    print("Username must:")
    print("- Contain 5 to 15 characters.")
    print("- Start with a letter.")
    print("- Contain only letters, digits and underscores.")
    print("- Not contain spaces or special characters.")