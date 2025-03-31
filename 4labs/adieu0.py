"""Write an Adiey song"""


def main():
    """Main code"""

    names = []

    while True:
        try:
            name = input("Name: ")
            if name != "":
                names.append(name)
        except EOFError:
            break

    song = "Adieu, adieu, to "
    if len(names) > 1:
        song += ", ".join(names[:-1])
        if len(names) > 2:
            song += ","
        song += " and " + names[len(names) - 1]
    elif len(names) == 1:
        song += names[0]

    print(song)


if __name__ == "__main__":
    main()
