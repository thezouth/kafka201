from typing import NamedTuple

class StockItem(NamedTuple):
    product_id: int
    product_name: str
    remaining_stock: int
