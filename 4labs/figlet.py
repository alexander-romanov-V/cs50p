"""Work with system, random and figlet"""

import sys
import random
import pyfiglet

# pip install pyfiglet

def main():
    """Main code"""
    figlet = pyfiglet.Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        fnt = random.choice(fonts)
    elif (
        len(sys.argv) == 3
        and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
        and sys.argv[2] in fonts
    ):
        fnt = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    txt = input("Input: ")
    figlet.setFont(font=fnt)
    print(figlet.renderText(txt))


if __name__ == "__main__":
    main()
