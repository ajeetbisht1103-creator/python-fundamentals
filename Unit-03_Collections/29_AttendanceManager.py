# ----------------------------------------------------
# Description:
# This program manages attendance using
# sets and finds absent students.
# ----------------------------------------------------

all_students = set(input("Enter all student names: ").split())

present_students = set(input("Enter present student names: ").split())

absent_students = all_students - present_students

print("\nPresent Students:")
print(present_students)

print("\nAbsent Students:")
print(absent_students)