# ----------------------------------------------------
# Description:
# This program uses regular expressions to identify
# HTML tags from a given HTML-like text.
# ----------------------------------------------------

import re

html = input("Enter HTML text: ")

pattern = r"<\/?[A-Za-z][A-Za-z0-9]*(?:\s+[^<>]*)?>"

tags = re.findall(pattern, html)

if tags:
    print("\n----- HTML Tags Found -----")

    for tag in tags:
        print(tag)

    print("\nTotal Tags:", len(tags))
else:
    print("No HTML tags found.")