from typing import List, Optional
from datetime import datetime

import attr

@attr.s
class OrderItem(object):
    product_id = attr.ib(type=int)
    amount = attr.ib(type=int)
    price_per_unit = attr.ib(type=int)

    item_id = attr.ib(type=int, default=None)


@attr.s
class Order(object):
    customer_id = attr.ib(type=int)
    customer_name = attr.ib(type=int)
    is_member = attr.ib(type=bool, default=False)
    
    items = attr.ib(type=List[OrderItem], default=[])

    order_id = attr.ib(type=Optional[int], default=None)
    date = attr.ib(type=datetime, default=attr.Factory(datetime.now))


def serialize_order(order: Order):
    return {
        'order_id': order.order_id,
        'date': order.date.isoformat(),
        'customer_id': order.customer_id,
        'customer_name': order.customer_name,
        'is_member': order.is_member,
        'items': [_serialize_item(item) for item in order.items]
    }

def _serialize_item(item: OrderItem):
    return {
        'item_id': item.item_id,
        'product_id': item.product_id,
        'amount': item.amount,
        'price_per_unit': item.price_per_unit
    }