# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-16 22:12:41
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-30 22:26:35

from array import ArrayType
from multiprocessing.heap import rebuild_arena
from pathlib import Path
import random, re, itertools
from collections import Counter
from typing import List
from Codex import datav


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

    __vers = {'len': lambda x: len(set(x)) == len(x)}

    def __init__(self, n: List[int], T: List[int] | int) -> None:
        self.number = sorted(n)
        self.tiebie = [T, [T]][isinstance(T, int)]

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

    def verify(self) -> bool:
        rxbool = []
        for k, v in self.__vers.items():
            rxbool.extend([v(x) for x in [self.number, self.tiebie]])
        return [False, True][rxbool.count(True) == 2]


class filterN:
    init: bool = False
    referto = None
    fixrb = {}

    def __init__(self, referto: Note, lvc: dict) -> None:
        self.rego = Path('rego')
        #print(self.rego.stat().st_ctime)
        if self.rego.exists():
            self.init = True
            self.load_rego()
            if referto is not None:
                self.referto = referto
            self.lvc = lvc

    def verify(self, N: Note) -> bool:
        Rex = []
        if self.init == False:
            return True
        if 'R' in self.fixrb.keys():
            intersection = N.setnumber_R.intersection(set(self.fixrb['R']))
            Rex.append([False, True][intersection.__len__() == 0])
        if 'B' in self.fixrb.keys():
            intersection = N.setnumber_B.intersection(set(self.fixrb['B']))
            Rex.append([False, True][intersection.__len__() == 0])
        if '+' in self.fixrb.keys():
            intersection = N.setnumber_R.intersection(set(self.fixrb['+']))
            Rex.append([False, True][intersection.__len__() > 0])
            
        if False in Rex:
            return False
        else:
            if self.referto is not None:
                diff = [
                    abs(a - b) for a, b in itertools.product(N.number, N.number)
                ]
                Rex.append([False, True][diff.count(1) in [0, 1, 2]])

                Rex.append(self.verify_Three_categories(N.number))
                
        if False in Rex:
            return False
        else:
            return True


    def load_rego(self):
        _huanhang = re.compile(r'\\n')
        _zs = re.compile(r'^#.*')
        _bh = re.compile(r'^\+([ 0-9]+)$')
        _pc = re.compile(r'^-([ 0-9]+)as [R|B]$')
        with self.rego.open(mode='r', encoding='utf-8') as go:
            reglins = go.readlines()
            for linx in reglins:
                if not _zs.match(linx):
                    tmp_huan = _huanhang.sub('', linx)
                    if (remac := _pc.match(tmp_huan)) != None:
                        self.__fix_rb(remac.string)
                    if (remac := _bh.match(tmp_huan)) != None:
                        self.__fix_bh(remac.string)

    def __fix_rb(self, match: str):
        _nums = re.compile('[0-9]{1,2}')
        _fixw = re.compile('(R|B)$')
        pfix = _fixw.findall(match)
        numx = [int(x, base=10) for x in _nums.findall(match)]
        for p in pfix:
            self.fixrb.update({p: numx})

    def __fix_bh(self, match: str):
        _nums = re.compile('[0-9]{1,2}')
        numx = [int(x) for x in _nums.findall(match)]
        self.fixrb.update({'+': numx})

    def consecutive(self, N: List[int]) -> bool:
        bools = False
        count = 0
        for i in range(len(N) - 1):
            _n = N[i]
            _n1 = _n + 1
            while True:
                if _n1 in N:
                    count += 1
                    _n1 += 1
                else:
                    break
        #print(count)
        if count in [0, 1, 2]:
            bools = True
        return bools

    def verify_Three_categories(self, number: List) -> bool:
        bools = False
        level1_elements = [item[0] for item in self.lvc.get('lv1', [])]
        level2_elements = [item[0] for item in self.lvc.get('lv2', [])]
        level3_elements = [item[0] for item in self.lvc.get('lv3', [])]
        # 检查号码中是否包含每个等级的元素
        contains_level1 = any(element in number for element in level1_elements)
        contains_level2 = any(element in number for element in level2_elements)
        contains_level3 = any(element in number for element in level3_elements)
        if contains_level1 and contains_level2 and contains_level3:
            bools = True

        return bools


class glnsMpls:
    '''glns mpls'''

    _rlen = 6
    _blen = 1
    _deep = 10000 * 1

    @property
    def rLan(self) -> int:
        return self._rlen

    def __init__(self, lix: dict) -> None:
        self.R = lix.get('R', [])
        fix_r = [x for x in range(1, 34) if x not in self.R]
        self.R.extend(fix_r)

        self.groupby = [self.R[i:i + 6] for i in range(0, len(self.R), 6)]

        self.B = lix.get('B', [])
        fix_b = [x for x in range(1, 17) if x not in self.B]
        self.B.extend(fix_b)

        self._datav = datav.data_visualization(Lix=lix)

        self.filter = filterN(referto=Note(self.groupby[0], self.B[0]),
                              lvc=self._datav.Three_categories())

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
                return Note([1, 2, 3, 4, 5, 6], [7])
            if n.verify():
                if self.filter.verify(N=n):
                    if self.filter.consecutive(N=r):
                        if self.maxjac(N=n) < 0.34:
                            return n

    def maxjac(self, N: Note) -> float:
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
    print("Hello, World!")
    n = Note([1, 2, 3, 4, 5, 6], [2, 3])
    block = splitqueue().queuestr()
    print(block)


if __name__ == "__main__":
    main()
