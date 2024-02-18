
class Library:
    
    
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "a+")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            
    def list_books(self):
        # Method to list all the books in the books.txt file
        with open(self.file_name, "r") as file:
            for line in file:
                book_info = line.strip().split(',')
                print(f"Book: {book_info[0]}, Author: {book_info[1]}")
                
                

    def add_book(self, book_name, author, publish_date, page_count):
        # Method to add a book to the books.txt file
        with open(self.file_name, "a+") as file:
            file.write(f"{book_name},{author},{publish_date},{page_count}\n")

    def remove_book(self, line_number):
        # Kitabın silinmesi istenilen dosyadaki satırı kaldırır
        lines = []
        with open(self.file_name, "r") as file:
            lines = file.readlines()

        line_number = int(line_number)  # Kullanıcının girdisini tamsayıya dönüştür
        if 0 < line_number <= len(lines):
            del lines[line_number - 1]  # Satır numarası 1'den başladığı için, dizideki indeks 1 eksik olmalı

        with open(self.file_name, "w") as file:
            file.writelines(lines)

# Create an object named “lib” with “Library” class
with Library("books.txt") as lib:
    # Create a menu to interact with the “lib” object
    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Exit")

        # Ask user input for menu item
        choice = input("Enter your choice: ")

        if choice == '1':
            # List Books
            print("\nList of Books:")
            lib.list_books()
        elif choice == '2':
            # Add Book
            book_name = input("Enter book title: ")
            author = input("Enter author: ")
            publish_date = input("Enter publish date: ")
            page_count = input("Enter page count: ")
            lib.add_book(book_name, author, publish_date, page_count)
            print("Book added successfully!")
        elif choice == '3':
            # Remove Book
            book_title = input("Enter the title of the book to remove: ")
            lib.remove_book(book_title)
            print("Book removed successfully!")
        elif choice == '4':
            # Exit
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")