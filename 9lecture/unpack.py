"""Lecture 9.9 - Etc: unpacking"""

# exmpl 1:
# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")


def total(galleons, sickles, knuts):
    """Convert currency into Knuts"""
    return (galleons * 17 + sickles) * 29 + knuts


# 1 - source code
print(total(100, 50, 25), "Knuts")

# store coins in the list
coins = [100, 50, 25]

# 2 - try simple
print(total(coins[0], coins[1], coins[2]), "Knuts")

# 3 - try smarter - UNPACK values
print(total(*coins), "Knuts")
