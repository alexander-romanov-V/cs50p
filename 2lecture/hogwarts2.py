students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor",
    "Draco": "SLytherin"
}
print(students["Ron"])
for student in students:
    print(student, students[student], sep=": ")