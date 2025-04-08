"""Reformat input with RegExp"""

import re

name = input("What's your name? ").strip()
# () - uses to capture that group(s)
if matches := re.search(r"^(.+), *(.+)$", name):        # := assign before if (walrus operator)
    name = matches.group(2) + " " + matches.group(1)    # group # starts with '1'

print(f"hello, {name}")
