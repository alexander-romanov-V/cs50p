import csv

students = []

with open("students6.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)   # read file as DICTIONARY

#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, 
#                       key=lambda student: student["name"], 
#                       reverse=False):
#     print(f"{student['name']} is from {student['home']}")

    for student in sorted(reader, key=lambda s: s["name"]):
        print(f"{student['name']} is from {student['home']}")
