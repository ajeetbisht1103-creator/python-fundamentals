# ----------------------------------------------------
# Description:
# This program demonstrates multiple inheritance
# by combining academic and sports information
# into a single Student class.
# ----------------------------------------------------

class Academic:

    def __init__(self, marks):
        self.marks = marks

    def display_marks(self):
        print("Academic Marks:", self.marks)


class Sports:

    def __init__(self, sports_score):
        self.sports_score = sports_score

    def display_sports_score(self):
        print("Sports Score:", self.sports_score)


class Student(Academic, Sports):

    def __init__(self, name, marks, sports_score):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_score)
        self.name = name

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        self.display_marks()
        self.display_sports_score()
        print("Overall Score:", self.marks + self.sports_score)


name = input("Enter student name: ")
marks = float(input("Enter academic marks: "))
sports_score = float(input("Enter sports score: "))

student = Student(name, marks, sports_score)

student.display()