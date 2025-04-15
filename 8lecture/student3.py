"""OOP Example 3"""


def main():
    """Main code"""
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"  # CAN assign to the list
    print(f"{student[0]} from {student[1]}")


def get_student():
    """Ask a student"""
    name = input("Name: ")
    house = input("House: ")
    return [name, house]  # list is mutable


if __name__ == "__main__":
    main()
