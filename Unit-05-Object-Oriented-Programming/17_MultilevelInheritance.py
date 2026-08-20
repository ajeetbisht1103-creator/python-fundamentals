# ----------------------------------------------------
# Description:
# This program demonstrates multilevel inheritance
# using Person, Employee and Manager classes.
# ----------------------------------------------------

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


class Manager(Employee):

    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def display(self):
        print("\nManager Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)


name = input("Enter name: ")
age = int(input("Enter age: "))
employee_id = input("Enter employee ID: ")
department = input("Enter department: ")

manager = Manager(name, age, employee_id, department)

manager.display()