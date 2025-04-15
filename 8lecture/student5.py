"""OOP Example 5 - CLASSES"""


class Student:
    """Student class"""

    ...  # instance variables
    # name: str
    # house: str


def main():
    """Main code"""
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(f"{student.name} from {student.house}")


def get_student():
    """Ask a student"""
    student = Student()
    # instance variables:
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
