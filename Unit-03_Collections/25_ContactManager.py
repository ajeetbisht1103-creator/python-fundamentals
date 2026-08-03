# ----------------------------------------------------
# Description:
# This program manages contacts using
# a dictionary. Users can add, search
# and delete contacts.
# ----------------------------------------------------

contacts = {}

while True:
    print("\n===== Contact Manager =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone

    elif choice == 2:
        name = input("Enter Name to Search: ")

        if name in contacts:
            print(f"Phone Number: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == 4:
        print("\nContact List")

        for name, phone in contacts.items():
            print(f"{name} : {phone}")

    elif choice == 5:
        print("Exiting Contact Manager...")
        break

    else:
        print("Invalid choice.")