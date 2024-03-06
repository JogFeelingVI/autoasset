# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:03:10
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-03-06 15:23:17
from codex import filters_v3, gethtml, postcall, tools
from aiohttp import web
from app_setting import BASE_DIR
import aiohttp_jinja2, json, random


@aiohttp_jinja2.template('index.html')
async def index(request):
    lock_json = BASE_DIR / 'luck.json'
    with lock_json.open(mode='r', encoding='utf-8') as L:
        jsond = json.loads(L.read())
        
    DataFrame = BASE_DIR / 'DataFrame.json'
    with DataFrame.open(mode='r', encoding='utf-8') as L:
        df = json.loads(L.read())
        n = df['R'][-6::]
        t = df['B'][-1]
        nt = f'{tools.f(n)} + {tools.dS(t)}'
        Ltime = tools.diffnow(df['date'])
    return {'luck':jsond[f'{random.randint(1,6)}'], 'Last':nt, 'Ltime': Ltime}

@aiohttp_jinja2.template('science.html')
async def science(request):
    Ltime = tools.nowstr()
    return {'Ltime': Ltime}


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
        Last = f'{tools.f(data_fr["R"][-6::])} + {tools.dS(data_fr["B"][-1])}'
        response_obj.update({'time': data_fr.get('date', '')})
        response_obj.update({'Last': Last})
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
    '''js done onclick'''
    try:
        request_data = await request.json()
        p = postcall
        p.initPostCall()
        p.instal_json(js=request_data)
        p.tasks_futures()
        rejs = p.toJson()
        #! todo 这是新的方法
        
    except:
        rejs = {'1': ['error', 'ER']}
    finally:
        print(f'postcall is done! length {p.interimStorage.keys().__len__()}')
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps(rejs), headers=headers, status=200)


async def handle_get_filter_name(request):
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
        print(f'handle GET filter_v3 name {class_attrs.__len__()}')
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
            response_obj.update({'message': 'insx.rego File writing completed.'})
    except:
        response_obj.update({'message': 'insx.rego File write failed.'})
    finally:
        print(f'message: {response_obj["message"]}')
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps({'msg': 'test'}),
                            headers=headers,
                            status=200)


async def handle_read_insx_rego(request):
    insx_rego = BASE_DIR / 'insx.rego'
    response_obj = {'insxd': '', 'message':''}
    try:
        with insx_rego.open(mode='r', encoding='utf-8') as L:
            insxd = L.read()
            response_obj.update({'insxd': insxd})
            response_obj.update({'message': 'insx_rego loading completed.'})
    except:
        response_obj = {'message': 'insx_rego loading failed.'}
    finally:
        print(f'message: {response_obj["message"]}')
        headers = {'Content-Type': 'application/json'}
        return web.Response(text=json.dumps(response_obj),
                            headers=headers,
                            status=200)
