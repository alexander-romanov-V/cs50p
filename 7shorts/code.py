"""RegExp for Color Code #0055FF"""

import re


def main():
    """Main code"""
    code = input("Hexadecimal color code: ")

    # - Begins with #
    # - Composed of 6 characters: 0-9 and A-F
    pattern = r"^#[0-9a-fA-F]{6}$"
    
    if match := re.search(pattern, code):
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")


if __name__ == "__main__":
    main()
