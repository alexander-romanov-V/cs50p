"""Lecture 9.9 - Etc: cli arguments - argparse"""

# classic approach:
#
# import sys
# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage:", sys.argv[0])


# argparse:
import argparse

# description of program [for usage:]
parser = argparse.ArgumentParser(description="Meow like a cat")
# configure our arg '-n' to parse. also adds descriptionof our arg [for usage:]
parser.add_argument("-n", help="number of times to meow")

args = parser.parse_args() # get value X of parsed arg '-n X'
for _ in range(int(args.n)):
    print("meow")
