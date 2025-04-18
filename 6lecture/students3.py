students = []

with open("students.csv", encoding="utf-8") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["house"] = house
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

# func key= is called for each element of seq to compare them
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")
