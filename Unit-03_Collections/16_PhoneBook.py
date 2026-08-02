# ----------------------------------------------------
# Description:
# This program implements a simple phone
# book using a dictionary. The user can
# add contacts and search for a contact.
# ----------------------------------------------------

phone_book = {}

n = int(input("How many contacts do you want to add? "))

for i in range(n):
    name = input("Enter Name: ")
    number = input("Enter Phone Number: ")
    phone_book[name] = number

search_name = input("\nEnter name to search: ")

if search_name in phone_book:
    print(f"{search_name}'s Number: {phone_book[search_name]}")
else:
    print("Contact not found.")