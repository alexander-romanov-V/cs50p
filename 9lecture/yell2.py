"""Lecture 9.13 - Etc: map"""


def main():
    """Main code"""
    yell("This", "is", "CS50")


def yell(*words):
    """YELL a phrase"""

    # pass a func (str.upper) to apply it for each element (words)
    # map() returns a sequence (list in this case) of 'uppered' elements
    uppercased = map(str.upper, words)
    print(*uppercased) # unpack the list


if __name__ == "__main__":
    main()
