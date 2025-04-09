"""Capture RegExp groups"""

import re


locations = {
    "+1": "United States and Canada",
    "+62": "Indonesia",
    "+505": "Nicaragua",
    }

def main():
    """Main code"""
    pattern = r"\+\d{1,3} \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    if match := re.search(pattern, number):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
