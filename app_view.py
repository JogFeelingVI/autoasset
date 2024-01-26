# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:03:10
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-01-26 23:50:07
from codex import glns_v2, datav, note
from aiohttp import web
from app_setting import BASE_DIR
from codex import gethtml, glns_v2
import aiohttp_jinja2, json, random


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
    response_obj = {'time': '---', 'status': 'done'}
    try:
        DataFrame = BASE_DIR / 'DataFrame.json'
        if DataFrame.exists() == False:
            response_obj.update({'message':'DataFrame exists is Not'})
        url= 'https://www.cjcp.cn/zoushitu/cjwssq/hqaczhi.html'
        data_fr = gethtml.toDict(gethtml.get_html(url).neirong)
        response_obj.update({'time': data_fr.get('date', '')})
        json_str = json.dumps(data_fr)
        with open(DataFrame, 'w') as datajson:
            datajson.write(json_str)
            hszie = json_str.__sizeof__()
            response_obj.update({'message':f'The data has been updated, sized {hszie}'})
    except:
        response_obj.update({'message':'Network connection failed'})
    finally:
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

async def handle_get_filter_name(request):
    response_obj = {'list': [], 'status': 'done'}
    filters = glns_v2.filterN_v2.getfilter()
    response_obj.update({'list':filters})
    print(f'handle GET filter_v2 name {filters}')
    headers = {'Content-Type': 'application/json'}
    return web.Response(text=json.dumps(response_obj), headers=headers, status=200)