from bottle import Bottle, template, request, redirect,route,run,post
import sqlite3



conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

@route('/')
def home():
    return template('home')

@route('/books')
def books():
    cursor.execute("SELECT books.book_id, books.book_name, books.author, price.price FROM books JOIN price ON books.book_id = price.book_id")
    books = cursor.fetchall()
    return template('books', books=books)

@route('/price')
def price():
    cursor.execute("SELECT * FROM price")
    price = cursor.fetchall()
    return template('price', price=price)

# @route('/add_book', method='GET')
# def add_book_form():
#     cursor.execute("SELECT * FROM price")
#     price = cursor.fetchall()
#     return template('add_book', price=price)

# @route('/add_player', method='POST')
# def add_player():
#     player_name = request.forms.get('player_name')
#     position = request.forms.get('position')
#     team_id = request.forms.get('team_id')

#     cursor.execute("INSERT INTO players (name, position, team_id) VALUES (?, ?, ?)", (player_name, position, team_id))
#     conn.commit()

#     redirect('/players')
@route('/update_book/<book_id>', method='GET')
def update_book_form(book_id):
    cursor.execute("SELECT * FROM books WHERE book_id=?", (book_id,))
    book = cursor.fetchone()
    return template('update_book',books=book)

@route('/update_book/<book_id>', method='POST')
def update_book(book_id):
    book = request.forms.get('book_name')
    author = request.forms.get('author')
    cursor.execute("UPDATE books SET book_name=?, author=? WHERE book_id=?", (book,author,book_id)) 
    conn.commit()

    redirect('/books')

@route('/delete_book/<book_id>')
def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE book_id=?", (book_id,))
    conn.commit()

    redirect('/books')

@route('/search_books')
def search_books_form():
    return template('search_books', players=None, search_query=None)

@route('/search_books', method='get')
def search_books():
    search_query = request.query.get('search', '').strip()

    if search_query:
        # If there's a search query, filter players based on the name
        cursor.execute("SELECT books.book_name, books.author, price.price FROM books JOIN price ON books.book_id = price.book_id WHERE books.book_name LIKE ?", ('%' + search_query + '%',))
        books = cursor.fetchall()
    else:
        # If no search query, set players to None
        books = None

    return template('search_books', books=books, search_query=search_query)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
