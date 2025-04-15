"""OOP Example 8 - user function"""


class Student:
    """Student class"""

    # instance method __init__ (like a constructor)
    def __init__(self, name, house, patronus):
        if not name:        # name == ""
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name    # Create new variables inside
        self.house = house  # just created empty object.
        self.patronus = patronus

    # __str__ default func to get string of this object (to print it 4 example)
    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        """Returns charm according patronus"""
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "💂🏽"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    """Main code"""
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
    # print(student)          # automatic call __str__ func of Student object


def get_student():
    """Ask a student"""
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)  # instantiate object


if __name__ == "__main__":
    main()
