"""Lecture 9.12 - Etc: args and unpacking"""


def main():
    """Main code"""
    yell("This", "is", "CS50")


def yell(*words):
    """YELL a phrase"""
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)  # unpack the list


if __name__ == "__main__":
    main()
