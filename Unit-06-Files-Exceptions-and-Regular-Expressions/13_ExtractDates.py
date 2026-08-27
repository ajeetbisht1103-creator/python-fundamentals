# ----------------------------------------------------
# Description:
# This program uses regular expressions to find dates
# in DD-MM-YYYY format from a given text.
# ----------------------------------------------------

import re

text = input("Enter text containing dates: ")

pattern = r"\b(?:0[1-9]|[12]\d|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b"

dates = re.findall(pattern, text)

if dates:
    print("\n----- Dates Found -----")

    for date in dates:
        print(date)

    print(f"\nTotal Dates: {len(dates)}")
else:
    print("No dates found.")