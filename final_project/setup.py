from bottle import Bottle, template, request, redirect, route, run
import sqlite3

# Connect to the database
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

# Create the 'books' table with default values
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_name TEXT DEFAULT 'Unknown Title',
        author TEXT DEFAULT 'Unknown Author'
    )
''')

# Create the 'price' table with a foreign key relationship to 'books' and default values
cursor.execute('''
    CREATE TABLE IF NOT EXISTS price (
        price_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        price INTEGER DEFAULT 0.0,
        FOREIGN KEY (book_id) REFERENCES books (book_id)
    )
''')

# Insert 5 default records into the 'books' table
# Insert default data into the 'books' table
cursor.execute('''
    INSERT INTO books (book_name, author)
    VALUES 
        ('The Catcher in the Rye', 'J.D. Salinger'),
        ('To Kill a Mockingbird', 'Harper Lee'),
        ('1984', 'George Orwell'),
        ('Pride and Prejudice', 'Jane Austen')
''')
# Insert default data into the 'price' table
cursor.execute('''
    INSERT INTO price (book_id, price)
    VALUES 
       (1, 199),
        (2, 114),
        (3, 124),
        (4, 129) 
''')

# Commit the changes to the database
conn.commit()

# Define your Bottle app
app = Bottle()

#