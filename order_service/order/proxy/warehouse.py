import aiohttp
import logging

from ..model import Order, OrderItem, serialize_order


SERVICE_HOST = 'http://localhost:8001/'
SESSION = None

logger = logging.getLogger(__name__)

async def start(loop=None):
    global SESSION
    SESSION = aiohttp.ClientSession(loop=loop)

async def stop():
    await SESSION.close()

async def send_order(order: Order):
    async with SESSION.post(SERVICE_HOST + 'delivery-order', 
            json=serialize_order(order)) as resp:
        resp.raise_for_status()
        logger.info(f'Successful! Send order %{order.order_id} to warehouse.')
