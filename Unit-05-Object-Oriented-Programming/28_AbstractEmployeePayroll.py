# ----------------------------------------------------
# Description:
# This program demonstrates abstraction and polymorphism
# by calculating salaries differently for permanent
# and contract employees.
# ----------------------------------------------------

from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class PermanentEmployee(Employee):

    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class ContractEmployee(Employee):

    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


name = input("Enter employee name: ")

print("\n1. Permanent Employee")
print("2. Contract Employee")

choice = int(input("Enter employee type: "))

if choice == 1:
    salary = float(input("Enter monthly salary: "))
    employee = PermanentEmployee(name, salary)

elif choice == 2:
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    employee = ContractEmployee(name, hours, rate)

else:
    employee = None
    print("Invalid choice.")

if employee:
    print(f"\nEmployee: {employee.name}")
    print(f"Salary: ₹{employee.calculate_salary():.2f}")