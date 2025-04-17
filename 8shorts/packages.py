"""shorts 8 - Packages class:
incapsulate info into a class,
use instance variables and instance methods"""


class Package:
    """Represent a package class"""

    # dunder init
    def __init__(self, number, sender, recipient, weight) -> None:
        # instance variables
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    # dunder str
    # instance method
    def __str__(self) -> str:
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"

    # instance method
    def calculate_cost(self, cost_per_kg):
        """Get shipping cost according the weight and cost per kg"""
        return self.weight * cost_per_kg


def main():
    """Main code"""
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5),
    ]
    for package in packages:
        print(f"{package} cost ${package.calculate_cost(cost_per_kg=2)}")


if __name__ == "__main__":
    main()
