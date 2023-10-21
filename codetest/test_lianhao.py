# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-10-20 14:47:22
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-21 18:26:54
from random import randrange
from typing import List
import unittest, time


def runtime(func):

    def inst(*args, **kwargs):
        t1 = time.time()
        for i in range(1000 * 10):
            rex = func(*args, **kwargs)
        t2 = time.time()
        print(f'    -> Run time {t2-t1:.4f}s')

    return inst


@runtime
def linma(N: list, L: list):
    '''计算临码'''
    ranges = []
    for x in N:
        if 1 in (abs(x - y) for y in L):
            ranges.append(x)
    #print(f'linma {linma}')
    #return [False, True][linma.__len__() in (0, 1, 2, 3)]


def linma_2(N: List, L: List):
    ranges = []
    for n in N:
        if n + 1 in L or n - 1 in L:
            ranges.append(n)
    #print(f'ranges {ranges}')
    flgrex = len(ranges)
    print(f'flgrex {flgrex} {ranges}')


def lianhao(N: List[int]) -> List | None:
    ranges = []
    for n in N:
        if not ranges or n != ranges[-1][-1] + 1:
            ranges.append([])
        ranges[-1].append(n)
    return [len(r) for r in ranges if len(r) > 1]


@runtime
def dzx(N: List):
    a = range(1, 34)
    g = [a[i:i + 11] for i in range(0, len(a), 11)]
    count = [[], [], []]
    for ai in N:
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
    print(f'{flgrex}')


class lianhaotest(unittest.TestCase):

    def setUp(self) -> None:
        self.a = [1, 2, 6, 7, 8, 10]
        self.b = [20, 9, 3, 19, 21, 28]
        self.c = [6, 9, 11, 12, 19, 25]
        return super().setUp()

    def test_linma(self):
        '''test linma'''
        rex_a = dzx(N=self.c)
        #print(f'Linma {rex_a}')


if __name__ == '__main__':
    unittest.main()