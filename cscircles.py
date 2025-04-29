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

    # print(find_line(["10 GOTO 20", "20 END"], "10"))
    # print(execute(["10 GOTO 21", "21 GOTO 37", "37 GOTO 21", "40 END"]))
    # print(execute(["5 GOTO 30", "10 GOTO 20", "20 GOTO 10", "30 GOTO 40", "40 END"]))

    # temperature_converter()
    # print(check("9384 3495 3297 0123"))
    # print(check("9384 3495 3297 0121"))

    # poetic_analysis()
    # print(choose(8, 5))
    # print(shift_code("SPY CODER", 5))
    # print(shift_decode("HUD", 6))
    print(auto_decode("IQQF"))


def auto_decode(s):
    """Auto-Decryption"""
    letterGoodness = [
        0.0817, 0.0149, 0.0278, 0.0425, 0.1270, 0.0223,
        0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241,
        0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633,
        0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007,
    ]
    def goodness(s):
        r = 1
        for c in s:
            r *= letterGoodness[(ord(c) - ord('A'))] if "A" <= c <= "Z" else 1
        return r
    goodnesses = [goodness(shift_decode(s, i)) for i in range(26)]
    return shift_decode(s, goodnesses.index(max(goodnesses)))


def shift_decode(s, n):
    """Spy Decoder"""
    r = ""
    for c in s.upper():
        r += chr((ord(c) - ord("A") + 26 - n) % 26 + ord("A")) if "A" <= c <= "Z" else c
    return r


def shift_code(s, n):
    """Spy Coder"""
    r = ""
    for c in s.upper():
        r += chr((ord(c) - ord("A") + n) % 26 + ord("A")) if "A" <= c <= "Z" else c
    return r


def choose(n, k):
    """Be Choosy"""
    # from math import factorial
    # return factorial(n) // (factorial(k) * factorial(n - k))
    numerator = 1
    for i in range(n, n - k, -1):
        numerator *= i
    denominator = 1
    for i in range(k, 1, -1):
        denominator *= i
    return numerator // denominator


def poetic_analysis():
    """Poetic Analysis"""
    lines = ""
    while (line := input()) != "###":
        lines += " " + line
    words = {}
    for line in lines.lower().split():
        words[line] = 1 + words.get(line, 0)
    print(max(words, key=lambda w: words[w]))


def check(S):
    """Credit Check"""

    import re

    if not re.search(r"^(\d{4} ){3}\d{4}$", S):
        return False
    if sum(int(c) for c in S if "0" <= c <= "9") % 10 > 0:
        return False
    return True


def temperature_converter():
    """Forty Below In The Winter"""
    s = input().strip()
    t = float(s[:-1])
    cf = s[-1:].upper()
    if cf == "C":
        t = round(t * 9 / 5 + 32, 3)
        print(f"{t}F")
    elif cf == "F":
        t = round((t - 32) * 5 / 9, 3)
        print(f"{t}C")
    else:
        print("error")


def get_basic():
    """BASIC: Reading the Program"""
    res = []
    while True:
        try:
            line = input()
            res.append(line)
        except EOFError:
            return res


def find_line(prog, target):
    """BASIC: Go to it!"""
    for i, line in enumerate(prog):
        if line.startswith(target):
            return i
    return 0


def execute(prog):
    """Smart Simulation"""
    location = 0
    visited = [False] * len(prog)
    while not visited[location]:
        visited[location] = True
        cmd = prog[location].split()
        if cmd[1] == "END":
            return "success"
        if len(cmd) == 3 and cmd[1].upper() == "GOTO":
            location = find_line(prog, cmd[2])
        else:
            location += 1
    return "infinite loop"


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
