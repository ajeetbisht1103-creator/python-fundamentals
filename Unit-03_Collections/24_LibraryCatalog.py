# ----------------------------------------------------
# Description:
# This program stores book titles and
# authors using a dictionary and allows
# the user to search for a book.
# ----------------------------------------------------

library = {}

n = int(input("Enter number of books: "))

for i in range(n):
    book = input("Enter book title: ")
    author = input("Enter author name: ")
    library[book] = author

search = input("\nEnter book title to search: ")

if search in library:
    print(f"Author: {library[search]}")
else:
    print("Book not found.")