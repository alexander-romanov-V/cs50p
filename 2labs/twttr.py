def main():
    txt_in = input("Input: ")
    txt_out = "".join([succinct(s) for s in txt_in])
    print(f"Output: {txt_out}")


def succinct(s):
    match s.lower():
        case "a" | "e" | "i" | "o" | "u":
            return ""
        case _:
            return s


main()
