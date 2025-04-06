def main():
    """Main code"""
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            f = convert(x, y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    if f <= 1:
        print("E")
    elif f >= 99:
        print("F")
    else:
        print(f"{f}%")


def convert(x, y):
    x = int(x)
    y = int(y)
    if x > y or y == 0:
        raise ValueError
    return int(100 * x / y)


if __name__ == "__main__":
    main()
