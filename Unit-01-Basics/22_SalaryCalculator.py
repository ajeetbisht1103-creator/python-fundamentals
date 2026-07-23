# ----------------------------------------------------
# Description:
# This program calculates the gross salary
# of an employee using HRA and DA.
# ----------------------------------------------------

basic_salary = float(input("Enter Basic Salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10

gross_salary = basic_salary + hra + da

print(f"HRA: ₹{hra:.2f}")
print(f"DA: ₹{da:.2f}")
print(f"Gross Salary: ₹{gross_salary:.2f}")