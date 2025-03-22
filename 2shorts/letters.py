def main():
    # print(write_letter("Mario", "Princess Peach"))
    # print(write_letter("Luigi", "Princess Peach"))
    # print(write_letter("Daisy", "Princess Peach"))
    # print(write_letter("Yoshi", "Princess Peach"))

    # for sender in ["Mario", "Luigi", "Daisy", "Yoshi"]:
    #     print(write_letter(sender, "Princess Peach"))

    persons = ["Mario", "Luigi", "Daisy", "Yoshi", "Bowser"]
    # for i in range(len(persons)):
    #     print(write_letter(persons[i], "Princess Peach"))
    for person in persons:
        print(write_letter(person, "Princess Peach"))



def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        dear {receiver},

        You are cordinally inited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


main()
