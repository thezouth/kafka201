from sanic import Sanic, response
from sanic.request import Request
from typing import Dict

from . import persistence
from .model import Order, OrderItem

app = Sanic()

@app.post('order')
def create_order(request: Request):
    order = build_order(request.json)
    order_id = persistence.create_order(order)
    return response.json({ "order_id": order_id })

def build_order(json: Dict) -> Order:
    items = [OrderItem(**item) for item in json['items']]
    del json['items']
    return Order(items=items, **json)

if __name__ == '__main__':
    app.run()
