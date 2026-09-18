# ----------------------------------------------------
# Description:
# This program reads student records from a CSV file.
# It calculates the average marks and identifies
# students who scored above the average.
# ----------------------------------------------------

import csv

file_name = "students.csv"

try:
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        students = []

        for row in reader:
            row["marks"] = float(row["marks"])
            students.append(row)

    if not students:
        print("No student records found.")
    else:
        average = sum(s["marks"] for s in students) / len(students)

        print("Average Marks:", round(average, 2))
        print("\nStudents above average:")

        for student in students:
            if student["marks"] > average:
                print(student["name"], "-", student["marks"])

except FileNotFoundError:
    print("CSV file not found.")

except ValueError:
    print("Invalid marks found in the file.")