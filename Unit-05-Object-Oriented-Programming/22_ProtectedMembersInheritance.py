# ----------------------------------------------------
# Description:
# This program demonstrates the use of protected
# members in a parent class and their access from
# a child class.
# ----------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary


class Manager(Employee):

    def calculate_bonus(self):
        return self._salary * 0.20

    def display(self):
        print("Name:", self.name)
        print(f"Salary: ₹{self._salary:.2f}")
        print(f"Bonus: ₹{self.calculate_bonus():.2f}")


name = input("Enter manager name: ")
salary = float(input("Enter salary: "))

manager = Manager(name, salary)

print("\nManager Details")
manager.display()