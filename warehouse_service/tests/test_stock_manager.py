import unittest

from ..warehouse.stock_manager import receive_order, DELIVERY_ORDERS, PENDING_ORDERS
from ..warehouse.stock_warehouse import STOCK_WAREHOUSE

class TestStockManager(unittest.TestCase):
    def test_order_less_than_stock(self):
        order = {
            'id': 1,
            'customer': { 'id': 1 },
            'items': [
                {
                    'product_id': 1,
                    'amount': STOCK_WAREHOUSE[1].remaining_stock - 5
                },
                {
                    'product_id': 2,
                    'amount': STOCK_WAREHOUSE[2].remaining_stock - 3
                }
            ]
        }

        receive_order(order)
        delivery_order = DELIVERY_ORDERS[0]
        assert order['id'] == delivery_order['id']
        assert order['customer'] == delivery_order['customer']
        for order_item, delivery_item in zip(order['items'], delivery_order['items']):
            assert order_item == delivery_item
        
        assert STOCK_WAREHOUSE[1].remaining_stock == 5
        assert STOCK_WAREHOUSE[2].remaining_stock == 3

    def test_order_more_than_stock(self):
        order = {
            'id': 2,
            'customer': { 'id': 1 },
            'items': [
                {
                    'product_id': 1,
                    'amount': STOCK_WAREHOUSE[1].remaining_stock - 5
                },
                {
                    'product_id': 2,
                    'amount': STOCK_WAREHOUSE[2].remaining_stock + 3
                }
            ]
        }

        item1_before_order = STOCK_WAREHOUSE[1].remaining_stock
        item2_before_order = STOCK_WAREHOUSE[2].remaining_stock

        receive_order(order)
        pending_order = PENDING_ORDERS[0]
        assert order == pending_order
        
        assert STOCK_WAREHOUSE[1].remaining_stock == item1_before_order
        assert STOCK_WAREHOUSE[2].remaining_stock == item2_before_order
