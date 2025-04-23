"""Lecture 9.16 - Etc: dictionary comprehensions"""

students = ["Hermione", "Harry", "Ron"]

# # simple way 1
#
# gryffindors = []
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# pythonic way 2
#
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
# Result: lsit of dictionaries
# [{'name': 'Hermione', 'house': 'Gryffindor'},
#  {'name': 'Harry', 'house': 'Gryffindor'},
#  {'name': 'Ron', 'house': 'Gryffindor'}]

# pythonic way 3
#
# dictionary comprehensions
gryffindors = {student: "Gryffindor" for student in students}
# Result: one big dictionary
# {'Hermione': 'Gryffindor',
#  'Harry': 'Gryffindor',
#  'Ron': 'Gryffindor'}

print(gryffindors)
