"""OOP Example 10 - classmethods"""

# incapsulate ALL relating to this class inside the class

# also exists @staticmethods ...

class Student:
    """Student class"""

    # instance method __init__ (like a constructor)
    def __init__(self, name, house):
        self.name = name  # call setter (with error checking)
        self.house = house  # call setter (with error checking)

    # __str__ default func to get string of this object (to print it 4 example)
    def __str__(self):
        return f"{self.name} from {self.house}"

    # Class method (can be used without instanciating of object)
    @classmethod
    def get(cls):
        """Ask a student"""
        name = input("Name: ")
        house = input("House: ")
        return cls(
            name, house
        )  # instantiate new object of this class [cls] and return it

    @property
    def name(self):
        """Getter for name"""
        return self._name

    @name.setter
    def name(self, name):
        """Setter for name"""
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        """Getter for house"""
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        """Setter for house"""
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    """Main code"""
    student = Student.get()  # call classmethod and get an instance of this object
    print(student)  # automatic call __str__ func of Student object


if __name__ == "__main__":
    main()
