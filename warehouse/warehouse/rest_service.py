from sanic import Sanic, response
from sanic.request import Request
import logging

from .stock_manager import receive_order

app = Sanic()

@app.post('/delivery-order')
async def create_delivery_order(request: Request):
    receive_order(request.json)
    return response.json('ok')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run()
