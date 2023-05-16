# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-16 22:12:41
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-16 23:33:39

from array import ArrayType
from multiprocessing.heap import rebuild_arena
import random
from collections import Counter
from re import S
from time import sleep
from typing import List


class Note:
    
    __vers ={
        'len': lambda x:len(set(x))==len(x)
    }
    
    def __init__(self, n:List[int], T:List[int]) -> None:
        self.number = sorted(n)
        self.tiebie = sorted(T)
        
    def __str__(self) -> str:
        n = ' '.join([f'{num:02d}' for num in self.number])
        t = ' '.join([f'{num:02d}' for num in self.tiebie])
        return f'{n} + {t}'
    
    def verify(self) -> bool:
        rxbool =[]
        for k, v in self.__vers.items():
            rxbool.extend([v(x) for x in [self.number, self.tiebie]])
        rxbool = set(rxbool)
        return [True, False][rxbool.__len__() == 2]

class glnsMpls:
    '''glns mpls'''
    
    _rlen = 6
    _blen = 1
    
    @property
    def rLan(self) -> int:
        return self._rlen
    
    def __init__(self, lix:dict) -> None:
        self.R = lix.get('R', [])
        self.B = lix.get('B', [])
        
    @staticmethod    
    def CounterRB(rb:List[int], L:int) -> List[int]:
        counter = Counter(rb)
        total = sum(counter.values())
        inverse_freq = {k: total - v for k, v in counter.items()}
        weights = list(inverse_freq.values())
        number_pool = list(inverse_freq.keys())
        result = random.choices(number_pool, weights=weights, k=L)
        return result
    
    def creativity(self) -> Note:
        while True:
            r = self.CounterRB(self.R, self._rlen)
            b = self.CounterRB(self.B, self._blen)
            n = Note(r, b)
            if n.verify():
                return n


def main():
    print("Hello, World!")
    n = Note([1, 2, 3, 4, 5, 6], [2, 3])
    print(n)


if __name__ == "__main__":
    main()
