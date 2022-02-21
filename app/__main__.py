from aiohttp import web

from app import create_app

HTTP_HOST = "127.0.0.1"
HTTP_PORT = 8888


if __name__ == '__main__':
    web.run_app(create_app(), host=HTTP_HOST, port=HTTP_PORT)



