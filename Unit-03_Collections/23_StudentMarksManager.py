# ----------------------------------------------------
# Description:
# This program stores marks of students
# and calculates the class average.
# ----------------------------------------------------

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("\nStudent Marks")

total = 0

for name, marks in students.items():
    print(f"{name} : {marks}")
    total += marks

average = total / len(students)

print(f"\nClass Average: {average:.2f}")