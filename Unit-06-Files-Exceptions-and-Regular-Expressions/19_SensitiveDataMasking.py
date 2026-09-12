# ----------------------------------------------------
# Description:
# This program uses regular expressions to detect
# email addresses and phone numbers in text and
# replaces them with masked values.
# ----------------------------------------------------

import re

text = input("Enter text containing sensitive information: ")

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
phone_pattern = r"\b[6-9]\d{9}\b"

masked_text = re.sub(email_pattern, "[EMAIL HIDDEN]", text)
masked_text = re.sub(phone_pattern, "[PHONE HIDDEN]", masked_text)

print("\n----- Masked Text -----")
print(masked_text)