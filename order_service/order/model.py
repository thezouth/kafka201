from typing import NamedTuple, List, Optional
from datetime import datetime

class OrderItem(NamedTuple):
    product_id: int
    amount: int
    price_per_unit: float

    item_id: Optional[int] = None


class Order(NamedTuple):
    customer_id: int
    customer_name: str
    is_member: bool
    
    items: List[OrderItem]

    order_id: Optional[int] = None
    date: datetime = datetime.now()
