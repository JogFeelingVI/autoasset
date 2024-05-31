# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-27 17:28:57
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-05-31 15:14:59
import json, itertools, concurrent.futures, os
from typing import List
from codex import glns_v2, note, rego_v3, datav, filters_v3, tools
from multiprocessing import Manager
from collections import defaultdict

postcall_length = 25
postcall_json = {}
postcall_data = {}
interimStorage = {}
Return_state = {"values": 0, "length": 0, "state": {1: 0}}
# values state == 1 的总长度
# length 任务链总长度
# state
#   -> 0 还没有开始执行
#   -> 1 顺利获得执行结果
#   -> 2 无法获取执行结果


def getReturnState():
    global_vars = globals()
    return global_vars["Return_state"]


def initReturnState(values=-1, length=-1, state=[]):
    """
    values state == 1 的总长度
    length 任务链总长度
    state [1, 0] 1 为编号 0 为状态可以是 0,1,2
        -> 0 还没有开始执行
        -> 1 顺利获得执行结果 [[1,2,3,4,5,6], [16]]
        -> 2 无法获取执行结果 None
    """
    global_vars = globals()
    _temp = {}
    if values == -1 and length == -1 and state == []:
        # 初始化状态
        _temp = {"values": 0, "length": 0, "state": {1: 0}}
    else:
        _temp = global_vars["Return_state"]
    # 第一阶段
    if length > 0:
        _temp["length"] = length
    if state != [] and state[1] < 3:
        _task, _state = state
        dict(_temp["state"]).update({_task: _state})
        if _state == 1:
            _temp["length"] += 1
    global_vars["Return_state"] = _temp


def initPostCall():
    global_vars = globals()
    data = {}
    cdic = datav.LoadJson().toLix
    fite = filters_v3
    fite.initialization()
    data["glns"] = glns_v2.glnsMpls(cdic, 6, 1, "b").producer
    data["rego"] = rego_v3.Lexer().pares(rego_v3.load_rego_v2())
    data["filter"] = fite.SyntheticFunction()
    global_vars["postcall_data"] = data


def setting_length(length: int):
    global_vars = globals()
    global_vars["postcall_length"] = length
    print(f"setting length {length}")


def instal_json(js: str):
    global_vars = globals()
    jsond = dict(json.loads(js))
    if "range" in jsond.keys():
        setting_length(int(jsond["range"]))
        initReturnState(length=int(jsond["range"]))
    keys = " ".join([k for k in jsond.keys()][-5:])
    global_vars["postcall_json"] = jsond
    print(f"install jsonx, keys: {keys}...")


def in_key(key: str, jsond: dict) -> bool:
    if key in jsond.keys():
        return True
    return False


def key_val(key: str, jsond: dict) -> bool:
    return bool(jsond[key])


def create(pcall_data: dict, jsond: dict):  # -> list[Any] | None:
    if not pcall_data:
        print(f"Not Find PostCall Data!")
        return
    count = 0
    while 1:
        _n = pcall_data["glns"]["r"]()
        _t = pcall_data["glns"]["b"]()
        # print(f'test {_n} {_t}')
        n = note.Note(_n, _t)
        rfilter = True
        # print(f'{jsond = }')
        if in_key("rego", jsond) and key_val("rego", jsond):
            for _, f in pcall_data["rego"].items():
                if f(n) == False:
                    rfilter = False
                    break
        jsond_key = [k for k, v in jsond.items() if v == True]
        filterx = {
            name: func(n)
            for name, func in pcall_data["filter"].items()
            if name in jsond_key
        }
        # print(f'{filterx = }')
        # for name, func in pcall_data['filter'].items():
        #     if name in jsond.keys():
        #         print(f'{name = }')
        # if filterx.count(False) > 1:
        #     rfilter = False
        # filterx = {'acvalue': True, 'jmsht': True, 'mod2': True, 'mod3': True, 'mod4': True, 'mod5': True, 'mod6': True, 'mod7': True, 'mod8': True, 'mod9': True, 'sixlan': True, 'zhihe': True}
        match filterx:
            case {
                "acvalue": bool() as ac,
                "jmsht": bool() as five,
            } if ac == True and five == True:
                if sum(not value for value in filterx.values()) > 0:
                    # print(f'T, T {filterx}')
                    rfilter = False
            case {
                "acvalue": bool() as ac,
                "jmsht": bool() as five,
            } if ac == False or five == False:
                # print(f'F, _ {filterx}')
                rfilter = False
            case _:
                if sum(not value for value in filterx.values()) > 0:
                    # print(f'T, T {filterx}')
                    rfilter = False

        if rfilter == True:
            return [_n, _t]
        count += 1
        if count >= 3000:
            break

