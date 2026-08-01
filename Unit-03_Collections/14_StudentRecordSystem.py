# ----------------------------------------------------
# Description:
# This program stores student details
# using a dictionary and displays them.
# ----------------------------------------------------

student = {}

student["Name"] = input("Enter Name: ")
student["Roll No"] = input("Enter Roll Number: ")
student["Branch"] = input("Enter Branch: ")
student["CGPA"] = float(input("Enter CGPA: "))

print("\nStudent Record")

for key, value in student.items():
    print(f"{key}: {value}")