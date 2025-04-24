"""Short 9 - recursion"""


def factorial(n):
    """Returns a factorial of n"""
    return 1 if n == 1 else n * factorial(n - 1)


result = factorial(3)

print(result)
