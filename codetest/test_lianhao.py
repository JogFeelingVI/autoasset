# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-10-20 14:47:22
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-29 21:29:32
# from Codex.datav import LoadJson
# from Codex.rego import rego
from collections import Counter
import itertools
from pdb import run
import random
from typing import List, Self
import unittest, time, os


class Note:

    def __init__(self, n: List[int], T: List[int] | int) -> None:
        """Note

        Args:
            n (List[int]): 1-33 红色号码球
            T (List[int] | int): 1-16 蓝色号码球
        """
        self.number = []
        self.tiebie = []
        for i in sorted(n):
            if 1 <= i <= 33 and n.count(i) == 1:
                self.number.append(i)
        Tx = [T, [T]][isinstance(T, int)]
        for i in sorted(Tx):
            if 1 <= i <= 16 and Tx.count(i) == 1:
                self.tiebie.append(i)
        if self.number.__len__() < 6 or self.tiebie.__len__() == 0:
            raise Exception(f'Note Creation failed {self.number}')

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
    fixrb = {}

    __Lever = {}
    __Last = [0, 0, 0, 0, 0, 0]

    @property
    def Lever(self) -> dict:
        ''' 出号频率等级 '''
        return self.__Lever

    @Lever.setter
    def Lever(self, value: dict) -> None:
        self.__Lever = value

    @property
    def Last(self) -> List[int]:
        ''' 最后的出号 '''
        return self.__Last

    @Last.setter
    def Last(self, value: List[int]):
        self.__Last = value

    def __init__(self) -> None:
        self.filters = {
            'sixlan': self.sixlan,
            'linma': self.linma,
            'duplicates': self.duplicates,
            'lianhao': self.lianhao,
            'denji': self.denji,
            'hisdiff': self.hisdiff,
            'ac': self.acvalue,
            'dzx': self.dzx
        }

    def dzx(self, N: Note) -> bool:
        '''xiao zhong da'''
        a = range(1, 34)
        g = [a[i:i + 11] for i in range(0, len(a), 11)]
        count = [[], [], []]
        for ai in N.setnumber_R:
            index = 1
            while True:
                if ai in g[index]:
                    count[index].append(ai)
                    break
                else:
                    if ai < min(g[index]):
                        index -= 1
                    if ai > max(g[index]):
                        index += 1

        flgrex = [len(x) for x in count]
        rebool = [False, True][5 not in flgrex or 6 in flgrex]
        return rebool

    def acvalue(self, N: Note) -> bool:
        '''计算数字复杂程度 默认 P len = 6'''
        p = N.setnumber_R
        ac = len(set(x - y for x in p for y in p if x > y)) - (len(p) - 1)
        return [True, False][ac > 4]

    def linma(self, N: Note) -> bool:
        '''计算临码'''
        plus_minus = []
        for n in N.setnumber_R:
            if n + 1 in self.Last or n - 1 in self.Last:
                plus_minus.append(n)
        return [False, True][plus_minus.__len__() in (0, 1, 2, 3)]

    def duplicates(self, N: Note) -> bool:
        '''计算数组是否有重复项目'''
        duplic = N.setnumber_R & set(self.Last)
        return [False, True][duplic.__len__() in (0, 1, 2)]

    def sixlan(self, N: Note) -> bool:
        '''判断红色区域是否等于 1, 2, 3, 4, 5, 6, 7'''
        ntoe = {1, 2, 3, 4, 5, 6}
        rb = [False, True][N.setnumber_R != ntoe]
        return rb

    def lianhao(self, n: Note) -> bool:
        count = []
        for v in n.setnumber_R:
            if not count or v != count[-1][-1] + 1:
                count.append([])
            count[-1].append(v)
        flgrex = sorted([len(v) for v in count if len(v) > 1])
        rebool = [False, True][flgrex in [[], [3], [2], [2, 2]]]
        return rebool

    def hisdiff(self, N: Note) -> bool:
        '''
        hisdiff 与上一期号码对比
        '''
        diff = [abs(a - b) for a, b in itertools.product(N.number, self.Last)]
        Rex = [False, True][diff.count(1) in [0, 1, 2]]
        return Rex

    def denji(self, N: Note) -> bool:
        '''
        [(4, 1), (20, 3), (7, 3), (23, 3), (21, 3), (2, 4), (29, 4), (28, 4), (5, 4), (12, 4), (17, 4)]
        '''
        bools = False
        if self.Lever.keys() == 0:
            return True
        rex = []
        for _, v in self.Lever.items():
            vz = [x[0] for x in v]
            rex.append(any(x in N.setnumber_R for x in vz))
        bools = [False, True][False not in rex]
        return bools


class random_rb:
    '''random R & B'''
    __usew = False

    def __init__(self, rb: List[int], L: int) -> None:
        self.dep = [0] * L
        self.duilie = rb
        self.nPool = []
        self.weights = None

    @property
    def usew(self) -> bool:
        return self.__usew

    @usew.setter
    def usew(self, value: bool):
        self.__usew = value

    def find_zero(self) -> int:
        '''find zero'''
        if 0 in self.dep:
            return self.dep.index(0)
        return -1

    def __initializations(self):
        '''initialization data'''
        if self.nPool == [] or self.weights == None:
            counter = Counter(self.duilie)
            total = max(counter.values())
            inverse_freq = {k: total - v for k, v in counter.items()}
            self.nPool = list(inverse_freq.keys())
            self.weights = list(inverse_freq.values())

    def get_number(self):
        find = self.find_zero()
        if find == -1:
            return True

        if self.nPool == []:
            self.__initializations()
        if self.usew:
            result = random.choices(self.nPool, weights=self.weights, k=6)
        else:
            result = random.choices(self.nPool, k=6)
        for num in result:
            if self.__isok(n=num, index=find):
                self.dep[find] = num
                if self.get_number():
                    return True
                self.dep[find] = 0
        return False

    def __isok(self, n: int, index: int) -> bool:
        '''判断数字是否符合标准'''
        if n in self.dep:
            return False
        return True


def runtime(func):

    def inst(*args, **kwargs):
        t1 = time.time()
        for i in range(1000 * 10):
            rex = func(*args, **kwargs)
        t2 = time.time()
        print(f'    -> Run time {t2-t1:.4f}s')

    return inst


@runtime
def dzx(N: List):
    print('glns test')
    rlist = [random.choice(range(1, 34)) for i in range(1, 181)]
    rb = random_rb(rlist, 6)
    rb.usew = False
    rb.get_number()
    n = Note(rb.dep, 7)
    filters = filterN_v2()
    refilter = [f'key {k:>9} -> {f(n)}' for k, f in filters.filters.items()]
    print(refilter)


class lianhaotest(unittest.TestCase):

    def setUp(self) -> None:
        self.a = [1, 2, 6, 7, 8, 10]
        self.b = [20, 9, 3, 19, 21, 28]
        self.c = [6, 9, 11, 12, 19, 25]
        return super().setUp()

    def test_linma(self):
        '''test linma'''
        rex_a = dzx(self.a)
        #print(f'Linma {rex_a}')


if __name__ == '__main__':
    unittest.main()