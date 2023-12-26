# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2023-12-26 20:55:18
# @Last Modified by:   Your name
# @Last Modified time: 2023-12-26 23:12:36

from typing import List
from functools import partial
import pathlib, re

#from Codex.glns_v2 import Note

filenam = 'rego'


def load_rego_v2() -> str:
    '''装载rego文件'''
    rego = pathlib.Path(filenam)
    with rego.open(mode='r', encoding='utf-8') as go:
        return go.read()
    

class Note:
    def __init__(self) -> None:
        self.number=[]
        self.tiebie = []
        self.setnumber_R = set()
        self.setnumber_B = set()
        
    def index(self, i=1):
        return 1

        
class Lexer:
    def __init__(self, debug='') -> None:
        self.debug = debug
        self.rules = [
            #(re.compile(r'^#.*$'), self.handle_comment),
            (re.compile(r'^- [ 0-9]+as (R|B)$'), self.handle_paichu),
            (re.compile(r'^\+ [ 0-9]+as R$'), self.handle_baohan),
            (re.compile(r'^\+ [ 0-9]+ @bit([1-7])$'), self.handle_bit),
        ]
        
    def pares(self, rego:str):
        '''词法分析'''
        result = {}
        index = 1
        for line in rego.splitlines():
            for pattern, handler in self.rules:
                match = pattern.match(line)
                if match:
                    result.update({index:handler(match=match)})
                    index += 1
                    break
        return result
            
    def handle_paichu(self, match):
        match_list = match.group(0).split()
        numbers = [int(x) for x in match_list[1:-2]]
        rb = match.group(1)
        if self.debug.count('v') == 1:
            print(f'debug paichu {match.group(0)} | {numbers} ? {rb}')
        match rb:
            case 'R':
                return {'f': rego_filter.f_paichu_r, 'a': numbers}
            case 'B':
                return {'f': rego_filter.f_paichu_b, 'a': numbers}
            case _:
                return {}
            
    def handle_baohan(self, match):
        match_list = match.group(0).split()
        numbers = [int(x) for x in match_list[1:-2]]
        if self.debug.count('v') == 1:
            print(f'debug baohan {match.group(0)} | {numbers}')
        return {'f': rego_filter.f_baohan, 'a': numbers}
    
    def handle_bit(self, match):
        match_list = match.group(0).split()
        numbers = [int(x) for x in match_list[1:-2]]
        bit = int(match.group(1))
        f_bitn = partial(rego_filter.f_bit, index=bit)
        if self.debug.count('v') == 1:
            print(f'debug bit {match.group(0)} | {numbers} ? {bit}')
        return {'f': f_bitn, 'a': numbers}
    
    def handle_comment(self, match):
        '''注释'''
        print(f'debug zhushi {match.group()}')
        return {}
    
class rego_filter:

    @staticmethod
    def f_paichu_r(N: Note, args: List) -> bool:
        '''排除'''
        for _n in N.number:
            if _n in args:
                return False
        return True

    @staticmethod
    def f_paichu_b(N: Note, args: List) -> bool:
        '''排除'''
        for _n in N.tiebie:
            if _n in args:
                return False
        return True

    @staticmethod
    def f_baohan(N: Note, args: List) -> bool:
        '''包含'''
        for _n in N.setnumber_R:
            if _n in args:
                return True
        return False

    @classmethod
    def f_bit_1(cls, N: Note, args: List) -> bool:
        return cls.f_bit(N, args, 1)

    @classmethod
    def f_bit_2(cls, N: Note, args: List) -> bool:
        return cls.f_bit(N, args, 2)

    @classmethod
    def f_bit_3(cls, N: Note, args: List) -> bool:
        return cls.f_bit(N, args, 3)

    @classmethod
    def f_bit_4(cls, N: Note, args: List) -> bool:
        return cls.f_bit(N, args, 4)

    @classmethod
    def f_bit_5(cls, N: Note, args: List) -> bool:
        return cls.f_bit(N, args, 5)

    @classmethod
    def f_bit_6(cls, N: Note, args: List) -> bool:
        return cls.f_bit(N, args, 6)

    @staticmethod
    def f_bit_7(N: Note, args: List) -> bool:
        for _n in N.tiebie:
            if _n in args:
                return True
        return False

    @staticmethod
    def f_bit(N: Note, args: List, index: int) -> bool:
        '''定位 包含'''
        if index in [1, 2, 3, 4, 5, 6]:
            _n = N.index(i=index)
            if _n not in args:
                return False
        return True

    @classmethod
    def f_bitex_1(cls, N: Note, args: List) -> bool:
        return cls.f_bitex(N, args, 1)

    @classmethod
    def f_bitex_2(cls, N: Note, args: List) -> bool:
        return cls.f_bitex(N, args, 2)

    @classmethod
    def f_bitex_3(cls, N: Note, args: List) -> bool:
        return cls.f_bitex(N, args, 3)

    @classmethod
    def f_bitex_4(cls, N: Note, args: List) -> bool:
        return cls.f_bitex(N, args, 4)

    @classmethod
    def f_bitex_5(cls, N: Note, args: List) -> bool:
        return cls.f_bitex(N, args, 5)

    @classmethod
    def f_bitex_6(cls, N: Note, args: List) -> bool:
        return cls.f_bitex(N, args, 6)

    @staticmethod
    def f_bitex_7(N: Note, args: List) -> bool:
        for _n in N.tiebie:
            if _n in args:
                return False
        return True

    @staticmethod
    def f_bitex(N: Note, args: List, index: int) -> bool:
        '''定位 不包含'''
        if index in [1, 2, 3, 4, 5, 6]:
            _n = N.index(i=index)
            if _n in args:
                return False
        return True

def main():
    print("Hello, World!")
    rego = load_rego_v2()
    lexer = Lexer(debug='v')
    result = lexer.pares(rego=rego)
    print(f'ok {result}')


if __name__ == "__main__":
    main()
