"""OOP Example 6 - __init__"""


class Student:
    """Student class"""

    # instance method __init__ (like a constructor)
    def __init__(self, name, house):
        if not name:        # name == ""
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name    # Create new variables inside
        self.house = house  # just created empty object.


def main():
    """Main code"""
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(f"{student.name} from {student.house}")


def get_student():
    """Ask a student"""
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)  # instantiate object


if __name__ == "__main__":
    main()
