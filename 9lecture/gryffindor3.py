"""Lecture 9.17 - Etc: enumerate"""

# enumerate(iterable, start=0)

students = ["Hermione", "Harry", "Ron"]


for i, student in enumerate(students, start=1):
    print(i, student)
# 1 Hermione
# 2 Harry
# 3 Ron
