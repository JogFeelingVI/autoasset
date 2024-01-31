# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:03:10
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-01-31 09:33:55
from codex import glns_v2, datav, note, gethtml, postcall
from aiohttp import web
from app_setting import BASE_DIR
import aiohttp_jinja2, json, random, inspect


@aiohttp_jinja2.template('index.html')
async def index(request):
    lock_json = BASE_DIR / 'luck.json'
    with lock_json.open(mode='r', encoding='utf-8') as L:
        jsond = json.loads(L.read())
    return {'luck': jsond[f'{random.randint(1,6)}']}


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
                {'message': f'The data has been updated, sized {hszie}'})
    except:
        response_obj.update({'message': 'Network connection failed'})
    finally:
        print(f'handle GET {response_obj}')
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps(response_obj),
                            headers=headers,
                            status=200)


async def handle_post(request):
    request_data = await request.json()
    print(f'handle POST {request_data} {type(request_data)}')
    p = postcall.postcallforjson()
    p.instal_json(request_data)
    rejs = p.toJson()
    headers = {'Content-Type': 'application/json'}
    return web.Response(text=json.dumps(rejs), headers=headers, status=200)


async def handle_get_filter_name(request):
    response_obj = {'list': [], 'checked': [], 'status': 'done'}
    class_attrs = inspect.classify_class_attrs(glns_v2.filterN_v2)
    checked = glns_v2.filterN_v2.getchecked()
    response_obj.update({'checked': checked})
    filters = []
    for method in class_attrs:
        if method.kind == 'method' and not method.name.startswith('_'):
            filters.append(method.name)
    response_obj.update({'list': filters})
    print(f'handle GET filter_v2 name {filters}')
    headers = {'Content-Type': 'application/json'}
    return web.Response(text=json.dumps(response_obj),
                        headers=headers,
                        status=200)


async def handle_save_insx_rego(request):
    try:
        pass
    except:
        pass
    finally:
        pass


async def handle_read_insx_rego(request):
    try:
        insx_rego = BASE_DIR / 'insx.rego'
        with insx_rego.open(mode='r', encoding='utf-8') as L:
            insxd = L.read()
        response_obj = {'insxd': insxd}
    except:
        response_obj = {'insxd': 'insx_rego loading failed'}
    finally:
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps(response_obj),
                            headers=headers,
                            status=200)
