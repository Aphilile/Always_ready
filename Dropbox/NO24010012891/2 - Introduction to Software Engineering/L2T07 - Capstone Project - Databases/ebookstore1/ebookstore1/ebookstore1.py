import sqlite3

# Step 1: Set up the SQLite database and table
def create_database():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            qty INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def populate_database():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    books = [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ]
    c.executemany('INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)', books)
    conn.commit()
    conn.close()

# Step 2: Create functions for adding, updating, deleting, and searching books
def add_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    c.execute('INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', (id, title, author, qty))
    conn.commit()
    conn.close()
    print("Book added successfully.")

def update_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    id = int(input("Enter book ID to update: "))
    title = input("Enter new title: ")
    author = input("Enter new author: ")
    qty = int(input("Enter new quantity: "))
    c.execute('UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?', (title, author, qty, id))
    conn.commit()
    conn.close()
    print("Book updated successfully.")

def delete_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    id = int(input("Enter book ID to delete: "))
    c.execute('DELETE FROM book WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print("Book deleted successfully.")

def search_books():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    search_term = input("Enter search term (title or author): ")
    c.execute('SELECT * FROM book WHERE title LIKE ? OR author LIKE ?', ('%' + search_term + '%', '%' + search_term + '%'))
    results = c.fetchall()
    conn.close()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Quantity: {row[3]}")
    else:
        print("No books found.")

# Step 3: Create a menu for the user to interact with the program
def main_menu():
    while True:
        print("\n1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Ensure database is created and populated when the script is run
if __name__ == "__main__":
    create_database()
    populate_database()
    main_menu()  
