"""OOP Example 2"""

def main():
    """Main code"""
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    """Ask a student"""
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()
