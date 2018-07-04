import sqlite3

conn = sqlite3.connect('order.db')

def init_db(conn: sqlite3.Connection = conn):
    conn.execute('''
        CREATE TABLE orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATETIME, 
            customer_id INTEGER, 
            customer_name TEXT,
            is_member BOOLEAN
        )
    ''')

    conn.execute('''
        CREATE TABLE order_items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_id INTEGER,
            amount INTEGER,
            price_per_unit REAL
        )
    ''')

if __name__ == '__main__':
    init_db()
