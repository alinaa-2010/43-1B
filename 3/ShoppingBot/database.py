
import sqlite3

db = sqlite3.connect("shopping.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT,
    quantity INTEGER
)
""")

db.commit()


def add_user(user_id):
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
        (user_id,)
    )
    db.commit()


def add_product(user_id, name, quantity):
    cursor.execute(
        "INSERT INTO products (user_id, name, quantity) VALUES (?, ?, ?)",
        (user_id, name, quantity)
    )
    db.commit()


def get_products(user_id):
    cursor.execute(
        "SELECT * FROM products WHERE user_id = ?",
        (user_id,)
    )
    return cursor.fetchall()


def delete_product(product_id, user_id):
    cursor.execute(
        "DELETE FROM products WHERE id = ? AND user_id = ?",
        (product_id, user_id)
    )
    db.commit()
