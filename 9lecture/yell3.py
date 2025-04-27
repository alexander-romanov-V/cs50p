"""Lecture 9.14 - Etc: list comprehension"""


def main():
    """Main code"""
    yell("This", "is", "CS50")


def yell(*words):
    """YELL a phrase"""

    # uppercased = map(str.upper, words)
    # alternative (pythonuc) way apply upper for each elements in list
    uppercased = [word.upper() for word in words]
    print(*uppercased)  # unpack the list


if __name__ == "__main__":
    main()
