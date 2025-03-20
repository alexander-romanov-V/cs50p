name = input("What;s your name? ")

match name:
    case "Harry" | "Hermiony" | "Ron":  # Or
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:                             # Any other case
        print("Who?")


