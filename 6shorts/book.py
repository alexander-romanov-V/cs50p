"""Book - extract chapter from text"""


def main():
    """Main code"""
    with open("alice.txt", "r", encoding="utf-8") as f:
        contents = f.readlines()
    chapter1 = contents[52:270]
    print(chapter1[0])

    with open("chapter1.txt", "w", encoding="utf-8", newline="") as f:
        f.writelines(chapter1)


if __name__ == "__main__":
    main()
