# ----------------------------------------------------
# Description:
# This program demonstrates inheritance by creating
# different employee types from a common Employee class.
# ----------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary:.2f}")


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display(self):
        super().display()
        print(f"Team Size: {self.team_size}")


name = input("Enter manager name: ")
salary = float(input("Enter salary: "))
team_size = int(input("Enter team size: "))

manager = Manager(name, salary, team_size)

print("\nManager Details")
manager.display()