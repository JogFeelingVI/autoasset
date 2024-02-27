# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-27 17:28:57
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-02-27 22:45:37
import multiprocessing
from typing import List
from codex import glns_v2, note, rego_v3, datav, filters_v3, tools
import json

postcall_length = 25
postcall_json = {}
postcall_data = {}
interimStorage = {}


def initPostCall():
    global postcall_data
    cdic = datav.LoadJson().toLix
    fite = filters_v3
    fite.initialization()
    postcall_data['glns'] = glns_v2.glnsMpls(cdic, 6, 1, 's')
    postcall_data['rego'] = rego_v3.Lexer().pares(rego_v3.load_rego_v2())
    postcall_data['filter'] = fite.SyntheticFunction()


def setting_length(length: int):
    global postcall_length
    postcall_length = length
    print(f'setting length {length}')


def instal_json(js: str):
    global postcall_json
    postcall_json = dict(json.loads(js))
    if 'range' in postcall_json.keys():
        setting_length(postcall_json['range'])
    keys = ' '.join([k for k in postcall_json.keys()][-5:])
    print(f'install jsonx, keys: {keys}...')


def in_key(key: str) -> bool:
    global postcall_json
    if key in postcall_json.keys():
        return True
    return False


def key_val(key: str) -> bool:
    global postcall_json
    return bool(postcall_json[key])


def create():
    global postcall_data

    count = 0
    while 1:
        _n = postcall_data['glns'].producer['r']()
        _t = postcall_data['glns'].producer['b']()
        n = note.Note(_n, _t)
        rfilter = True
        if in_key('rego') and key_val('rego'):
            for _, f in postcall_data['rego'].items():
                if f(n) == False:
                    rfilter = False
                    break
        for k, func in postcall_data['filter'].items():
            if in_key(k) and key_val(k):
                if func(n) == False:
                    rfilter = False
                    break
        if rfilter == True:
            return [_n, _t]
        count += 1
        if count >= 3000:
            break


def create_task(task: int):
    return [task, create()]


def manufacturingQueue():
    global interimStorage
    global postcall_length
    interimStorage = {}
    f = tools.f
    for i in range(postcall_length):
        nt = create()
        if nt != None:
            n, t = nt
            interimStorage[i] = [f(n), f(t)]


def toJson():
    global interimStorage
    if interimStorage.keys().__len__() == 0:
        manufacturingQueue()
    return json.dumps(interimStorage)


def todict():
    global interimStorage
    if interimStorage.keys().__len__() == 0:
        manufacturingQueue()
    return interimStorage


def tasks_multiprocessing():
    global interimStorage, postcall_data, postcall_length
    with multiprocessing.Pool() as p:
        from functools import partial
        indexs = [x for x in range(postcall_length)]
        chunksize = int(postcall_length * 0.083)
        results = p.map(create_task, indexs, chunksize=chunksize)
        interimStorage = {}
        for res in results:
            if isinstance(res, list):
                index, task = res
                if task is not None:
                    n, t = task
                    interimStorage[index] = [tools.f(n), tools.f(t)]
    return results
