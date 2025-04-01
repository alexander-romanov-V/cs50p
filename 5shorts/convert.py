"""Convert AU into meters"""


def main():
    """Main code"""
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue

    print(f"{au} AU is {convert(au)} m")


def convert(au):
    """Convert AU into meters"""
    # Check au is a type int or float:
    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or float")
    return au * 149597870700


if __name__ == "__main__":
    main()
