"""Lecture 9.7 - Etc: set func return value type and checking them with mypy"""

# pip install mypy


# 'var: int' type hint (annotation for python of var type)
# '-> str' type hint (annotation for python of return value type)
def meow(n: int) -> str:
    """Print meow"""
    return "meow\n" * n


number: int = int(input("Number: "))
# 'mypy meow4.py' - shows this type error (if meow() returns not a str)
meows: str = meow(number)
print(meows, end="")
