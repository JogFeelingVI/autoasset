# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-10-20 14:47:22
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-30 22:40:25
# from Codex.datav import LoadJson
# from Codex.rego import rego
from collections import Counter, deque
import itertools
import rego, glns_v2
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
    dulie = glns_v2.formation(max=25)
    rlist = [random.choice(range(1, 34)) for i in range(1, 181)]
    rb = glns_v2.random_rb(rlist, 6)
    rb.usew = False
    rb.get_number()
    n = glns_v2.Note(rb.dep, 7)
    reego = rego.rego()
    reego.debug = True
    reego.parse_v2()
    regoo = reego.filtration(N=n)
    print(f'rego {n}')


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