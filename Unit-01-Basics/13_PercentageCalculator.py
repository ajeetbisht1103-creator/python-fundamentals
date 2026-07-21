# ----------------------------------------------------
# Description:
# This program calculates the percentage
# obtained in five subjects.
# ----------------------------------------------------

subject1 = float(input("Enter marks of Subject 1: "))
subject2 = float(input("Enter marks of Subject 2: "))
subject3 = float(input("Enter marks of Subject 3: "))
subject4 = float(input("Enter marks of Subject 4: "))
subject5 = float(input("Enter marks of Subject 5: "))

total = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total / 500) * 100

print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")