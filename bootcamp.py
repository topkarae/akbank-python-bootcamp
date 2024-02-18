class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            title, author = book.split(',')[:2]
            print(f"Title: {title}, Author: {author}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = self.get_integer_input("Enter first release year: ")
        pages = self.get_integer_input("Enter number of pages: ")
        self.file.write(f"{title},{author},{year},{pages}\n")

    def get_integer_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        for i, book in enumerate(books):
            title = book.split(',')[0]
            if title == title_to_remove:
                del books[i]
                break
        self.file.truncate(0)
        for book in books:
            self.file.write(f"{book}\n")

lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    choice = input("Choose an option: ")
    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid option, please try again.")
