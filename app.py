# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2024-01-06 21:09:15
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-01-23 20:43:26
from aiohttp import web
from app_routes import setup_routes, setup_static_routes
from app_midd import setup_middleware
from app_setting import BASE_DIR
import aiohttp_jinja2, jinja2

app = web.Application()
print(f'BASE_DIR {BASE_DIR}')

aiohttp_jinja2.setup(app=app,
                     loader=jinja2.FileSystemLoader(str(BASE_DIR /
                                                        'templates')))
setup_static_routes(app=app)
setup_routes(app=app)
setup_middleware(app=app)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
