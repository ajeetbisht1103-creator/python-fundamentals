# ----------------------------------------------------
# Description:
# This program demonstrates inheritance by creating
# different employee types with different bonus rules.
# ----------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return 0


class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.20


class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.15


name = input("Enter employee name: ")
salary = float(input("Enter salary: "))

print("\n1. Manager")
print("2. Developer")

choice = int(input("Enter employee type: "))

if choice == 1:
    employee = Manager(name, salary)
elif choice == 2:
    employee = Developer(name, salary)
else:
    employee = None
    print("Invalid choice.")

if employee:
    bonus = employee.calculate_bonus()

    print("\nEmployee Details")
    print("Name:", employee.name)
    print(f"Salary: ₹{employee.salary:.2f}")
    print(f"Bonus: ₹{bonus:.2f}")
    print(f"Total Compensation: ₹{employee.salary + bonus:.2f}")