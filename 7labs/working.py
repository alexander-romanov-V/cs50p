"""Working 9 to 5"""

import re


def main():
    """Mauin code"""
    print(convert(input("Hours: ")))


def convert(s):
    """Expects a str  of the 12-hour formats and returns the corresponding str in 24-hour format"""
    meridiem = {"AM": 0, "PM": 12}
    pattern = r"(?P<h1>\d{1,2})(:(?P<m1>\d{2}))? (?P<a1>AM|PM) to (?P<h2>\d{1,2})(:(?P<m2>\d{2}))? (?P<a2>AM|PM)"

    if match := re.search(pattern, s):
        h1 = int(match.group("h1"))
        h2 = int(match.group("h2"))
        try:
            m1 = int(match.group("m1"))
        except TypeError:
            m1 = 0
        try:
            m2 = int(match.group("m2"))
        except TypeError:
            m2 = 0
        a1 = meridiem[match.group("a1")]
        a2 = meridiem[match.group("a2")]
        if not (0 <= h1 <= 12 and 0 <= h2 <= 12 and 0 <= m1 <= 59 and 0 <= m2 <= 59):
            raise ValueError
        return f"{(h1+a1)%24:02}:{m1:02} to {(h2+a2)%24:02}:{m2:02}"
    raise ValueError


if __name__ == "__main__":
    main()
