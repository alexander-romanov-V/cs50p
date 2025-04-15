"""class methods"""

# @classmethod

import random


class Hat:
    """One Hat for msny uses"""

    # class variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # use vars of class [cls] (not instance [self])
    @classmethod
    def sort(cls, name):
        """Get a home for passed name"""
        print(name, "is in", random.choice(cls.houses))  # use class variable


# can use class method without creating of instance of this class
Hat.sort("Harry")
