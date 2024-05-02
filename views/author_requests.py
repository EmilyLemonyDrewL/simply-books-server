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

def create_author(new_author):
    print("new_author type:", type(new_author))
    print("new_author content:", new_author)

    if isinstance(new_author, bytes):
        new_author = json.loads(new_author)

    with sqlite3.connect("./simply.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Author
            ( email, first_name, last_name, image, favorite )
        VALUES
            ( ?, ?, ?, ?, ?);
        """,  (new_author['email'], new_author['first_name'], new_author['last_name'], new_author['image'], new_author['favorite'], ))

        id = db_cursor.lastrowid
        new_author['id'] = id

    return new_author

def update_author(id, new_author):
    with sqlite3.connect("./simply.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Author
            SET
                email = ?
                first_name = ?
                last_name = ?
                image = ?
                favorite = ?
        WHERE id = ?
        """, (new_author['email'], new_author['first_name'], new_author['last_name'], new_author['image'], new_author['favorite'], id, ))

        row_affected = db_cursor.rowcount

    if row_affected == 0:
        return False
    else:
        return

def delete_author(id):
    with sqlite3.connect("./simply.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM author
        WHERE id = ?
        """, (id, ))
