"""Lecture 9.6 - Etc: set variables type and checking them with mypy"""

# pip install mypy


def meow(n: int):  # 'var: int' type hint (annotation for python of var type)
    """Print meow"""
    for _ in range(n):
        print("meow")


# number: int = input("Number: ") # 'mypy meow3.py' - shows this type error
# meow(number)    # 'mypy meow3.py' - shows this type error

number: int = int(input("Number: "))
meow(number)
