"""shorts 8 - Food: class variable & method"""


class Food:
    # class variable
    # good for actually embedding information about the class itself and
    # accessing that through the name of the class
    # not tied to any particular instance of your class
    base_hearts = 1

    # dunder init
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)

    # good for functionality
    # to be shared across all instances of your class
    # good for giving a programmer other ways to make instances of your class.
    @classmethod
    def calculate_hearts(cls, ingredients):
        """Get score of ingredients list"""
        hearts = cls.base_hearts  # access to class variable
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        """make a new instance of this class with default epty list"""
        food = cls(ingredients=[])
        food.hearts = hearts
        return food  # and return just created the instance


def main():
    """Main code"""
    mushroom_skewer = Food(ingredients=["Mushroom", "Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")

    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts!")


if __name__ == "__main__":
    main()
