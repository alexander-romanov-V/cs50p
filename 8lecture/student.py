"""OOP Example"""


def main():
    """Main code"""
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    """Ask a name"""
    return input("Name: ")


def get_house():
    """Ask a house"""
    return input("House: ")


if __name__ == "__main__":
    main()
