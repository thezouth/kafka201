from sqlite3 import Connection, Cursor

from .db import conn
from .model import Order, OrderItem


def create_order(order: Order, conn: Connection = conn) -> Order:
    cursor = conn.cursor()

    new_order = _create_order(order, cursor)
    new_order.items = [
        _create_item(item, new_order.order_id, cursor)
        for item in order.items
    ]

    conn.commit()
    return new_order
    

def _create_order(order: Order, cursor: Cursor) -> Order:
    cursor.execute(
        '''INSERT INTO orders(date, customer_id, customer_name, is_member)
           VALUES (?, ?, ?, ?)''',
        (order.date, order.customer_id, order.customer_name, order.is_member)
    )

    return Order(
        order_id=cursor.lastrowid, 
        date=order.date,
        customer_id=order.customer_id, 
        customer_name=order.customer_name, 
        is_member=order.is_member
    )

def _create_item(item: OrderItem, order_id: int, cursor: Cursor) -> OrderItem:
    cursor.execute(
        '''INSERT INTO order_items(order_id, product_id, amount, price_per_unit)
           VALUES (?, ?, ?, ?)''',
        (order_id, item.product_id, item.amount, item.price_per_unit)
    )

    return OrderItem(
        item_id=cursor.lastrowid,
        product_id=item.product_id,
        amount=item.amount,
        price_per_unit=item.price_per_unit
    )
