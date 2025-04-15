"""OOP Example 7 - __str__"""


class Student:
    """Student class"""

    # instance method __init__ (like a constructor)
    def __init__(self, name, house):
        if not name:  # name == ""
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name  # Create new variables inside
        self.house = house  # just created empty object.

    # __str__ default func to get string of this object (to print it 4 example)
    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    """Main code"""
    student = get_student()
    print(student)  # automatic call __str__ func of Student object


def get_student():
    """Ask a student"""
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  # instantiate object


if __name__ == "__main__":
    main()