def create_task_index(index, data, jsond):
    return [index, create(data, jsond)]

def create_task_v2(task, data, jsond, pd):
    temp = []
    pid = os.getpid()
    for task_index in task:
        if pid not in pd.keys():
            pd[pid] = 0
        else:
            pd[pid] += 1
        sumx = sum(pd.values())
        temp.append([task_index, create(data, jsond)])
        if task_index % 5 ==1:
            print(f"\033[K[P] create_task_v2 completed {sumx}", end="\r")
    return temp, pid


def initTaskQueue_to_list():
    global_vars = globals()
    length = global_vars["postcall_length"]
    data = global_vars["postcall_data"]
    jsond = global_vars["postcall_json"]
    return length, data, jsond

def tasks_Queue_v2():
    global_vars = globals()
    iStorage = {}
    seen_n = set()
    f = tools.f
    length, data, jsond = initTaskQueue_to_list()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(create_task_index, index, data, jsond) for index in range(length)]
        # results = [future.result() for future in concurrent.futures.as_completed(futures)]
        for future in concurrent.futures.as_completed(futures):
            index, rex = future.result()
            if rex != None:
                n, t = rex
                tup_n = tuple(n)
                if tup_n not in seen_n:
                    iStorage[index] = [f(n), f(t)]
                    seen_n.add(tup_n)
    global_vars["interimStorage"] = iStorage

def tasks_Queue():
    global_vars = globals()
    iStorage = {}
    seen_n = set()
    f = tools.f
    length, data, jsond = initTaskQueue_to_list()
    for index in range(length):
        rex = create(data, jsond)
        if rex != None:
            n, t = rex
            tup_n = tuple(n)
            if tup_n not in seen_n:
                iStorage[index] = [f(n), f(t)]
                seen_n.add(tup_n)
    global_vars["interimStorage"] = iStorage


def tasks_progress_rate_new():
    global_vars = globals()
    iStorage = {}
    length, data, jsond = initTaskQueue_to_list()
    chunk_size = max(1,length // 8)
    chunks = [range(length)[i : i + chunk_size] for i in range(0, length, chunk_size)]
    seen_n = set()
    with Manager() as mem:
        pd = mem.dict(defaultdict(int))
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(create_task_v2, i, data, jsond, pd).add_done_callback(
                    lambda future: done_task(future, iStorage, seen_n)
                )
                for i in chunks
            ]
    global_vars["interimStorage"] = iStorage


def done_task(future, storage: dict, seen: set):
    temp, pid = future.result()
    count = 0
    for i in temp:
        index, nt = i
        if nt is not None:
            n, t = nt
            tup_n = tuple(n)
            if tup_n not in seen:
                storage[index] = [tools.f(n), tools.f(t)]
                seen.add(tup_n)
                count += 1
    # print(f"Complete effective tasks {count} from worker-{pid}")


def toJson():
    global_vars = globals()
    iStorage = global_vars["interimStorage"]
    if iStorage.keys().__len__() == 0:
        return ""
    return json.dumps(iStorage)


def toDict():
    global_vars = globals()
    iStorage = dict(global_vars["interimStorage"])
    if iStorage.keys().__len__() == 0:
        return {0: ["-", "-"]}
    return iStorage
