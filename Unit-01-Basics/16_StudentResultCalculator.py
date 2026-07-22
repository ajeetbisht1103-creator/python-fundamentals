# ----------------------------------------------------
# Description:
# This program calculates the total marks,
# percentage, and average marks of a student
# in five subjects.
# ----------------------------------------------------

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5
average = total / len(marks)

print(f"\nTotal Marks: {total:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Average Marks: {average:.2f}")