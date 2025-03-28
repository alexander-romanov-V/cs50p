"""Module providing a random functions."""
import random

cards = ["jack", "queen", "king"]

def main():
    """Main code block."""
    # setup 'sudo unique number'
    # for each 'seed number' random sequence will be the same - useful for debugging (same results)
    random.seed(10)

    print(f"choice: {random.choice(cards)}")              # get 1
    print(f"choices of 2: {random.choices(cards, k=2)}")  # get some (can be the same)
    print(f"sample of 2: {random.sample(cards, k=2)}")    # get some (every one is unique)

    # assign weight for every item (100% is a sum of all weights)
    print(f"choices of 2 with weights: {random.choices(cards, weights=[75, 20, 5], k=2)}")


if __name__ == "__main__":
    main()
