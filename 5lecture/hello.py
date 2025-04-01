"""hello test"""


def main():
    """Main code"""
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    """print hello, by default to world"""
    return f"hello, {to}"


if __name__ == "__main__":
    main()
