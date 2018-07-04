import unittest

from datetime import datetime
import itertools
import sqlite3
from typing import Tuple

from order_service.order.persistence import accumulate_sales, create_order
from order_service.order import db
from order_service.order.model import Order, OrderItem

class TestPersistence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = sqlite3.connect(':memory:')
        db.init_db(cls.conn)
        cls.mock_data()

    def test_accumulate_sales_of_multiple_order(self):
        actual_acc = accumulate_sales(customer_id=1, year=2018, conn=self.conn)
        
        relevant_items = itertools.chain(*(
            order.items 
            for order in self.orders 
            if order.date.year == 2018 and order.customer_id == 1
        ))

        expected_acc = sum((item.price_per_unit * item.amount for item in relevant_items))

        assert actual_acc == expected_acc

    @classmethod
    def mock_data(cls):
        cls.orders = [
            Order(customer_id=1, customer_name='a', is_member=True, date=datetime(2018, 1, 1), 
                items=[OrderItem(product_id=1, amount=2, price_per_unit=5.0), OrderItem(product_id=2, amount=4, price_per_unit=10.0)]),
            Order(customer_id=2, customer_name='b', is_member=True, date=datetime(2018, 1, 1), 
                items=[OrderItem(product_id=1, amount=2, price_per_unit=5.0)]),
            Order(customer_id=1, customer_name='a', is_member=True, date=datetime(2018, 2, 2),
                items=[OrderItem(product_id=1, amount=3, price_per_unit=15.0)]),
            Order(customer_id=1, customer_name='a', is_member=True, date=datetime(2017, 1, 1),
                items=[OrderItem(product_id=1, amount=2, price_per_unit=5.0)]),
        ]

        for order in cls.orders:
            create_order(order, conn=cls.conn)

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
