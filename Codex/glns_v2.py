# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-21 21:14:47
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-09-23 15:49:55

from cProfile import label
from collections import Counter
import random
from typing import List
from .datav import LoadJson


class splitqueue:

    @staticmethod
    def queuestr(n: int = 4, gsize: int = 5) -> str:
        '''
            gsize group size = 5 
            n gsize * n
        '''
        block = ['■' * gsize] * n
        return '□'.join(block)


class Note:

    def __init__(self, n: List[int], T: List[int] | int) -> None:
        self.number = sorted(n)
        self.tiebie = [T, [T]][isinstance(T, int)]

    def filter(self, func) -> None:
        '''
        filter jiekou
        '''
        self.number = list(filter(func, self.number))

    @property
    def setnumber_R(self):
        return set(self.number)

    @property
    def setnumber_B(self):
        return set(self.tiebie)

    def __str__(self) -> str:
        n = ' '.join([f'{num:02d}' for num in self.number])
        t = ' '.join([f'{num:02d}' for num in self.tiebie])
        return f'{n} + {t}'


class filterN_v2:
    ''' 对Note进行过滤 '''
    filters = {}

    def __init__(self) -> None:
        self.filters = {
            'lens': self.lens,
            'sixlan': self.sixlan,
        }

    def lens(self, N: Note) -> bool:
        '''判断红色区域和蓝色区域是否在去重之后长度是否一致'''
        lamb = lambda x: len(set(x)) == len(x)
        rb_b = [lamb(x) for x in [N.setnumber_B, N.setnumber_R]]
        rb = [True, False][False in rb_b]
        return rb

    def sixlan(self, N: Note) -> bool:
        '''判断红色区域是否等于 1, 2, 3, 4, 5, 6, 7'''
        ntoe = {1, 2, 3, 4, 5, 6}
        rb = [False, True][N.setnumber_R != ntoe]
        return rb


class glnsMpls:
    '''glns mpls'''

    _rlen = 6
    _blen = 1
    _deep = 10000 * 1

    @property
    def rLen(self) -> int:
        return self._rlen

    @rLen.setter
    def rLen(self, value: int) -> None:
        if value >= 6 and value <= 19:
            self._rlen = value

    @property
    def bLen(self) -> int:
        return self._blen

    @bLen.setter
    def bLen(self, value: int) -> None:
        if value >= 1 and value <= 16:
            self._blen = value

    def __init__(self, cdic: dict) -> None:
        if 'R' in cdic and 'B' in cdic:
            self.R = self.__fixrb(max=33, n=cdic.get('R', []))
            self.B = self.__fixrb(max=16, n=cdic.get('B', []))
            if self.R != None and self.B != None:
                self.groupby = [
                    self.R[i:i + 6] for i in range(0, len(self.R), 6)
                ]

    @staticmethod
    def __fixrb(max: int = 16, n: List[int] = []) -> List[int]:
        '''
        修复 R B 中缺失的数字
        '''
        max_set = set([x for x in range(1, max + 1)])
        if max == 16 or max == 33 and n is not None:
            fix = max_set.difference(set(n))
            if fix is None:
                return list(max_set)
            else:
                n.extend(list(fix))
                return n
        else:
            return list(max_set)

    @staticmethod
    def CounterRB(rb: List[int], L: int) -> List[int]:
        counter = Counter(rb)
        total = max(counter.values())
        inverse_freq = {k: total - v for k, v in counter.items()}
        weights = list(inverse_freq.values())
        number_pool = list(inverse_freq.keys())
        result = random.choices(number_pool, weights=weights, k=L)
        return result

    def creativity(self) -> Note:
        Count = 0
        while True:
            r = self.CounterRB(self.R, self._rlen)
            b = self.CounterRB(self.B, self._blen)
            n = Note(r, b)
            Count += 1
            if Count >= self._deep:
                self.creativity()
            # n filter
            if self.maxjac(N=n) < 0.34:
                return n

    def maxjac(self, N: Note) -> float:
        # [2, 6, 20, 25, 29, 33]
        g = [self.jaccard(x, N.number) for x in self.groupby]
        return max(g)

    @staticmethod
    def jaccard(A: List, B: List) -> float:
        set_a = set(A)
        set_b = set(B)
        intersection = len(set_a.intersection(set_b))
        union = len(set_a.union(set_b))
        return intersection / union


def main():
    n = Note(n=[1, 2, 3, 4, 5, 6], T=[1, 15])
    print(f'Hello Note {n}')
    block = splitqueue().queuestr()
    cdic = LoadJson().toLix
    glns = glnsMpls(cdic=cdic)
    print(f'glns {glns.creativity()}')


if __name__ == "__main__":
    main()
