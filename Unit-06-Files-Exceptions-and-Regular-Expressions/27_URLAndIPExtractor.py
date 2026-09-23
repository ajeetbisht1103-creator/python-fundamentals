# ----------------------------------------------------
# Description:
# This program searches an input text file for valid IPv4
# addresses and HTTP/HTTPS URLs using Regular Expressions
# and reports all distinct matches found.
# ----------------------------------------------------

import re

input_file = "web_traffic.txt"

# Regex for IPv4 and standard URLs
ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
url_pattern = r"https?://[A-Za-z0-9.-]+(?:\:[0-9]+)?(?:/[^\s]*)?"

try:
    with open(input_file, "r") as file:
        content = file.read()

    ip_addresses = sorted(list(set(re.findall(ip_pattern, content))))
    urls = sorted(list(set(re.findall(url_pattern, content))))

    print("----- IP Addresses Found -----")
    for ip in ip_addresses:
        print(f" - {ip}")

    print("\n----- URLs Found -----")
    for url in urls:
        print(f" - {url}")

    print(f"\nTotal unique IPs: {len(ip_addresses)}")
    print(f"Total unique URLs: {len(urls)}")

except FileNotFoundError:
    print(f"Error: '{input_file}' file not found.")