# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:15:24
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-01-13 08:32:31
from aiohttp import web
from app_view import index, test


def setup_routes(app: web.Application):
    app.router.add_get('/', index)
    app.router.add_get('/test', test)
