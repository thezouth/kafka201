import asyncio
from typing import Dict

from sanic import Sanic, response
from sanic.request import Request

from . import persistence
from .proxy import warehouse, member
from .model import Order, OrderItem, serialize_order

app = Sanic()

@app.post('order')
async def create_order(request: Request):
    #Deserialize message
    req_order = build_order(request.json)
    #Execute main flow
    res_order = persistence.create_order(req_order)
    
    #Execute side orders
    await asyncio.gather(
        warehouse.send_order(res_order),
        notify_customer(res_order),
        maybe_promote_member(res_order),
    )
    
    #Response
    return response.json(serialize_order(res_order))


def build_order(json: Dict) -> Order:
    items = [OrderItem(**item) for item in json['items']]
    del json['items']
    return Order(items=items, **json)


GOLD_MEMBER_SALES = 1_000
async def maybe_promote_member(order: Order):
    if not order.is_member:
        return

    current_sales = sum((item.amount * item.price_per_unit for item in order.items))
    acc_sales = persistence.accumulate_sales(order.customer_id)
    if acc_sales >= GOLD_MEMBER_SALES and (acc_sales - current_sales) < GOLD_MEMBER_SALES:
        print('promote member', order.customer_id)
        await member.promote(order.customer_id, 'GOLD')

async def notify_customer(order: Order):
    if not order.is_member:
        return

    message = f'We received your order, Please find at http://me.thezouth.com/order/{order.order_id}'
    await member.notify(order.customer_id, message)


@app.listener('after_server_start')
async def start_proxy_session(app, loop):
    await asyncio.gather(
        warehouse.start(loop),
        member.start(loop)
    )
    

@app.listener('after_server_stop')
async def stop_proxy_session(app, loop):
    await asyncio.gather(
        warehouse.stop(),
        member.stop()
    )


if __name__ == '__main__':
    app.run()
