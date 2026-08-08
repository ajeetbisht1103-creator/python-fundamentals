# ----------------------------------------------------
# Description:
# This program demonstrates keyword arguments
# by generating a student's profile.
# ----------------------------------------------------

def display_student(name, age, branch, year):
    print("\nStudent Profile")
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Branch : {branch}")
    print(f"Year   : {year}")


name = input("Enter name: ")
age = int(input("Enter age: "))
branch = input("Enter branch: ")
year = int(input("Enter year: "))

display_student(
    name=name,
    age=age,
    branch=branch,
    year=year
)