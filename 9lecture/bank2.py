"""Lecture 9.2 - Etc: global variables vs class"""


class Account:
    """Bank account"""

    def __init__(self) -> None:
        self._balance = 0  # start with _ says this var is private

    @property
    def balance(self):
        """Get current balance"""
        return self._balance

    def deposit(self, n):
        """Put some mone in"""
        self._balance += n

    def withdraw(self, n):
        """Get some money out"""
        self._balance -= n


def main():
    """Main code"""
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
