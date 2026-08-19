# ----------------------------------------------------
# Description:
# This program demonstrates object composition and
# object management using a library system.
# ----------------------------------------------------


class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):

        status = "Borrowed" if self.is_borrowed else "Available"

        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("------------------------")


class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def display(self):

        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):

        self.books.append(book)
        print("Book added successfully.")

    def add_member(self, member):

        self.members.append(member)
        print("Member registered successfully.")

    def find_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:
                return book

        return None

    def find_member(self, member_id):

        for member in self.members:

            if member.member_id == member_id:
                return member

        return None

    def display_books(self):

        if not self.books:
            print("No books in the library.")
            return

        print("\n------ Library Books ------")

        for book in self.books:
            book.display()

    def borrow_book(self, book_id, member_id):

        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if book is None:
            print("Book not found.")
            return

        if member is None:
            print("Member not found.")
            return

        if book.is_borrowed:
            print("Book is already borrowed.")
            return

        book.is_borrowed = True

        print(f"{book.title} borrowed by {member.name}.")

    def return_book(self, book_id):

        book = self.find_book(book_id)

        if book is None:
            print("Book not found.")
            return

        if not book.is_borrowed:
            print("Book is already available.")
            return

        book.is_borrowed = False

        print(f"{book.title} returned successfully.")


library = Library()


while True:

    print("\n====== Library Management ======")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Display Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:

        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(book_id, title, author)

        library.add_book(book)

    elif choice == 2:

        member_id = input("Enter member ID: ")
        name = input("Enter member name: ")

        member = Member(member_id, name)

        library.add_member(member)

    elif choice == 3:

        library.display_books()

    elif choice == 4:

        book_id = input("Enter book ID: ")
        member_id = input("Enter member ID: ")

        library.borrow_book(book_id, member_id)

    elif choice == 5:

        book_id = input("Enter book ID: ")

        library.return_book(book_id)

    elif choice == 6:

        print("Exiting library system.")
        break

    else:

        print("Invalid choice.")