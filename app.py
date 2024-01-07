# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2024-01-06 21:09:15
# @Last Modified by:   Your name
# @Last Modified time: 2024-01-06 21:22:58
import aiohttp, base64
import aiohttp_session_fernet
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

app = aiohttp.web.Application()
aiohttp_session_fernet.setup(app, EncryptedCookieStorage(b'secret'))

@app.route('/')
async def index(request):
    return aiohttp.web.FileResponse('index.html')

@app.route('/draggable.js')
async def draggable_js(request):
    return aiohttp.web.FileResponse('draggable.js')

if __name__ == '__main__':
    aiohttp.web.run_app(app)
