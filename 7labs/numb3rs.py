"""Validate IPv4 address via RegExp"""

import re


def main():
    """Main code"""
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Return True if a valid IPv4 address is passed"""
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    if not (match := re.search(pattern, ip)):
        return False
    for i in range(1, 4):
        if not 0 <= int(match.group(i)) <= 255:
            return False
    return True


if __name__ == "__main__":
    main()
