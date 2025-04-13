"""Regular, um, Expressions"""

import re


def main():
    """Main code"""
    print(count(input("Text: ")))


def count(s):
    """Counts of appearing 'um' in str"""
    pattern = r"\bum\b"
    return len(re.findall(pattern, s, flags=re.IGNORECASE))


if __name__ == "__main__":
    main()
