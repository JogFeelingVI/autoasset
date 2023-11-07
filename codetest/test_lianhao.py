# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-10-20 14:47:22
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-11-07 21:17:33
# from Codex.datav import LoadJson
# from Codex.rego import rego
from collections import Counter, deque
import itertools
import math
import rego, glns_v2, datav
import random
from typing import List
import unittest, time, os


def runtime(func):
    def inst(*args, **kwargs):
        t1 = time.time()
        for i in range(1000 * 10):
            rex = func(*args, **kwargs)
        t2 = time.time()
        print(f'    -> Run time {t2-t1:.4f}s')
    return inst

@runtime
def cosv(x:List, y:List):
    dot = sum(a*b for a, b in zip(x, y))
    normx = math.sqrt(sum([a*a for a in x]))
    normy = math.sqrt(sum([a*a for a in y]))
    cos = dot / (normx * normy)
    print(f'COS {cos}')

def dzx():
    print('glns test')
    cdic = datav.LoadJson().toLix
    glns = glns_v2.glnsMpls(cdic=cdic)
    duLie = glns_v2.formation(max=25)
    filters = glns_v2.filterN_v2()
    reeego = rego.rego()
    reeego.parse_v2()
    filters.Lever = glns.getabc
    filters.Last = glns.getlast
    
    count = 0
    while True:
        # n = glns 是最慢的
        n=glns.creativity()
        # = True
        for k, func in filters.filters.items():
            if func(n) == False:
                #rxfil = False
                #print(f'key {k} is False')
                break
        if reeego.filtration(n):
            duLie.addNote(n=n)
            count += 1
            print(f'[{count:^4}]: {n}')

        if count >= duLie.maxlen:
            break


class lianhaotest(unittest.TestCase):

    def setUp(self) -> None:
        self.a = [10, 24, 26, 28, 29, 31]
        self.b = [3, 8, 19, 22, 26, 32]
        self.c = [11,15,18,24,26,32]
        return super().setUp()

    def test_linma(self):
        '''test linma'''
        rex_a = dzx()
        #print(f'Linma {rex_a}')


if __name__ == '__main__':
    unittest.main()