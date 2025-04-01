"""Test calculator's functions"""

from calculator import square


def main():
    """Main test code"""
    test_square()


def test_square():
    """Test square() function"""

    # 2. Improved approach
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squares was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squares was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squares was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squares was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squares was not 0")

    # 1. Basic approach
    # if square(2) != 4:
    #     print("2 squares was not 4")
    # if square(3) != 9:
    #     print("3 squares was not 9")


if __name__ == "__main__":
    main()
