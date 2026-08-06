# ----------------------------------------------------
# Description:
# This program stores employee records
# using nested dictionaries.
# ----------------------------------------------------

employees = {}

n = int(input("Enter number of employees: "))

for i in range(n):
    employee_id = input("\nEnter Employee ID: ")

    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employees[employee_id] = {
        "Name": name,
        "Department": department,
        "Salary": salary
    }

print("\nEmployee Records\n")

for employee_id, details in employees.items():
    print(f"Employee ID : {employee_id}")
    print(f"Name        : {details['Name']}")
    print(f"Department  : {details['Department']}")
    print(f"Salary      : ₹{details['Salary']}")
    print("-" * 30)