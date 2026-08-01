# ----------------------------------------------------
# Description:
# This program demonstrates basic
# dictionary operations.
# ----------------------------------------------------

student = {
    "Name": "Ajeet",
    "Age": 19,
    "Branch": "CSE"
}

print("Student Details:")
print(student)

print("\nName:", student["Name"])

student["Age"] = 20

student["City"] = "Jalandhar"

print("\nUpdated Dictionary:")
print(student)