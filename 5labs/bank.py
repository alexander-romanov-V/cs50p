"""Back to the Bank"""


def main():
    """Main code"""
    greeting = input("Greetings: ")
    val = value(greeting)
    print(f"${val}")


def value(greeting):
    """Returns value of greeting"""
    if isinstance(greeting, str):
        grtng = greeting.strip().lower()
        if grtng.startswith("hello"):
            return 0
        if grtng.startswith("h"):
            return 20
    return 100


if __name__ == "__main__":
    main()
