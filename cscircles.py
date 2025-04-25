"""Computer Science Circles tasks"""

# https://cscircles.cemc.uwaterloo.ca/
# Each func it is actually separate task (that why repeated imports)


def main():
    """Main code"""

    watch_the_pendulum()
    substring_counting()
    python_adder()

    # finding_factors()
    # square_census()

    # one_triangle()
    # gravity()
    # geometric_mean()

    # pizza_circles()
    # divisibility()
    # aggsactly()

    # name_game()
    # pig_latin()
    # next_letter()


def watch_the_pendulum():
    """Watch the Pendulum"""
    import math

    L = float(input())
    A = float(input())
    for T in range(10):
        print(L * math.cos(A * math.cos(T * math.sqrt(9.8 / L))) - L * math.cos(A))


def substring_counting():
    """Substring Counting"""
    # needle = input()  # "an"
    # haystack = input()  # "trans-Panamanian banana"
    needle = "sses"
    haystack = "assesses"
    # OVERLAPPING count: sum 1 if startswith
    print(
        sum(
            1
            for i in range(len(haystack) - len(needle) + 1)
            if haystack.startswith(needle, i)
        )
    )
    # OVERLAPPING count: sum of [True, False, ..., True] -> int(True) == 1
    # print(
    #     sum(
    #         [
    #             haystack.startswith(needle, i)
    #             for i in range(len(haystack) - len(needle) + 1)
    #         ]
    #     )
    # )
    # print(haystack.count(needle)) # NON-overlapping


def python_adder():
    """Python Adder"""
    S = input()
    a, b = S.split("+")
    print(int(a) + int(b))


def finding_factors():
    """Finding Factors"""
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j == n:
                print(f"{i} times {j} equals {n}")


def square_census():
    """Square Census"""
    import math

    n = int(input())
    i = 1
    while i**2 < n:
        print(i**2)
        i += 1


def one_triangle():
    """One Triangle"""
    n = int(input())
    for i in range(n, 0, -1):
        print("1" * i)


def gravity():
    """Gravity"""
    import math

    v = float(input())
    t = (v - math.sqrt(v**2 - 4 * (-4.9) * 11000)) / (2 * (-4.9))
    print(t)


def geometric_mean():
    """Geometric Mean"""
    import math

    a = float(input())
    b = float(input())
    print(math.sqrt(a * b))


def pizza_circles():
    """Pizza Circles"""
    import math

    r = float(input())
    s = math.pi * r**2
    print(s)


def divisibility():
    """Divisibility"""
    a = int(input())
    b = int(input())
    if a % b == 0:
        print("divisible")
    else:
        print("not divisible")


def aggsactly():
    """Eggsactly"""
    eggs = int(input())
    cartons = eggs // 12
    free = eggs % 12
    print(cartons)
    print(free)


def name_game():
    """The Name Game"""
    s = input()
    print(f"{s}, {s}, bo-b{s[1:]}")
    print(f"banana-fana fo-f{s[1:]}")
    print(f"fee-fi-mo-m{s[1:]}")
    print(f"{s}!")


def pig_latin():
    """Pig Latin"""
    s = input()
    print(s[1:] + s[0] + "ay")


def next_letter():
    """Next Letter"""
    c = input()
    if c == "Z":
        c = "A"
    else:
        c = chr(ord(c) + 1)
    print(c)


if __name__ == "__main__":
    main()
