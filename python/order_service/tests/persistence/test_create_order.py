import unittest

import sqlite3
from typing import Tuple
from datetime import datetime

from order_service.order.persistence import create_order
from order_service.order import db
from order_service.order.model import Order, OrderItem

class TestPersistence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(':memory:')
        db.init_db(cls.conn)
    
    def test_create_order(self):
        order = Order(
            customer_id=2,
            customer_name='Tansinee T.',
            is_member=True,
            items=[
                OrderItem(product_id=3, amount=15, price_per_unit=10.0),
                OrderItem(product_id=4, amount=13, price_per_unit=5.0)
            ]
        )

        new_order = create_order(order, self.conn)
        order_id = new_order.order_id

        actual_order, actual_items = self._load_order(order_id)
        self.assert_order(order, actual_order)
        assert len(order.items) == len(actual_items)
        for order_item, acutal_item in zip(order.items, actual_items):
            self.assert_order_item(order_item, acutal_item)

    def _load_order(self, order_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT customer_id, customer_name, is_member, date FROM orders WHERE id = ?', 
            (order_id,))
        order = cursor.fetchone()

        cursor.execute('SELECT product_id, amount, price_per_unit FROM order_items WHERE order_id = ?', 
            (order_id,))
        order_items = cursor.fetchall()

        return order, order_items

    def assert_order(self, expected: Order, db_actual: Tuple):
        assert db_actual[0] == expected.customer_id
        assert db_actual[1] == expected.customer_name
        assert db_actual[2] == expected.is_member
        assert datetime.strptime(db_actual[3], '%Y-%m-%d %H:%M:%S.%f') == expected.date
    
    def assert_order_item(self, expected: OrderItem, db_actual: Tuple):
        assert db_actual[0] == expected.product_id
        assert db_actual[1] == expected.amount
        assert db_actual[2] == expected.price_per_unit

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
