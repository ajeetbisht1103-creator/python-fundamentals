# ----------------------------------------------------
# Description:
# This program uses regular expressions to find and
# extract valid HTTP and HTTPS URLs from a text.
# ----------------------------------------------------

import re

text = input("Enter text containing URLs: ")

pattern = r"https?://(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?"

urls = re.findall(pattern, text)

if urls:
    print("\n----- URLs Found -----")

    for url in urls:
        print(url)

    print(f"\nTotal URLs: {len(urls)}")
else:
    print("No URLs found.")