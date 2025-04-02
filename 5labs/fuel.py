"""Fuel Gauge - Refueling"""


def main():
    """Main code"""
    while True:
        try:
            lvl = convert(input("Fraction: "))
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(lvl))


def convert(fraction):
    """Convert fraction to decimal"""
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return round(100 * x / y)


def gauge(percentage):
    """Return E, F, or % according of percentage"""
    if not isinstance(percentage, int):
        return ""

    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"

    return f"{percentage}%"


if __name__ == "__main__":
    main()
