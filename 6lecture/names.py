name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()                      # do not forget to close it

# Pythonic way - use WITH - it automatically call file.CLOSE at the end
with open("names.txt", "a", encoding="utf-8") as file:
    file.write(f"{name}\n")
