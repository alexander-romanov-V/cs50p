"""Lecture 9.9 - Etc: cli arguments - argparse"""

import argparse

# description of program [for usage:]
parser = argparse.ArgumentParser(description="Meow like a cat")
# configure our arg '-n' to parse. also adds descriptionof our arg [for usage:].
# default value needs to get rid of error while run program without arg
parser.add_argument("-n", default=1, type=int, help="number of times to meow")

args = parser.parse_args()  # get value X of parsed arg '-n X'
for _ in range(args.n):  # get rid of 'int(args.n)' - specify type of arg as int
    print("meow")


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
