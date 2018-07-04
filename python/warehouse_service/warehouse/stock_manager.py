import logging

from .stock_warehouse import STOCK_WAREHOUSE
from .stock import StockItem

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

DELIVERY_ORDERS = []
PENDING_ORDERS = []

def receive_order(order):
    if _check_remainning_stock(order):
        create_delivery_order(order)
    else:
        pending_order(order)

def create_delivery_order(order):
    for item in order['items']:
        _deduct_stock(item)

    logger.info("\033[94mCreate delivery order: %s\033[0m", order['order_id'])
    DELIVERY_ORDERS.append(order)

def pending_order(order):
    logger.info("\033[91mPending order: %s\033[0m", order['order_id'])
    PENDING_ORDERS.append(order)

def _check_remainning_stock(order) -> bool:
    return all((
        item['amount'] <= STOCK_WAREHOUSE[item['product_id']].remaining_stock
        for item in order['items']
    ))

def _deduct_stock(order_item):
    product_id = order_item['product_id']
    request_amount = order_item['amount']
    curr_stock = STOCK_WAREHOUSE[product_id]
    
    new_remaining_stock = curr_stock.remaining_stock - request_amount

    STOCK_WAREHOUSE[product_id] = \
        curr_stock._replace(remaining_stock=new_remaining_stock)
