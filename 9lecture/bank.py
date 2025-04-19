"""Lecture 9.2 - Etc: global variables"""

balance = 0


def main():
    """Main code"""
    print("Balance:", balance)
    deposit(1000)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    """Put some mone in"""
    global balance  # before change global var - needs to declare it as global
    balance += n


def withdraw(n):
    """Get some money out"""
    global balance
    balance -= n


if __name__ == "__main__":
    main()
