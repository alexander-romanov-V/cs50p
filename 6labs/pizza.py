"""Pizza Py"""

import sys
import csv
from tabulate import tabulate

# pip install tabulate


def main():
    """Main code"""
    file_name = check_arguments(sys.argv)

    try:
        headers, table = get_table(file_name)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, headers, tablefmt="grid"))  # type: ignore


def check_arguments(argv):
    """Checks arguments - must be exactly one *.csv file"""
    argc = len(argv)
    if argc < 2:
        sys.exit("Too few command-line argumens")
    if argc > 2:
        sys.exit("Too many command-line argumens")
    file_name = argv[1]
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")
    return file_name


def get_table(file_name):
    """Load file_name as SCV. Returns separated headers and tables (as list)"""
    headers = []
    table = []
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for line in reader:
            table.append(line.values())
            # row = []
            # for h in headers:  # type: ignore
            #     row.append(line[h])
            # table.append(row)
    return headers, table


if __name__ == "__main__":
    main()
