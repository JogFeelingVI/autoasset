# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-10-20 14:47:22
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-31 19:23:23
# from Codex.datav import LoadJson
# from Codex.rego import rego
from collections import Counter, deque
import itertools
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


def dzx(N: List):
    print('glns test')
    cdic = datav.LoadJson().toLix
    glns = glns_v2.glnsMpls(cdic=cdic)
    duLie = glns_v2.formation(max=5)
    filters = glns_v2.filterN_v2()
    reeego = rego.rego()
    reeego.parse_v2()
    filters.Lever = glns.getabc
    filters.Last = glns.getlast

    count = 0
    while True:
        n = glns.creativity()
        rxfil = [f(n) for _, f in filters.filters.items()]
        if False not in rxfil:
            if reeego.filtration(n):
                duLie.addNote(n=n)
                count += 1
                print(f'[{count:^4}]: {n}')
        if count >= duLie.maxlen:
            break


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