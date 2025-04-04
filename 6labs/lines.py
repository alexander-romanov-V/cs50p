"""Lines of Code"""

import sys


def main():
    """Main code"""
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(
        ".py"
    ):  # len(sys.argv[1]) < 3 or sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")

    try:
        count = get_lines(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)


def get_lines(file_name):
    """Returns lines of code, except blank and comments #"""
    count = 0
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.lstrip()
            if len(line) > 0 and not line.startswith("#"):  # line[0] != "#":
                count += 1
    return count


if __name__ == "__main__":
    main()
