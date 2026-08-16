# ----------------------------------------------------
# Description:
# This program demonstrates the creation of a class
# and objects in Python using student information.
# ----------------------------------------------------

class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

student = Student(name, roll_no, marks)

student.display()