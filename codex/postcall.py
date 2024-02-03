# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-01-27 17:28:57
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-02-02 14:17:12
from codex import glns_v2, note, rego_v3, datav
import json

class postcallforjson:
    '''post call for json'''
    length = 25
    jsonx = {}
    
    def __init__(self) -> None:
        cdic = datav.LoadJson().toLix
        self.glns = glns_v2.glnsMpls(cdic, 6, 1, 'c')
        self.filters = glns_v2.filterN_v2()
        self.rego = rego_v3.Lexer().pares(rego_v3.load_rego_v2())
        self.filters.Lever = self.glns.getabc
        self.filters.Last = self.glns.getlast
        
    def instal_json(self, js:str):
        self.jsonx = dict(json.loads(js))
        self.instal_length(self.jsonx['range'])
        keys = ' '.join([k for k in self.jsonx.keys()][-5:])
        print(f'install jsonx, keys: {keys}..., range: [{self.jsonx["range"]}].')
        
    def instal_length(self, length:int):
        self.length = length
        
    def in_key(self, key:str) -> bool:
        if key in self.jsonx.keys():
            return True
        return False
        
    def key_val(self, key:str) -> bool:
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
            for k, func in self.filters.filters.items():
                if self.in_key(k) and self.key_val(k):
                    if func(n) == False:
                        rfilter = False
                        break
            if rfilter == True:
                return [_n, _t]
            count += 1
            if count >= 3000:
                break
                    
        
    def toJson(self):
        temp = {}
        f = lambda x: ' '.join([f"{n:02}" for n in x])
        for i in range(self.length):
            nt = self.create()
            if nt != None:
                n, t = nt
                temp[i] = [f(n), f(t)]
        return json.dumps(temp)
        
