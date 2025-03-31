"""Work with emoji"""

import emoji

# pip install emoji


def main():
    """Main code block."""
    txt = input("Input: ")
    print(emoji.emojize(txt, language="alias"))


if __name__ == "__main__":
    main()
