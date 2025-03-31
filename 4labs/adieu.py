"""Write an Adiey song, using inflect"""

import inflect

# pip install inflect


def main():
    """Main code"""

    names = []
    p = inflect.engine()

    while True:
        try:
            name = input("Name: ")
            if name != "":
                names.append(name)
        except EOFError:
            break

    song = "Adieu, adieu, to " + p.join(names)
    print(song)


if __name__ == "__main__":
    main()
