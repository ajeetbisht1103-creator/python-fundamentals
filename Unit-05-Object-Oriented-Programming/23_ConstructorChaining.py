# ----------------------------------------------------
# Description:
# This program demonstrates constructor chaining
# using super() to initialize attributes from
# multiple levels of inheritance.
# ----------------------------------------------------

class Person:

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id


class Developer(Employee):

    def __init__(self, name, employee_id, language):
        super().__init__(name, employee_id)
        self.language = language

    def display(self):
        print("\nDeveloper Details")
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Programming Language:", self.language)


name = input("Enter developer name: ")
employee_id = input("Enter employee ID: ")
language = input("Enter programming language: ")

developer = Developer(name, employee_id, language)

developer.display()