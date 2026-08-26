# ----------------------------------------------------
# Description:
# This program validates Indian mobile phone numbers
# using a regular expression.
# ----------------------------------------------------

import re

phone = input("Enter phone number: ")

pattern = r"^[6-9]\d{9}$"

if re.fullmatch(pattern, phone):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")