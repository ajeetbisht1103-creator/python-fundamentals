# ----------------------------------------------------
# Description:
# This program stores student names and marks in a file,
# then reads the file and calculates the average marks.
# ----------------------------------------------------

filename = "students.txt"

try:
    count = int(input("Enter number of students: "))

    with open(filename, "w") as file:
        for i in range(count):
            name = input(f"Enter name of student {i + 1}: ")
            marks = float(input(f"Enter marks of {name}: "))

            if not 0 <= marks <= 100:
                raise ValueError("Marks must be between 0 and 100.")

            file.write(f"{name},{marks}\n")

    total = 0
    students = 0

    with open(filename, "r") as file:
        for line in file:
            name, marks = line.strip().split(",")
            total += float(marks)
            students += 1

    average = total / students

    print("\n----- Student Report -----")
    print("Students:", students)
    print(f"Average Marks: {average:.2f}")

except ValueError as error:
    print("Error:", error)

except ZeroDivisionError:
    print("No student records available.")

finally:
    print("File processing completed.")