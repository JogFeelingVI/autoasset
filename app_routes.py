# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:15:24
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-01-13 15:13:23
from aiohttp import web
from app_view import index, test
from app_setting import BASE_DIR


def setup_routes(app: web.Application):
    app.router.add_get('/', index)
    app.router.add_get('/test', test)
    
def setup_static_routes(app:web.Application):
    app.router.add_static('/static/', path=BASE_DIR / 'static', name='static')
