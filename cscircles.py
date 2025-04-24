"""Computer Science Circles tasks"""


def main():
    """Main code"""
    one_triangle()
    gravity()
    geometric_mean()
    pizza_circles()
    divisibility()
    aggsactly()
    name_game()
    pig_latin()
    next_letter()


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


if __name__ == "__mani__":
    main()
