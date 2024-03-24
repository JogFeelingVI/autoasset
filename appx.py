# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-03-23 22:16:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-03-23 22:40:00

from aiohttp import web
import asyncio
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


def blocking_code():
    """Some long running code"""
    time.sleep(12)
    return "!!!!"


async def blocking_code_task(loop: asyncio.BaseEventLoop, request: web.Request):
    """Wrapper to be used in asyncio Task"""
    r = await loop.run_in_executor(executor=request.app["workers_pool"], func=blocking_code)
    logging.info(f"{datetime.now()}: {r}")


async def handle(request: web.Request):
    name = request.match_info.get('name', "Anonymous")
    text = f'name {name = } Quick.'
    return web.Response(text=text)


async def sleephandle(request: web.Request):
    """We wait fore results here, then send response"""
    name = request.match_info.get('name', "Anonymous")
    loop = asyncio.get_event_loop()
    # if you want to wait for result
    r = await loop.run_in_executor(executor=request.app["workers_pool"], func=blocking_code)
    text = f'Hello {name =} {r=} sleep.'
    return web.Response(text=text)


async def fast_sleep_answer(request: web.Request):
    """We send response as fast as possible and do all work in another asyncio Task"""
    name = request.match_info.get('name', "Anonymous")
    loop = asyncio.get_event_loop()
    text = f'Fast answer {name = } {loop.time()}'
    # if you do not want to want for result
    asyncio.create_task(blocking_code_task(loop, request))
    return web.Response(text=text)


async def on_shutdown(app):
    """Do not forget to correctly close ThreadPool"""
    app["workers_pool"].shutdown()
    logging.info(f"{datetime.now()}: Pool is closed")


async def init(args=None):
    """Changed your code for newer aiohttp"""
    pool = ThreadPoolExecutor(8)
    app = web.Application()
    app.router.add_get('/quick', handle)
    app.router.add_get('/sleep', sleephandle)
    app.router.add_get('/fast', fast_sleep_answer)
    app["workers_pool"] = pool  # can be ThreadPool or ProcessPool
    app.on_shutdown.append(on_shutdown)  # close the pool when app closes
    return app

# the better way to tun app
# name of file is x.py
# in Linux command will be python3
# python -m aiohttp.web -H 0.0.0.0 -P 8080 x:init
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    web.run_app(init(), host="0.0.0.0", port=8080)