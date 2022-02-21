import asyncio
import aiohttp


async def req(session: aiohttp.ClientSession, url="http://localhost:8888/"):
    async with session.get(url) as resp:
        r = await resp.json()
        return r


async def main():
    async with aiohttp.ClientSession() as session:
        url_show_dbs = "http://localhost:8888/show_all_db_in_mongo_server"
        res = await asyncio.gather(*[req(session, url_show_dbs) for _ in range(25)])

    return res


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for i in loop.run_until_complete(main()):
        print(i)
