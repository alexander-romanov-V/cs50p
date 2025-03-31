"""I'm thinking of a number between 1 and 100..."""

from random import randint


def main():
    """Main code"""
    n = 0
    while n <= 0:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass

    guess = randint(1, n)
    n = 0
    while n != guess:
        try:
            n = int(input("Guess: "))
        except ValueError:
            continue
        if n <= 0:
            continue
        elif n < guess:
            print("Too small!")
        elif n > guess:
            print("Too large!")

    print("Just right!")


if __name__ == "__main__":
    main()
