import asyncio
from typing import List, Dict, Any
import time
from concurrent.futures import ThreadPoolExecutor

from aiohttp import web
from pymongo import MongoClient
import pymongo as pmg


async def show_all_db_in_mongo_server(req: web.Request) -> web.Response:
    def heavy_db_call(_client: MongoClient) -> List[Dict[Any, Any]]:
        _res = list(client.list_databases())
        time.sleep(5)
        return _res

    st = time.monotonic()
    client: MongoClient = req.app["client"]
    th_pool: ThreadPoolExecutor = req.app["th_pool"]

    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(th_pool, heavy_db_call, client)
    print(res)

    end = time.monotonic()

    return web.json_response({"start": st, "end": end, "duration":  end - st})
