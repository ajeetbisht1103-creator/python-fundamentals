# ----------------------------------------------------
# Description:
# This program demonstrates the use of
# lists, tuples, dictionaries and sets
# through a menu-driven application.
# ----------------------------------------------------

numbers = []
student = ("Ajeet", "CSE")
marks = {}
subjects = set()

while True:

    print("\n========== Collection Manager ==========")
    print("1. Add Number to List")
    print("2. Add Student Marks")
    print("3. Add Subject")
    print("4. Display Collections")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = int(input("Enter Number: "))
        numbers.append(number)

    elif choice == 2:
        name = input("Enter Student Name: ")
        mark = int(input("Enter Marks: "))
        marks[name] = mark

    elif choice == 3:
        subject = input("Enter Subject Name: ")
        subjects.add(subject)

    elif choice == 4:
        print("\nList :", numbers)
        print("Tuple:", student)
        print("Dictionary:", marks)
        print("Set:", subjects)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")