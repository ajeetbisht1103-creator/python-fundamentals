# ----------------------------------------------------
# Description:
# This program demonstrates data hiding using a
# private attribute and controlled access through
# getter and setter methods.
# ----------------------------------------------------

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100.")


name = input("Enter student name: ")
marks = float(input("Enter marks: "))

student = Student(name, marks)

print("\nStudent:", student.name)
print("Marks:", student.get_marks())

new_marks = float(input("Enter updated marks: "))
student.set_marks(new_marks)

print("Updated Marks:", student.get_marks())