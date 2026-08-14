# ----------------------------------------------------
# Description:
# This program sorts a list of tuples based on
# the second element using a lambda function.
# ----------------------------------------------------

students = [
    ("Aman", 78),
    ("Riya", 92),
    ("Karan", 65),
    ("Neha", 85)
]

students.sort(key=lambda student: student[1])

print("Students sorted by marks:")

for student in students:
    print(student[0], "-", student[1])