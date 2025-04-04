"""Little Professor toy"""

from random import randint
import sys


def main():
    """Main code"""
    level = get_level()
    score = 0

    for _ in range(10):
        try:
            x = generate_integer(level)
            y = generate_integer(level)
        except ValueError:
            sys.exit()

        errors = 0
        while errors < 3:
            try:
                res = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            else:
                if res == x + y:
                    score += 1
                    break
            errors += 1
            print("EEE")
            if errors == 3:
                print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


def get_level():
    """Function get level from 1 to 3."""
    level = 0
    while not 1 <= level <= 3:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass

    return level


def generate_integer(level):
    """Function get number according level."""
    if not 1 <= level <= 3:
        raise ValueError
    if level == 1:
        return randint(0, 9)
    return randint(10 ** (level - 1), 10**level)


if __name__ == "__main__":
    main()
