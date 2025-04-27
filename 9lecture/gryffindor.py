"""Lecture 9.15 - Etc: filter"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


# pythonic way 1 - create new LIST with conditional
#
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]
for gryffindor in sorted(gryffindors):
    print(gryffindor)


# pythonic way 2 - filter DICT with boolean func
#
# def is_gryffindor(s):
#     """Returns True if it is Gryffindor"""
#     return s["house"] == "Gryffindor"
# gryffindors = filter(is_gryffindor, students)
# # The same, but with lambda:
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
