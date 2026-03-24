import datetime

library = {}

def input_date(prompt):
    while True:
        date_str = input(prompt + " (YYYY-MM-DD): ").strip()
        try:
            year, month, day = map(int, date_str.split('-'))
            return datetime.date(year, month, day)
        except Exception:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def add_book():
    book_id = input("Enter Book ID: ")
    if book_id in library:
        print("Book with this ID already exists.")
    else:
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        available = input("Is the book available? (yes/no): ").strip().lower() == 'yes'
        library[book_id] = {
            'title': title, 
            'author': author, 
            'available': available,
            'borrow_date': None,
            'due_date': None
        }
        print("Book added successfully.")

def display_books():
    if not library:
        print("No books in the library.")
        return
    print("\nBook List:")
    for book_id, info in library.items():
        status = "Available" if info['available'] else "Not Available"
        borrow_info = ""
        if not info['available'] and info['borrow_date'] and info['due_date']:
            borrow_info = f", Borrowed on: {info['borrow_date'].strftime('%Y-%m-%d')}, Due date: {info['due_date'].strftime('%Y-%m-%d')}"
        print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Status: {status}{borrow_info}")

def search_book():
    book_id = input("Enter Book ID to search: ")
    if book_id in library:
        info = library[book_id]
        status = "Available" if info['available'] else "Not Available"
        borrow_info = ""
        if not info['available'] and info['borrow_date'] and info['due_date']:
            borrow_info = f", Borrowed on: {info['borrow_date'].strftime('%Y-%m-%d')}, Due date: {info['due_date'].strftime('%Y-%m-%d')}"
        print(f"ID: {book_id}, Title: {info['title']}, Author: {info['author']}, Status: {status}{borrow_info}")
    else:
        print("Book not found.")

def borrow_book():
    book_id = input("Enter Book ID to borrow: ")
    if book_id in library:
        if library[book_id]['available']:
            borrow_date = input_date("Enter date of borrow")
            due_date = borrow_date + datetime.timedelta(days=7)
            library[book_id]['available'] = False
            library[book_id]['borrow_date'] = borrow_date
            library[book_id]['due_date'] = due_date
            print(f"Book borrowed successfully. Please return by {due_date.strftime('%Y-%m-%d')}.")
        else:
            info = library[book_id]
            due_info = f" It was borrowed on {info['borrow_date'].strftime('%Y-%m-%d')} and is due by {info['due_date'].strftime('%Y-%m-%d')}." if info['borrow_date'] and info['due_date'] else ""
            print(f"Sorry, the book is currently not available.{due_info}")
    else:
        print("Book not found.")

def return_book():
    book_id = input("Enter Book ID to return: ")
    if book_id in library:
        if not library[book_id]['available']:
            # User input for date of return
            return_date = input_date("Enter the return date")
            due_date = library[book_id]['due_date']
            library[book_id]['available'] = True
            library[book_id]['borrow_date'] = None
            library[book_id]['due_date'] = None
            if due_date and return_date > due_date:
                print("Book returned. You are late! The book was due on {}.".format(due_date.strftime('%Y-%m-%d')))
            else:
                print("Book returned successfully.")
        else:
            print("This book was not borrowed.")
    else:
        print("Book not found.")

def menu():
    print("\n--- Mini Library Management System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

def library_system():
    menu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        borrow_book()
    elif choice == '5':
        return_book()
    elif choice == '6':
        print("Exiting Library System. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")
    # Recursive call to continue the loop
    library_system()

# Start the library management system
library_system()