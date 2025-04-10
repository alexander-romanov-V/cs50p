"""Exctract youtube links and returns its short version with RegEx"""

import re


def main():
    """Main code"""
    print(parse(input("HTML: ")))


def parse(s):
    """Exctract youtube links and returns its short version"""
    pattern = r"<iframe.*src=\"https?://(?:www\.)?youtube\.com/embed/([\d\w]*)\".*></iframe>"

    if match := re.search(pattern, s):
        return "https://youtu.be/" + match.group(1)
    return None


if __name__ == "__main__":
    main()
