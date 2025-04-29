"""Computer Science Circles tasks"""

# https://cscircles.cemc.uwaterloo.ca/
# Each func it is actually separate task (that's why repeated imports)


def main():
    """Main code"""

    # next_letter()
    # pig_latin()
    # name_game()

    # aggsactly()
    # divisibility()
    # pizza_circles()

    # geometric_mean()
    # gravity()
    # one_triangle()

    # square_census()
    # finding_factors()

    # python_adder()
    # substring_counting()
    # watch_the_pendulum()

    # centering_text()
    # ending_time()
    # character_map()

    # absolute_value()
    # first_second_third()
    # letters()

    # print(lower_string("TEST string"))

    # print("Hypotenuse (a=3, b=4):", hypotenuse(3, 4))
    # print("Perimeter right triangle (a=3, b=4):", right_triangle_perimeter(3, 4))
    # print("Distance between (10, 15) and (13, 11):", distance_2d(10, 15, 13, 11))
    # print("Perimeter any triangle (5, 1) (7, 10) (4, 3):", f"{triangle_perimeter(5, 1, 7, 10, 4, 3):.2f}")

    # lucky_sevens()
    # print(middle([8, 0, 100, 12, 1]))
    # print(natural_numbers(5))
    # print(is_palindrome("racecar"))
    # print(prod([2, 3, 4]))
    # print(replace([3, 1, 4, 1, 5, 9], 1, 7))
    # print(postalValidate("d4s0s2 "))


def getBASIC():
    """BASIC: Reading the Program"""
    res = []
    while True:
        try:
            line = input()
            res.append(line)
        except EOFError:
            return res


def postal_validate(S):
    """Exact Postage"""
    S = S.replace(" ", "").upper()
    if len(S) != 6:
        return False
    for i in range(3):
        if not S[i * 2].isalpha() or not S[i * 2 + 1].isdigit():
            return False
    return S


def replace(list, X, Y):
    """The Replacements"""
    for _ in range(list.count(X)):
        i = list.index(X)
        list.pop(i)
        list.insert(i, Y)
    return list


def prod(L):
    """Product"""
    res = 1
    for i in L:
        res *= i
    return res


def is_palindrome(S):
    """Palindrome"""
    for i in range(len(S) // 2):
        if S[i] != S[-(i + 1)]:
            return False
    return True


def natural_numbers(n):
    """It's Natural"""
    res = [0] * n
    for i in range(n):
        res[i] = i + 1
    return res


def middle(L):
    """Monkey in the Middle"""
    return L[len(L) // 2]


def lucky_sevens():
    """Lucky Sevens"""
    for i in range(10, 100, 10):
        print(i + 7)


def hypotenuse(a, b):
    """Compute the length of a right triangle's hypotenuse"""
    import math

    return math.sqrt(a**2 + b**2)


def right_triangle_perimeter(a, b):
    """Compute the perimeter of a right triangle"""
    return a + b + hypotenuse(a, b)


def distance_2d(x1, y1, x2, y2):
    """Compute the distance between two points in 2D"""
    return hypotenuse(abs(x2 - x1), abs(y2 - y1))


def triangle_perimeter(xA, yA, xB, yB, xC, yC):
    """Compute the perimeter of an arbitrary triangle"""
    return (
        distance_2d(xA, yA, xB, yB)
        + distance_2d(xB, yB, xC, yC)
        + distance_2d(xA, yA, xC, yC)
    )


def lower_char(char):
    """Convert char to lowercase"""
    return chr(ord(char) - ord("A") + ord("a")) if "A" <= char <= "Z" else char


def lower_string(string):
    """Convert string to lowercase"""
    result = ""
    for c in string:
        result += lower_char(c)
    return result


def letters():
    """26 Letters"""
    letter = input()
    if "A" <= letter <= "Z":
        print(ord(letter) - ord("A") + 1)
    else:
        print("invalid")


def first_second_third():
    """First, Second, Third"""
    n = int(input())
    if n == 1:
        e = "st"
    elif n == 2:
        e = "nd"
    elif n == 3:
        e = "rd"
    else:
        e = "th"
    print(f"{n}{e}")


def absolute_value():
    """Absolute Value"""
    x = int(input())
    print(max(-x, x))


def character_map():
    """Character Map"""
    n = 32  # start number
    for r in range(6):
        nn = n + r * 16
        print("chr:", end="")
        for i in range(16):
            print(f"{chr(nn+i):>3}", end=" ")
        print("\nasc:", end="")
        for i in range(16):
            print(f" {(nn+i):^3}", end="")
        print()


def ending_time():
    """Ending Time"""
    h, m = input().strip().split(":")
    d = int(input())
    h, m = int(h), int(m)
    h = (h + (m + d) // 60) % 24
    m = (m + d) % 60
    print(f"{h:02}:{m:02}")


def centering_text():
    """Centering Text"""
    # Option 1
    # width = int(input())
    # lines = []
    # while (line := input()) != "END":
    #     lines.append(line.center(width, "."))
    # print(*lines, sep="\n")
    #
    # Option 2
    # width = int(input())
    # lines = []
    # while True:
    #     line = input()
    #     if line == "END":
    #         break
    #     lines.append(line)
    # for line in lines:
    #     print(line.center(width, "."))
    #
    # Option 3 (left dots must be gerater of rights if not equals)
    width = int(input())
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lenght = len(line)
        half = (width - lenght) // 2
        lines.append("." * (width - lenght - half) + line + "." * half)
    print(*lines, sep="\n")


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
