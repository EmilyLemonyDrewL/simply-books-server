import json
import sqlite3
from models import Author

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

    return author.__dict__


# def create_author

# def update_author

# def delete_author
