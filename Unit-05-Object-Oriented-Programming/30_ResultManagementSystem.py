# ----------------------------------------------------
# Description:
# This program implements an object-oriented student
# result management system using encapsulation,
# methods, validation and grade calculation.
# ----------------------------------------------------

class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = []

    def add_marks(self, mark):
        if 0 <= mark <= 100:
            self.__marks.append(mark)
        else:
            print("Invalid marks. Enter a value from 0 to 100.")

    def calculate_total(self):
        return sum(self.__marks)

    def calculate_average(self):
        if not self.__marks:
            return 0

        return self.calculate_total() / len(self.__marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def display_result(self):
        average = self.calculate_average()

        print("\n----- Student Result -----")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.__marks)
        print("Total:", self.calculate_total())
        print(f"Average: {average:.2f}")
        print("Grade:", self.calculate_grade())


name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

student = Student(name, roll_no)

subjects = int(input("Enter number of subjects: "))

for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    student.add_marks(mark)

student.display_result()