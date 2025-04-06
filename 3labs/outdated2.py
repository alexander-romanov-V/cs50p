def main():
    """Main code"""
    while True:
        date = input("Date: ").strip().capitalize()
        try:
            m, d, y = convert_date(date)
            break
        except ValueError:
            pass

    print(f"{y:04}-{m:02}-{d:02}")


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


def convert_date(date):
    date = date.replace(", ", "/").replace(" ", "/").replace(",", "/")
    m, d, y = date.split("/")
    if m in months:
        m = months.index(m) + 1
    else:
        m = int(m)
    d = int(d)
    y = int(y)
    if not (1 <= d <= 31 and 1 <= m <= 12):
        raise ValueError
    return m, d, y


if __name__ == "__main__":
    main()
