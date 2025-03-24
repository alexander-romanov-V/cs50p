def main():
    history = []

    while True:
        action = input("Action: ").capitalize()
        match action:
            case "Undo":
                if len(history) > 0:
                    undone = history.pop()
                    print(f"Undone: {undone}")
                else:
                    print("Nothing to undone!")
            case "Restart":
                history.clear()
                print("Game was restarted!")
            case _:
                history.append(action)
        
        print(history)



main()