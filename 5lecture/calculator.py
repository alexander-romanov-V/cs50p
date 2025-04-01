"""Simple calculater"""


def main():
    """Main code"""
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    """Returns n^2"""
    return n + n


if __name__ == "__main__":
    main()
