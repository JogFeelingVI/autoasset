# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-27 17:28:57
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-03-24 09:03:03
import json, itertools, concurrent.futures, asyncio
from typing import List
from codex import glns_v2, note, rego_v3, datav, filters_v3, tools

postcall_length = 25
postcall_json = {}
postcall_data = {}
interimStorage = {}
Return_state = {'values': 0, 'length': 0, 'state': {1: 0}}
# values state == 1 的总长度
# length 任务链总长度
# state
#   -> 0 还没有开始执行
#   -> 1 顺利获得执行结果
#   -> 2 无法获取执行结果

def getReturnState():
    global_vars = globals()
    return global_vars['Return_state']

def initReturnState(values=-1, length=-1, state=[]):
    '''
    values state == 1 的总长度
    length 任务链总长度
    state [1, 0] 1 为编号 0 为状态可以是 0,1,2
        -> 0 还没有开始执行
        -> 1 顺利获得执行结果 [[1,2,3,4,5,6], [16]]
        -> 2 无法获取执行结果 None
    '''
    global_vars = globals()
    _temp = {}
    if values == -1 and length == -1 and state == []:
        #初始化状态
        _temp = {'values': 0, 'length': 0, 'state': {1: 0}}
    else:
        _temp = global_vars['Return_state']
    #第一阶段
    if length > 0:
        _temp['length'] = length
    if state != [] and state[1] < 3:
        _task,_state = state
        dict(_temp['state']).update({_task: _state})
        if _state == 1:
            _temp['length'] += 1
    global_vars['Return_state'] = _temp


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
        setting_length(int(jsond['range']))
        initReturnState(length=int(jsond['range']))
    keys = ' '.join([k for k in jsond.keys()][-5:])
    global_vars['postcall_json'] = jsond
    print(f'install jsonx, keys: {keys}...')


def in_key(key: str, jsond: dict) -> bool:
    if key in jsond.keys():
        return True
    return False


def key_val(key: str, jsond: dict) -> bool:
    return bool(jsond[key])


def create(pcall_data: dict, jsond: dict):  # -> list[Any] | None:
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


def initTaskQueue():
    global_vars = globals()
    length = global_vars['postcall_length']
    data = global_vars['postcall_data']
    jsond = global_vars['postcall_json']
    return itertools.product(range(length), [data], [jsond])


def tasks_Queue():
    global_vars = globals()
    iStorage = {}
    f = tools.f
    for iq in initTaskQueue():
        rex = create_task(iq)
        task, nt = rex
        if nt != None:
            n, t = nt
            iStorage[task] = [f(n), f(t)]
    global_vars['interimStorage'] = iStorage


def tasks_futures():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        global_vars = globals()
        iStorage = global_vars['interimStorage']
        iStorage = {}
        results = executor.map(create_task, initTaskQueue())
        for res in results:
            if isinstance(res, list):
                index, task = res
                if task is not None:
                    n, t = task
                    iStorage[index] = [tools.f(n), tools.f(t)]
        global_vars['interimStorage'] = iStorage
    return iStorage

async def tasks_progress_rate():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        global_vars = globals()
        iStorage = global_vars['interimStorage']
        iStorage = {}
        futures = [executor.submit(create_task, i) for i in initTaskQueue()]
        completed = 0
        futures_len = futures.__len__()
        for future in concurrent.futures.as_completed(futures):
            completed += 1
            _rf = future.result()
            if _rf[1] == None:
                initReturnState(state=[_rf[0], 2])
            else:
                initReturnState(state=[_rf[0], 1])
                n, t = _rf[1]
                iStorage[_rf[0]] = [tools.f(n), tools.f(t)]
            print(f'\033[K[P] completed {completed/futures_len*100:.4f}% tasks completed.', end='\r')
        print(f'\033[K[P] completed. 100%')
        global_vars['interimStorage'] = iStorage
        
        return iStorage.keys().__len__()

def toJson():
    global_vars = globals()
    iStorage = global_vars['interimStorage']
    if iStorage.keys().__len__() == 0:
        tasks_Queue()
    return json.dumps(iStorage)


def todict():
    global_vars = globals()
    iStorage = global_vars['interimStorage']
    if iStorage.keys().__len__() == 0:
        tasks_Queue()
    return iStorage
