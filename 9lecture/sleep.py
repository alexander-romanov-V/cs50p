"""Lecture 9.18 - Etc: generators [yield], iterators"""


def main():
    """Try to count of sheeps"""
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


# # simple approach
# # out of memory on high 'n' like a 1000000
# # because it generates ALL data at once
# def sheep(n):
#     """Returns a flock of sheeps"""
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock


# generator approach
# like an iterator
# returns [yield] only one value at a time (by each request)
# for loop still be working but will return value on each its iteration
def sheep(n):
    """Returns a row by row of sheeps on each iteration"""
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
