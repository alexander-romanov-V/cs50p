import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students7.csv", "a", encoding="utf-8") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, home])
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
