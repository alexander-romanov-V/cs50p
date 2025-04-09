"""Clean username from input with RegExp"""

import re

url = input("URL: ").strip()

# username = re.sub(r"^.*(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

# use uncapturing group (?:...)
# if matches := re.search(r"^.*(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url,
#                         flags=re.IGNORECASE):

if matches := re.search(r"^.*(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url,
                        flags=re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
