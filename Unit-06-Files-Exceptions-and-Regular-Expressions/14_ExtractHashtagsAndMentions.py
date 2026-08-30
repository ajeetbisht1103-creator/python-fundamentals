# ----------------------------------------------------
# Description:
# This program uses regular expressions to extract
# hashtags and user mentions from a social media post.
# ----------------------------------------------------

import re

text = input("Enter a social media post: ")

hashtags = re.findall(r"#[A-Za-z0-9_]+", text)
mentions = re.findall(r"@[A-Za-z0-9_]+", text)

print("\n----- Extracted Data -----")

if hashtags:
    print("Hashtags:")
    for tag in hashtags:
        print(tag)
else:
    print("No hashtags found.")

if mentions:
    print("\nMentions:")
    for mention in mentions:
        print(mention)
else:
    print("No mentions found.")

print("\nTotal Hashtags:", len(hashtags))
print("Total Mentions:", len(mentions))