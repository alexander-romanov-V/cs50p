"""Computer Science Circles tasks"""

def main():
    """Main code"""
    name_game()
    pig_latin()
    next_letter()

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
    print(s[1:]+s[0]+"ay")

def next_letter():
    """Next Letter"""
    c = input()
    if c == "Z":
        c = "A"
    else:
        c = chr(ord(c)+1)
    print(c)

if __name__ == "__mani__":
    main()
