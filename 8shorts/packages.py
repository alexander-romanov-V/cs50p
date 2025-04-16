"""shorts 8 - Packages class"""


class Package:
    """Represent a package class"""

    # Thunder init ?
    def __init__(self, number, sender, recipient, weight) -> None:
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight


def main():
    """Main code"""
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5),
    ]


if __name__ == "__mani__":
    main()
