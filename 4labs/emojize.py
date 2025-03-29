import emoji

def main():
    txt = input("Input: ")
    print(emoji.emojize(txt, language='alias'))


if __name__ == "__main__":
    main()