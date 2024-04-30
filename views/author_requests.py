import json
import sqlite3
from models import Author, Book

def get_authors():
    with sqlite3.connect("./simply.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.email,
            a.first_name,
            a.last_name,
            a.image,
            a.favorite
          FROM author a
          """)

        authors = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            author = Author(row['id'], row['email'], row['first_name'], row['last_name'], row['image'], row['favorite'])

            # fetch books associated with author
            db_cursor.execute("""
            SELECT
                b.id,
                b.title,
                b.image,
                b.price,
                b.sale,
                b.description
            FROM book b
            JOIN author_books ab ON b.id = ab.book_id
            WHERE ab.author_id = ?
            """, (author.id,))

            books_data = db_cursor.fetchall()
            books = [dict(data) for data in books_data]

            author.books = books
            authors.append(author.__dict__)

    return authors

def get_single_author(id):
    with sqlite3.connect("./simply.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    db_cursor.execute("""
        SELECT
            a.id,
            a.email,
            a.first_name,
            a.last_name,
            a.image,
            a.favorite
          FROM author a
          WHERE a.id = ?
          """, ( id, ))

    data = db_cursor.fetchone()

    author = Author(data['id'], data['email'], data['first_name'], data['last_name'], data['image'], data['favorite'])

    #fetch books for single author
    db_cursor.execute("""
    SELECT
        b.id,
        b.title,
        b.image,
        b.price,
        b.sale,
        b.description
    FROM book b
    JOIN author_books ab ON b.id = ab.book_id
    WHERE ab.author_id = ?
    """, (id, ))

    books_data = db_cursor.fetchall()
    books = [dict(data) for data in books_data]

    author.books = books

    return author.__dict__
