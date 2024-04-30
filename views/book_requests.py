import sqlite3
import json
from models import Book

def get_books():
    with sqlite3.connect("./simply.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            b.id,
            b.title,
            b.image,
            b.price,
            b.sale,
            b.description
          FROM book b
          """)

        books = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            book = Book(row['id'], row['title'], row['image'], row['price'], row['sale'], row['description'])

            books.append(book.__dict__)

    return books

def get_single_book(id):
    with sqlite3.connect("./simply.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    db_cursor.execute("""
        SELECT
            b.id,
            b.title,
            b.image,
            b.price,
            b.sale,
            b.description
          FROM book b
          WHERE b.id = ?
          """, ( id, ))

    data = db_cursor.fetchone()

    book = Book(data['id'], data['title'], data['image'], data['price'], data['sale'], data['description'])

    return book.__dict__

# def create_book

# def update_book

# def delete_book
