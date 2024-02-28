# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-27 17:28:57
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-02-28 09:21:05
import multiprocessing, json, itertools
from typing import List
from codex import glns_v2, note, rego_v3, datav, filters_v3, tools

postcall_length = 25
postcall_json = {}
postcall_data = {}
interimStorage = {}


def initPostCall():
    global_vars = globals()
    data = {}
    cdic = datav.LoadJson().toLix
    fite = filters_v3
    fite.initialization()
    data['glns'] = glns_v2.glnsMpls(cdic, 6, 1, 's').producer
    data['rego'] = rego_v3.Lexer().pares(rego_v3.load_rego_v2())
    data['filter'] = fite.SyntheticFunction()
    global_vars['postcall_data'] = data


def setting_length(length: int):
    global_vars = globals()
    global_vars['postcall_length'] = length
    print(f'setting length {length}')


def instal_json(js: str):
    global_vars = globals()
    jsond = dict(json.loads(js))
    if 'range' in jsond.keys():
        setting_length(jsond['range'])
    keys = ' '.join([k for k in jsond.keys()][-5:])
    global_vars['postcall_json'] = jsond
    print(f'install jsonx, keys: {keys}...')


def in_key(key: str, jsond:dict) -> bool:
    if key in jsond.keys():
        return True
    return False


def key_val(key: str, jsond:dict) -> bool:
    return bool(jsond[key])


def create(pcall_data:dict, jsond:dict):# -> list[Any] | None:
    if not pcall_data:
        print(f'Not Find PostCall Data!')
        return
    count = 0
    while 1:
        _n = pcall_data['glns']['r']()
        _t = pcall_data['glns']['b']()
        n = note.Note(_n, _t)
        rfilter = True
        if in_key('rego', jsond) and key_val('rego', jsond):
            for _, f in pcall_data['rego'].items():
                if f(n) == False:
                    rfilter = False
                    break
        for k, func in pcall_data['filter'].items():
            if in_key(k, jsond) and key_val(k, jsond):
                if func(n) == False:
                    rfilter = False
                    break
        if rfilter == True:
            return [_n, _t]
        count += 1
        if count >= 3000:
            break


def create_task(iq):
    task, pcall_data, jsond = iq
    return [task, create(pcall_data, jsond)]


def manufacturingQueue():
    global_vars = globals()
    length = global_vars['postcall_length']
    data = global_vars['postcall_data']
    jsond = global_vars['postcall_json']
    iStorage = {}
    f = tools.f
    for i in range(length):
        nt = create(data, jsond)
        if nt != None:
            n, t = nt
            iStorage[i] = [f(n), f(t)]
    global_vars['interimStorage'] = iStorage 


def toJson():
    global_vars = globals()
    iStorage = global_vars['interimStorage']
    if iStorage.keys().__len__() == 0:
        manufacturingQueue()
    return json.dumps(iStorage)


def todict():
    global_vars = globals()
    iStorage = global_vars['interimStorage']
    if iStorage.keys().__len__() == 0:
        manufacturingQueue()
    return iStorage

def initTaskQueue():
    global_vars = globals()
    length = global_vars['postcall_length']
    data = global_vars['postcall_data']
    jsond = global_vars['postcall_json']
    return itertools.product(range(length), [data], [jsond])
    
async def tasks_multiprocessing():
    global_vars = globals()
    length = global_vars['postcall_length']
    iStorage = global_vars['interimStorage']
    with multiprocessing.Pool() as p:
        chunksize = int(length * 0.083)
        results = p.map(create_task, initTaskQueue(), chunksize=chunksize)
        iStorage = {}
        for res in results:
            if isinstance(res, list):
                index, task = res
                if task is not None:
                    n, t = task
                    iStorage[index] = [tools.f(n), tools.f(t)]
    global_vars['interimStorage'] = iStorage
    return iStorage
