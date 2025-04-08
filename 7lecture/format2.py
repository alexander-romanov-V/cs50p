"""Reformat input with RegExp"""

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)     # () - uses to capture that group(s)
if matches:
    name = matches.group(2) + " " + matches.group(1)    # group # starts with '1'
    # last, first = matches.groups()
    # name = f"{first} {last}"

print(f"hello, {name}")
