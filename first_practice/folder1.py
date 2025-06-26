class Library:
    def _init_(self):
       self.books = ["Python", "Maths", "English", "Science"]

    def show_books(self):
        print("Books in library:")
        for book in self.books:
            print(book)

    def get_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(book_name)
        else:
            print("Book not available")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(book_name)


lib = Library()

while True:
    print("1. Show books")
    print("2. get book")
    print("3. Return book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.show_books()
    elif choice == "2":
        name = input("Enter book name to borrow: ")
        lib.get_book(name)
    elif choice == "3":
        name = input("Enter book name to return: ")
        lib.return_book(name)
    elif choice == "4":
        print("Thanks for visiting the library!")
        break
    else:
        print("Invalid choice. Try again.")
