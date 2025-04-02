"""Vanity Plates"""


def main():
    """Main code"""
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """Check validity of plate"""
    if 2 <= len(s) <= 6:
        a = d = 0
        for c in s:
            if d == 0 and c.isalpha():
                a += 1
            elif a >= 2 and c.isdecimal() and not (d == 0 and c == "0"):
                d += 1
            else:
                return False
    else:
        return False

    return True


if __name__ == "__main__":
    main()
