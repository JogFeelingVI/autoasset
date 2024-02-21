# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:03:10
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-02-21 19:15:42
from codex import filters_v3, gethtml, postcall
from aiohttp import web
from app_setting import BASE_DIR
import aiohttp_jinja2, json, random, inspect


@aiohttp_jinja2.template('index.html')
async def index(request):
    lock_json = BASE_DIR / 'luck.json'
    with lock_json.open(mode='r', encoding='utf-8') as L:
        jsond = json.loads(L.read())
    return {'luck':jsond[f'{random.randint(1,6)}']}


async def favicon(request):
    # Content-Type: image/vnd.microsoft.icon
    headers = {'Content-Type': 'mage/vnd.microsoft.icon'}
    return web.FileResponse(BASE_DIR / 'static' / 'favicon.ico')


async def handle(request):
    response_obj = {'time': '---', 'status': 'done'}
    try:
        DataFrame = BASE_DIR / 'DataFrame.json'
        if DataFrame.exists() == False:
            response_obj.update({'message': 'DataFrame exists is Not'})
        url = 'https://www.cjcp.cn/zoushitu/cjwssq/hqaczhi.html'
        data_fr = gethtml.toDict(gethtml.get_html(url).neirong)
        response_obj.update({'time': data_fr.get('date', '')})
        json_str = json.dumps(data_fr)
        with open(DataFrame, 'w') as datajson:
            datajson.write(json_str)
            hszie = json_str.__sizeof__()
            response_obj.update(
                {'message': f'The data has been updated, sized {hszie}kb/s'})
    except:
        response_obj.update({'message': 'Network connection failed'})
    finally:
        print(f'handle GET {response_obj}')
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps(response_obj),
                            headers=headers,
                            status=200)


async def handle_post(request):
    '''js done onclick'''
    try:
        request_data = await request.json()
        p = postcall.postcallforjson()
        p.instal_json(request_data)
        rejs = p.toJson()
    except:
        rejs = {'1': ['error', 'ER']}
    finally:
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps(rejs), headers=headers, status=200)


async def handle_get_filter_name(request):
    filters = []
    response_obj = {'list': [], 'checked': [], 'status': 'done'}
    try:
        fter = filters_v3
        fter.initialization()
        class_attrs, checked = fter.classAttrs()
        response_obj.update({'checked': checked})
        response_obj.update({'list': class_attrs})
    except:
        response_obj.update({'status': 'Error'})
    finally:
        print(f'handle GET filter_v2 name {filters.__len__()}')
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps(response_obj),
                            headers=headers,
                            status=200)


async def handle_save_insx_rego(request):
    insx_rego = BASE_DIR / 'insx.rego'
    response_obj = {'message': '', 'path': insx_rego}
    try:
        with insx_rego.open(mode='w', encoding='utf-8') as L:
            request_data = await request.json()
            L.write(request_data['insxd'])
            print(f'insxd {insx_rego}')
            response_obj.update({'message': 'insxd File writing completed.'})
    except:
        print(f'insxd File write failed.')
        response_obj.update({'message': 'insxd File write failed.'})
    finally:
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps({'msg': 'test'}),
                            headers=headers,
                            status=200)


async def handle_read_insx_rego(request):
    insx_rego = BASE_DIR / 'insx.rego'
    response_obj = {'insxd': ''}
    try:
        with insx_rego.open(mode='r', encoding='utf-8') as L:
            insxd = L.read()
            response_obj.update({'insxd': insxd})
    except:
        response_obj = {'insxd': 'insx_rego loading failed'}
        print(f'{response_obj["insxd"]}')
    finally:
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps(response_obj),
                            headers=headers,
                            status=200)
