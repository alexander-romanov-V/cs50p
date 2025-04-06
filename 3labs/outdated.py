months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    """Main code"""
    while True:
        date = input("Date: ").strip().capitalize()
        date = date.replace(", ", "/").replace(" ", "/").replace(",", "/")
        try:
            m, d, y = date.split("/")
            if m in months:
                m = months.index(m) + 1
            else:
                m = int(m)
            d = int(d)
            y = int(y)
        except ValueError:
            pass
        else:
            if 1 <= d <= 31 and 1 <= m <= 12:
                break

    print(f"{y:04}-{m:02}-{d:02}")


if __name__ == "__main__":
    main()
