import sqlite3
from datetime import date
import sys

if __name__ == '__main__':
    src_conn = sqlite3.connect('order.db')
    dst_conn = sqlite3.connect('../bi/order-bi.db')

    import_date = sys.argv[1] if len(sys.argv) >= 2 else date.today().strftime('%Y-%m-%d')
    print('Transfering data of ' + import_date)
    
    cursor = src_conn.cursor()
    cursor.execute('''
        SELECT orders.id as order_id, order_items.id as item_id,
               customer_id, is_member, 
               strftime('%Y-%m-%d', date) as date, strftime('%H:%M:%S', date) as time,
               product_id, amount, price_per_unit, 
               amount * price_per_unit as total_price
        FROM orders JOIN order_items ON orders.id = order_items.id
        WHERE strftime('%Y-%m-%d', date) = ?
    ''', (import_date,))

    source_data = list(cursor.fetchall())
    print(f'Fetch data (total: {len(source_data)} records)')

    dst_conn.executemany('''
        INSERT INTO orders (
            order_id, item_id, customer_id, is_member,
            date, time, product_id, amount, price_per_unit, total_price
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', source_data)
    dst_conn.commit()

    print('Successful import data to BI.')
    src_conn.close()
    dst_conn.close()
