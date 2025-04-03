students = []

with open("students.csv", encoding="utf-8") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# def get_name(student):
#     return student["name"]
# func key= is called for each element of seq to compare them

# use lambda - anonymous func
for student in sorted(students, 
                      # lambda's parameter(s)   return value
                      key=lambda student:       student["name"], 
                      reverse=False):
    print(f"{student['name']} is in {student['house']}")
