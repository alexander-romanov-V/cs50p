def main():
    s = input()
    print(convert(s))


def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")


main()
