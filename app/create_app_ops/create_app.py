import asyncio
from typing import List, Dict, Any
import time

from aiohttp import web
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor
import pymongo as pmg

from ..handlers import show_all_db_in_mongo_server

TH_POOL_SIZE = 5
MG_POOL_SIZE = 2

MG_HOST = "127.0.0.1"
MG_PORT = 27018


async def on_start(app: web.Application) -> None:
    client = MongoClient(host=MG_HOST, port=MG_PORT, maxPoolSize=2)
    app["client"]: MongoClient = client
    pool = ThreadPoolExecutor(max_workers=TH_POOL_SIZE)
    app["th_pool"] = pool
    return


async def on_shutdown(app: web.Application) -> None:
    client: MongoClient = app["client"]
    pool: ThreadPoolExecutor = app["th_pool"]
    pool.shutdown(wait=True)
    client.close()
    return


async def create_app() -> web.Application:
    app = web.Application()

    app.router.add_get("/show_all_db_in_mongo_server", show_all_db_in_mongo_server)

    app.on_startup.append(on_start)
    app.on_shutdown.append(on_shutdown)

    return app
