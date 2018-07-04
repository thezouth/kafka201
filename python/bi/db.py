import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('order-bi.db')
    conn.execute('''
        CREATE TABLE orders (
            order_id INT,
            item_id INT,
            customer_id INT,
            is_member BOOL,
            date DATE,
            time TIME,
            product_id INT,
            amount INT,
            price_per_unit FLOAT,
            total_price FLOAT
        )
    ''')
    conn.close()
