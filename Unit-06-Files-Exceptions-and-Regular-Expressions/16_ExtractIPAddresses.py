# ----------------------------------------------------
# Description:
# This program uses regular expressions to extract valid
# IPv4 addresses from a log or input string.
# ----------------------------------------------------
import re

text = input("Enter text containing IP addresses: ")
pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

ip_addresses = re.findall(pattern, text)

print("\n----- Extracted Data -----")
if ip_addresses:
    print("Found IPv4 Addresses:")
    for ip in ip_addresses:
        print(ip)
else:
    print("No IP addresses found.")

print("\nTotal IP Addresses:", len(ip_addresses))