# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:03:10
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-01-26 15:26:15
from codex import glns_v2, datav, note
from aiohttp import web
from app_setting import BASE_DIR
import aiohttp_jinja2, time, json, random



@aiohttp_jinja2.template('index.html')
async def index(request):
    cdic = datav.LoadJson().toLix
    glns = glns_v2.glnsMpls(cdic, 6, 1, 'c')
    navigation = []
    while len(navigation) <= 25:
        _n = glns.producer['r']()
        _t = glns.producer['b']()
        n = note.Note(_n, _t)
        navigation.append(n)
    return {'navigation': navigation}

async def favicon(request):
    # Content-Type: image/vnd.microsoft.icon
    headers = {'Content-Type': 'mage/vnd.microsoft.icon'}
    return web.FileResponse(BASE_DIR / 'static' / 'favicon.ico')

async def handle(request):
    response_obj = {'time': time.time(), 'status': 'done'}
    print(f'handle GET {response_obj}')
    headers = {'Content-Type': 'application/json'}
    return web.Response(text=json.dumps(response_obj), headers=headers, status=200)

async def handle_post(request):
    request_data = await request.json()
    request_data = dict(request_data)
    request_data.update({'lens':random.randint(1,1000)})
    request_data.update({'update':'JogFeelingVI'})
    print(f'handle POST {request_data} {type(request_data)}')
    headers = {'Content-Type': 'application/json'}
    return web.Response(text=json.dumps(request_data), headers=headers, status=200)