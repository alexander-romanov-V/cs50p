"""OOP Example 9 - properties, decorators"""
# decorator - a func what modify behaviour of another func

# int, str, list ... are classes
# class int(x, base=10)
# class str(object='')
# class list([iterable])

class Student:
    """Student class"""

    # instance method __init__ (like a constructor)
    def __init__(self, name, house):
        self.name = name    # call setter (with error checking)
        self.house = house  # call setter (with error checking)

    # __str__ default func to get string of this object (to print it 4 example)
    def __str__(self):
        return f"{self.name} from {self.house}"

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
        return self._house  # conventionally use underscor for variable name (not to collide with func name)

    # Setter
    @house.setter
    def house(self, house):
        """Setter for house"""
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    """Main code"""
    student = get_student()
    student._house = "Number Four, Privet Drive"     # still can access to internal var - please do NOT touch it :)
    print(student)          # automatic call __str__ func of Student object


def get_student():
    """Ask a student"""
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  # instantiate object


if __name__ == "__main__":
    main()
