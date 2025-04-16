"""shorts 8 - Packages"""


class Package:
    """Represent a package class"""

    def __init__(self, number, sender, recipient, weight) -> None:
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight


def main():
    """Main code"""
    packages = ["Package1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]


if __name__ == "__mani__":
    main()
