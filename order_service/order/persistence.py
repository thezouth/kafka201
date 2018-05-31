from sqlite3 import Connection, Cursor

from .db import conn
from .model import Order, OrderItem


def create_order(order: Order, conn: Connection = conn):
    cursor = conn.cursor()

    order_id = _create_order(order, cursor)
    for item in order.items:
        _create_item(item, order_id, cursor)
    
    conn.commit()
    return order_id
    

def _create_order(order: Order, cursor: Cursor) -> int:
    cursor.execute(
        '''INSERT INTO orders(date, customer_id, customer_name, is_member)
           VALUES (?, ?, ?, ?)''',
        (order.date, order.customer_id, order.customer_name, order.is_member)
    )

    return cursor.lastrowid

def _create_item(item: OrderItem, order_id: int, cursor: Cursor) -> int:
    cursor.execute(
        '''INSERT INTO order_items(order_id, product_id, amount, price_per_unit)
           VALUES (?, ?, ?, ?)''',
        (order_id, item.product_id, item.amount, item.price_per_unit)
    )

    return cursor.lastrowid
