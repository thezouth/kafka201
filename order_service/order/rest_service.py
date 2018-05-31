from sanic import Sanic, response
from sanic.request import Request
from typing import Dict

from . import persistence
from .proxy import warehouse
from .model import Order, OrderItem, serialize_order

app = Sanic()

@app.post('order')
async def create_order(request: Request):
    #Deserialize message
    req_order = build_order(request.json)
    #Execute main flow
    res_order = persistence.create_order(req_order)
    
    #Execute side orders
    await warehouse.send_order(res_order)

    #Response
    return response.json(serialize_order(res_order))

def build_order(json: Dict) -> Order:
    items = [OrderItem(**item) for item in json['items']]
    del json['items']
    return Order(items=items, **json)

@app.listener('after_server_start')
async def start_proxy_session(app, loop):
    await warehouse.start(loop)

@app.listener('after_server_stop')
async def stop_proxy_session(app, loop):
    await warehouse.stop()


if __name__ == '__main__':
    app.run()
