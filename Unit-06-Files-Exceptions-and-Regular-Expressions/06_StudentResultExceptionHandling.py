# ----------------------------------------------------
# Description:
# This program demonstrates multiple exception handling
# by validating student marks and calculating average.
# ----------------------------------------------------

try:
    subjects = int(input("Enter number of subjects: "))

    if subjects <= 0:
        raise ValueError("Number of subjects must be positive.")

    marks = []

    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))

        if not 0 <= mark <= 100:
            raise ValueError("Marks must be between 0 and 100.")

        marks.append(mark)

    average = sum(marks) / len(marks)

    print("\n----- Result -----")
    print("Marks:", marks)
    print(f"Average: {average:.2f}")

except ValueError as error:
    print("Invalid input:", error)

except ZeroDivisionError:
    print("Cannot calculate average without marks.")

finally:
    print("Result processing completed.")