# ----------------------------------------------------
# Description:
# This program uses functions to calculate
# the average marks and grade of a student.
# ----------------------------------------------------

def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

average = calculate_average(marks)
grade = calculate_grade(average)

print(f"\nAverage: {average:.2f}")
print(f"Grade: {grade}")