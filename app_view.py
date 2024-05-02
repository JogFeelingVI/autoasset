# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-12 21:03:10
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-05-02 21:48:37
from codex import filters_v3, gethtml, postcall, tools
from aiohttp import web, WSMsgType
from app_setting import BASE_DIR
import aiohttp_jinja2, json, random, asyncio, time


@aiohttp_jinja2.template("index.html")
async def index(request):
    lock_json = BASE_DIR / "luck.json"
    with lock_json.open(mode="r", encoding="utf-8") as L:
        jsond = json.loads(L.read())

    DataFrame = BASE_DIR / "DataFrame.json"
    with DataFrame.open(mode="r", encoding="utf-8") as L:
        df = json.loads(L.read())
        n = df["R"][-6::]
        t = df["B"][-1]
        nt = f"{tools.f(n)} + {tools.dS(t)}"
        Ltime = tools.diffnow(df["date"])
    return {"luck": jsond[f"{random.randint(1,6)}"], "Last": nt, "Ltime": Ltime}


@aiohttp_jinja2.template("science.html")
async def science(request):
    Ltime = tools.nowstr()
    return {"Ltime": Ltime}


async def favicon(request):
    # Content-Type: image/vnd.microsoft.icon
    headers = {"Content-Type": "mage/vnd.microsoft.icon"}
    return web.FileResponse(BASE_DIR / "static" / "favicon.ico")


async def handle(request):
    """这个地方似乎要使用 ASYNC 来处理 get html"""
    response_obj = {"time": "---", "status": "done"}
    try:
        DataFrame = BASE_DIR / "DataFrame.json"
        if DataFrame.exists() == False:
            response_obj.update({"message": "DataFrame exists is Not"})
        url = "https://www.cjcp.cn/zoushitu/cjwssq/hqaczhi.html"
        data_fr = gethtml.toDict(gethtml.get_html(url).neirong)
        Last = f'{tools.f(data_fr["R"][-6::])} + {tools.dS(data_fr["B"][-1])}'
        response_obj.update({"time": data_fr.get("date", "")})
        response_obj.update({"Last": Last})
        json_str = json.dumps(data_fr)
        with open(DataFrame, "w") as datajson:
            datajson.write(json_str)
            hszie = json_str.__sizeof__()
            response_obj.update(
                {"message": f"The data has been updated, sized {hszie}"}
            )
    except:
        response_obj.update({"message": "Network connection failed"})
    finally:
        print(f"handle GET {response_obj}")
        headers = {"Content-Type": "application/json"}
        return web.Response(text=json.dumps(response_obj), headers=headers, status=200)


async def blocking_code_task(loop: asyncio.BaseEventLoop, p, request: web.Request):
    """Wrapper to be used in asyncio Task"""
    r = await loop.run_in_executor(executor=request.app["workers_pool"], func=p)


async def handle_post(request):
    """js done onclick"""
    try:
        start = time.time()
        request_data = await request.json()
        p = postcall
        p.initPostCall()
        p.instal_json(js=request_data)
        # p.tasks_futures()
        # rejs = p.toJson()
        # loop.run_in_executor(executor=request.app["workers_pool"], func=p.tasks_progress_rate)
        # tracemalloc.stop()
        p.tasks_progress_rate_new()
        #! todo 这是新的方法
        # asyncio.gather(p.tasks_progress_rate())
        rejs = p.toJson()
        end = time.time() - start
    except:
        rejs = {"1": ["error", "ER"]}
    finally:
        print(f"postcall is done! {p.interimStorage.keys().__len__()} {end:.2f}")
        headers = {"Content-Type": "application/json"}
        return web.Response(text=json.dumps(rejs), headers=headers, status=200)


async def handle_get_Detailed_configuration(request):
    response_obj = {"list": [], "status": "done"}
    try:
        fter = filters_v3
        fter.initialization()
        class_attrs = fter.Detailed_configuration_table()

        response_obj.update({"list": class_attrs})
    except:
        response_obj.update({"status": "Error"})
    finally:
        print(f"handle GET filter_v3 Detailed_configuration {class_attrs.__len__()}")
        # print(f'class {class_attrs = } {checked = }')
        headers = {"Content-Type": "application/json"}
        return web.Response(text=json.dumps(response_obj), headers=headers, status=200)


async def handle_get_filter_name(request):
    response_obj = {"list": [], "checked": [], "status": "done"}
    try:
        fter = filters_v3
        fter.initialization()
        class_attrs, checked = fter.classAttrs()

        response_obj.update({"checked": checked})
        response_obj.update({"list": class_attrs})
    except:
        response_obj.update({"status": "Error"})
    finally:
        print(f"handle GET filter_v3 name {class_attrs.__len__()}")
        # print(f'class {class_attrs = } {checked = }')
        headers = {"Content-Type": "application/json"}
        return web.Response(text=json.dumps(response_obj), headers=headers, status=200)


async def handle_save_filterN_v3(request):
    filterN_v3 = BASE_DIR / "filterN_v3.json"
    response_obj = {"message": "", "path": filterN_v3}
    try:
        request_json = await request.json()
        with filterN_v3.open(mode="r", encoding="utf-8") as rJson:
            json_data = dict(json.loads(rJson.read()))
            json_data.update({'filter':request_json})
        with filterN_v3.open(mode="w", encoding="utf-8") as wJson:
            wJson.write(json.dumps(json_data, indent=4))
            
        response_obj.update({"message": "filterN_v3.json File writing completed."})
    except:
        response_obj.update({"message": "filterN_v3.json File write failed."})
    finally:
        print(f'message: {response_obj["message"]}')
        headers = {"Content-Type": "application/json"}
        return web.Response(
            text=json.dumps({"msg": "test"}), headers=headers, status=200
        )


async def handle_save_insx_rego(request):
    insx_rego = BASE_DIR / "insx.rego"
    response_obj = {"message": "", "path": insx_rego}
    try:
        with insx_rego.open(mode="w", encoding="utf-8") as L:
            request_data = await request.json()
            L.write(request_data["insxd"])
            response_obj.update({"message": "insx.rego File writing completed."})
    except:
        response_obj.update({"message": "insx.rego File write failed."})
    finally:
        print(f'message: {response_obj["message"]}')
        headers = {"Content-Type": "application/json"}
        return web.Response(
            text=json.dumps({"msg": "test"}), headers=headers, status=200
        )


async def handle_read_insx_rego(request):
    insx_rego = BASE_DIR / "insx.rego"
    response_obj = {"insxd": "", "message": ""}
    try:
        with insx_rego.open(mode="r", encoding="utf-8") as L:
            insxd = L.read()
            response_obj.update({"insxd": insxd})
            response_obj.update({"message": "insx_rego loading completed."})
    except:
        response_obj = {"message": "insx_rego loading failed."}
    finally:
        print(f'message: {response_obj["message"]}')
        headers = {"Content-Type": "application/json"}
        return web.Response(text=json.dumps(response_obj), headers=headers, status=200)


async def handle_ws(request):
    print("Websocket connection starting.")
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print("Websocket connection ready.")
    async for msg in ws:
        print(msg)
        if msg.type == WSMsgType.TEXT:
            print(msg.data)
            if msg.data == "close":
                await ws.close()
            else:
                await ws.send_str(msg.data + "/answer")

    print("Websocket connection closed")
    return ws
