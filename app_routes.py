# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:15:24
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-01-26 23:51:06
from aiohttp import web
from app_view import index, handle, favicon, handle_post, handle_get_filter_name
from app_setting import BASE_DIR


def setup_routes(app: web.Application):
    app.router.add_get('/', handler=index)
    app.router.add_get('/favicon.ico', handler=favicon)
    app.router.add_get('/handle', handler=handle)
    app.router.add_post('/handle_post', handler=handle_post)
    app.router.add_get('/filter_all_name', handler=handle_get_filter_name)
    
    
def setup_static_routes(app:web.Application):
    app.router.add_static('/static/', path=BASE_DIR / 'static', name='static')
