from sanic import Sanic, response
from sanic.request import Request
from typing import Dict

from . import persistence
from .model import Order, OrderItem, serialize_order

app = Sanic()

@app.post('order')
def create_order(request: Request):
    #Deserialize message
    req_order = build_order(request.json)
    #Execute main flow
    res_order = persistence.create_order(req_order)
    
    #Response
    return response.json(serialize_order(res_order))

def build_order(json: Dict) -> Order:
    items = [OrderItem(**item) for item in json['items']]
    del json['items']
    return Order(items=items, **json)

if __name__ == '__main__':
    app.run()
