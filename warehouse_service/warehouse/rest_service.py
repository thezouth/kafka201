from sanic import Sanic, response
from sanic.request import Request
import logging

from . import stock_manager

app = Sanic()

@app.post('/delivery-order')
async def create_delivery_order(request: Request):
    stock_manager.receive_order(request.json)
    return response.json('ok')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(port=8001)
