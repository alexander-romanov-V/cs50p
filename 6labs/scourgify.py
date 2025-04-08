"""Scourgify"""

import sys
import csv


def main():
    """Main code"""
    in_f_name, out_f_name = check_arguments(sys.argv)
    try:
        convert(in_f_name, out_f_name)
    except FileNotFoundError:
        sys.exit(f"Could not read {in_f_name}")


def check_arguments(argv):
    """Checks arguments - must be exactly two different *.csv files"""
    argc = len(argv)
    if argc < 3:
        sys.exit("Too few command-line argumens")
    if argc > 3:
        sys.exit("Too many command-line argumens")
    in_f_name = argv[1]
    out_f_name = argv[2]
    if not (in_f_name.lower().endswith(".csv") and out_f_name.lower().endswith(".csv")):
        sys.exit("Not a CSV file")
    if in_f_name == out_f_name:
        sys.exit("Input and output files must be different files")

    return in_f_name, out_f_name


def convert(in_f_name, out_f_name):
    """Converts in.csv [name,house] into out.csv [first,last,house]"""
    with open(in_f_name, "r", encoding="utf-8") as in_f, \
         open(out_f_name, "w", encoding="utf-8", newline="") as out_f:
        reader = csv.DictReader(in_f)
        writer = csv.DictWriter(out_f, fieldnames=["first", "last", "house"])  # type: ignore
        writer.writeheader()
        for row in reader:
            row["first"], row["last"] = row["name"].split(",")
            row.pop("name")
            writer.writerow(row)


if __name__ == "__main__":
    main()
