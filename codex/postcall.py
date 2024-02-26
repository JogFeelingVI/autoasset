# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-27 17:28:57
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-02-26 17:12:28
from codex import glns_v2, note, rego_v3, datav, filters_v3, tools
import json, timeit, concurrent.futures, asyncio


class postcallforjson:
    '''post call for json'''
    length = 25
    jsonx = {}
    interimStorage = {}

    def __init__(self) -> None:
        cdic = datav.LoadJson().toLix
        self.glns = glns_v2.glnsMpls(cdic, 6, 1, 's')
        self.rego = rego_v3.Lexer().pares(rego_v3.load_rego_v2())
        self.fter = filters_v3
        self.fter.initialization()

    def instal_json(self, js: str):
        self.jsonx = dict(json.loads(js))
        if 'range' in self.jsonx.keys():
            self.setting_length(self.jsonx['range'])
        keys = ' '.join([k for k in self.jsonx.keys()][-5:])
        print(f'install jsonx, keys: {keys}...')

    def setting_length(self, length: int):
        self.length = length
        print(f'install length {self.length}')

    def in_key(self, key: str) -> bool:
        if key in self.jsonx.keys():
            return True
        return False

    def key_val(self, key: str) -> bool:
        return bool(self.jsonx[key])

    def create(self):
        count = 0
        while 1:
            _n = self.glns.producer['r']()
            _t = self.glns.producer['b']()
            n = note.Note(_n, _t)
            rfilter = True
            if self.in_key('rego') and self.key_val('rego'):
                for _, f in self.rego.items():
                    if f(n) == False:
                        rfilter = False
                        break
            for k, func in self.fter.SyntheticFunction().items():
                if self.in_key(k) and self.key_val(k):
                    if func(n) == False:
                        rfilter = False
                        break
            if rfilter == True:
                return [_n, _t]
            count += 1
            if count >= 3000:
                break

    def create_task(self, task: int):
        return [task, self.create()]

    def manufacturingQueue(self):
        self.interimStorage = {}
        f = tools.f
        for i in range(self.length):
            nt = self.create()
            if nt != None:
                n, t = nt
                self.interimStorage[i] = [f(n), f(t)]

    def tasks_submit(self):
        # 创建一个线程池
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
        # print(f'executor done')

        # # 创建一个消息队列
        # queue = asyncio.Queue(maxsize=self.length)
        # for i in range(self.length):
        #     queue.put_nowait(i)
        # if queue.empty():
        #     print(f'queue is empty {queue.empty()}')

        self.interimStorage = {}
        

        # 等待所有任务完成
        results = executor.map(self.create_task, range(self.length))
        for res in results:
            if isinstance(res, list):
                index, task = res
                if task is not None:
                    n, t = task
                    self.interimStorage[index] = [tools.f(n), tools.f(t)]
        return self.interimStorage

    def toJson(self):
        if self.interimStorage.keys().__len__() == 0:
            self.manufacturingQueue()
        return json.dumps(self.interimStorage)

    def todict(self):
        if self.interimStorage.keys().__len__() == 0:
            self.manufacturingQueue()
        return self.interimStorage
