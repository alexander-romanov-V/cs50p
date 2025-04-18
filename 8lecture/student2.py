"""OOP Example 2"""


def main():
    """Main code"""
    student = get_student()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"    # Can NOT assign to tuple
    print(f"{student[0]} from {student[1]}")


def get_student():
    """Ask a student"""
    name = input("Name: ")
    house = input("House: ")
    return (
        name,
        house,
    )  # tuple is immutable !!!    (Can be nested - use round brackets )


if __name__ == "__main__":
    main()
