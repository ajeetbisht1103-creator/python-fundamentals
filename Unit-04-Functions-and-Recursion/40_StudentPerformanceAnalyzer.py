# ----------------------------------------------------
# Description:
# This program analyzes student marks using
# multiple user-defined functions.
# It calculates total, average, grade and result.
# ----------------------------------------------------

def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


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


def check_result(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"

    return "Pass"


marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = calculate_total(marks)
average = calculate_average(marks)
grade = calculate_grade(average)
result = check_result(marks)

print("\n----- Performance Report -----")
print("Total Marks:", total)
print(f"Average: {average:.2f}")
print("Grade:", grade)
print("Result:", result)

