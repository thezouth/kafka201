import aiohttp
import json


SERVICE_HOST = 'http://localhost:8002/'
SESSION = None


async def start(loop=None):
    global SESSION
    SESSION = aiohttp.ClientSession(loop=loop)


async def stop():
    await SESSION.close()


async def promote(member_id, privilege):
    async with SESSION.post(f'{SERVICE_HOST}member/{member_id}/promote', 
            json={'privilege': privilege}) as resp:
        resp.raise_for_status()
