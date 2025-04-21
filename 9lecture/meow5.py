"""Lecture 9.8 - Etc: docstrings"""

# https://peps.python.org/pep-0257/


def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to mew
    :type n: int
    :return: A string of n meows, one per line
    :rtype: str
    :raise TypeError: If n is not an int
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
