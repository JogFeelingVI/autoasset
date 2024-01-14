# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-13 15:15:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-01-13 15:23:03
import aiohttp_jinja2
from aiohttp import web
from app_setting import BASE_DIR


async def handle_404(request):
    return aiohttp_jinja2.render_template('404.html', request, {}, status=404)

async def handle_505(request):
    return aiohttp_jinja2.render_template('505.html', request, {}, status=505)

def create_error_middleware(overrides):
    
    @web.middleware
    async def error_middleware(request, handler):
        try:
            return await handler(request)
        except web.HTTPException as ex:
            override = overrides.get(ex.status)
            if override:
                return await override(request)

            raise
        except Exception:
            request.protocol.logger.exception("Error handling request")
            return await overrides[500](request)

    return error_middleware

def setup_middleware(app:web.Application):
    error_middleware = create_error_middleware({
        404: handle_404,
        505:handle_505
    })
    app.middlewares.append(error_middleware)