"""Emulate how twitter shorten text"""


def main():
    """Main code"""
    txt = input("Input: ")
    print(f"Output: {shorten(txt)}")


def shorten(word):
    """shorten the text by removing the vowels"""
    res=""
    for c in word:
        match c.lower():
            case "a" | "e" | "i" | "o" | "u":
                continue
            case _:
                res+=c
    return res

if __name__ == "__main__":
    main()
