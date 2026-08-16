# ----------------------------------------------------
# Description:
# This program uses a class to calculate an employee's
# gross salary using basic salary, HRA and allowances.
# ----------------------------------------------------

class Employee:

    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 0.20
        allowance = self.basic_salary * 0.10
        return self.basic_salary + hra + allowance

    def display(self):
        gross_salary = self.calculate_salary()

        print("\nEmployee Salary Details")
        print("Name:", self.name)
        print(f"Basic Salary: ₹{self.basic_salary:.2f}")
        print(f"Gross Salary: ₹{gross_salary:.2f}")


name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))

employee = Employee(name, salary)
employee.display()