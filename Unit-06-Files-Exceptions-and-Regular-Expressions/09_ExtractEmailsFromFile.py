# ----------------------------------------------------
# Description:
# This program reads a text file and uses regular
# expressions to find and extract valid email addresses.
# ----------------------------------------------------

import re

filename = input("Enter file name: ")

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

try:
    with open(filename, "r") as file:
        content = file.read()

    emails = re.findall(email_pattern, content)

    if emails:
        print("\n----- Email Addresses Found -----")

        for email in emails:
            print(email)

        print(f"\nTotal Emails: {len(emails)}")
    else:
        print("No valid email addresses found.")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Email extraction completed.")