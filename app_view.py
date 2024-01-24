# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:03:10
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-01-23 20:43:57
from codex import glns_v2, datav, note
from aiohttp import web
import aiohttp_jinja2, time


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

async def test(request):
    return web.Response(text=f'T{time.time()}')
