"""Lecture 9.5 - Etc: constants vs class"""


class Cat:
    """Class cat whic meows"""

    MEOWS = 3  # by convention all CONSTANTS are in capital (actually we can change it)

    def meow(self):
        """Print meow"""

        # explicit point that it is a class constant (not an instance)
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()
