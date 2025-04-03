import csv

students = []

with open("students.csv", encoding="utf-8") as file:
    reader = csv.reader(file)   # read file as LIST 
    # for row in reader:
    #     students.append({"name": row[0], "house": row[1]})
    for name, house in reader:
        students.append({"name": name, "house": house})

for student in sorted(students, 
                      key=lambda student: student["name"], 
                      reverse=False):
    print(f"{student['name']} is in {student['house']}")
