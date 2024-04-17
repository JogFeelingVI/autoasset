# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:15:24
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-04-17 15:23:55
from aiohttp import web
from app_view import index, science, handle, favicon, handle_post, handle_get_filter_name, handle_read_insx_rego, handle_save_insx_rego, handle_ws, handle_get_Detailed_configuration
from app_setting import BASE_DIR


def setup_routes(app: web.Application):
    app.router.add_get('/', handler=index)
    app.router.add_get('/science', handler=science)
    app.router.add_get('/favicon.ico', handler=favicon)
    app.router.add_get('/handle', handler=handle)
    app.router.add_post('/handle_post', handler=handle_post)
    app.router.add_get('/filter_all_name', handler=handle_get_filter_name)
    app.router.add_get('/Detailed_configuration',
                       handler=handle_get_Detailed_configuration)
    app.router.add_get('/load_insx_rego', handler=handle_read_insx_rego)
    app.router.add_post('/save_insx_rego', handler=handle_save_insx_rego)
    app.router.add_post('/ws_handle', handler=handle_ws)


def setup_static_routes(app: web.Application):
    app.router.add_static('/static/', path=BASE_DIR / 'static', name='static')
