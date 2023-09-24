# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-21 21:14:47
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-09-24 11:44:17

from collections import Counter, deque
import itertools
import random, re
from typing import List
from pathlib import Path
from .datav import LoadJson


class splitqueue:

    @staticmethod
    def queuestr(n: int = 4, gsize: int = 5) -> str:
        '''
            gsize group size = 5 
            n gsize * n
        '''
        block = ['+' * gsize] * n
        return '-'.join(block)


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
    fixrb = {}

    __Lever = {}
    __Last = [0, 0, 0, 0, 0, 0]

    @property
    def Lever(self) -> dict:
        return self.__Lever

    @Lever.setter
    def Lever(self, value: dict) -> None:
        self.__Lever = value

    @property
    def Last(self) -> List[int]:
        return self.__Last

    @Last.setter
    def Last(self, value: List[int]):
        self.__Last = value

    def __init__(self) -> None:
        self.load_rego()
        self.filters = {
            'lens': self.lens,
            'sixlan': self.sixlan,
            'rego': self.rego,
            'lianhao': self.lianhao,
            'denji': self.denji,
            'hisdiff': self.hisdiff,
        }

    def lens(self, N: Note) -> bool:
        '''判断红色区域和蓝色区域是否在去重之后长度是否一致'''
        lamb = lambda x: len(set(x)) == len(x)
        rb_b = [lamb(x) for x in [N.number, N.tiebie]]
        rb = [True, False][False in rb_b]
        return rb

    def sixlan(self, N: Note) -> bool:
        '''判断红色区域是否等于 1, 2, 3, 4, 5, 6, 7'''
        ntoe = {1, 2, 3, 4, 5, 6}
        rb = [False, True][N.setnumber_R != ntoe]
        return rb

    def lianhao(self, n: Note) -> bool:
        count = 0
        for i in range(len(n.setnumber_R) - 1):
            _n1 = n.number[i] + 1
            while True:
                if _n1 in n.number:
                    count += 1
                    _n1 += 1
                else:
                    break
        rebool = [False, True][count in [0, 1, 2]]
        return rebool

    def rego(self, N: Note) -> bool:
        '''根据rego规则判断项目是否符合标准'''
        rebool = False
        if self.fixrb is {}:
            # rego 规则不存在或者rego没有定义任何规则
            rebool = True
        else:
            Rex = []
            keysrb = self.fixrb.keys()
            if 'R' in keysrb:
                intersection = N.setnumber_R.intersection(set(self.fixrb['R']))
                Rex.append([False, True][intersection.__len__() == 0])
            if 'B' in keysrb:
                intersection = N.setnumber_B.intersection(set(self.fixrb['B']))
                Rex.append([False, True][intersection.__len__() == 0])
            if '+' in keysrb:
                intersection = N.setnumber_R.intersection(set(self.fixrb['+']))
                Rex.append([False, True][intersection.__len__() > 0])
            if 'bit' in keysrb:
                bit_number = dict(self.fixrb['bit'])
                for bit, number in bit_number.items():
                    bit = int(bit)
                    Nbit = {0}
                    if bit in [6, 1, 2, 3, 4, 5]:
                        Nbit = {N.number[bit - 1]}
                    if bit in [7]:
                        Nbit = N.setnumber_B
                    #print(f'bit {bit} num {number} NB {Nbit}')
                    intersection = Nbit.intersection(set(number))
                    Rex.append([False, True][intersection.__len__() > 0])
            rebool = [True, False][False in Rex]
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

    def load_rego(self):
        rego = Path('rego')
        _huanhang = re.compile(r'\\n')
        _zs = re.compile(r'^#.*')
        _bh = re.compile(r'^\+([ 0-9]+)$')
        _pc = re.compile(r'^-([ 0-9]+)as [R|B]$')
        _bit = re.compile(r'^\+([ 0-9]+)@bit[1-7]$')
        with rego.open(mode='r', encoding='utf-8') as go:
            reglins = go.readlines()
            for linx in reglins:
                if not _zs.match(linx):
                    tmp_huan = _huanhang.sub('', linx)
                    if (remac := _pc.match(tmp_huan)) != None:
                        self.__fix_rb(remac.string)
                    if (remac := _bh.match(tmp_huan)) != None:
                        self.__fix_bh(remac.string)
                    if (remac := _bit.match(tmp_huan)) != None:
                        self.__fix_bit(remac.string)

    def __fix_bit(self, match: str) -> None:
        _nums = re.compile(r'\s([0-9]{1,2})')
        _fixw = re.compile(r'@bit([1-7])$')
        pfix = _fixw.findall(match)
        numx = [int(x, base=10) for x in _nums.findall(match)]
        bit_dict = dict(self.fixrb.get('bit', {}))
        bit_dict.update({f'{pfix[0]}': numx})
        self.fixrb.update({'bit': bit_dict})

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


class formation:
    __dulie: deque
    __maxlen = 15
    __ExNote = Note(n=[1, 2, 3, 4, 5, 6], T=[7])

    @property
    def maxlen(self) -> int:
        return self.__maxlen

    @maxlen.setter
    def maxlen(self, value: int) -> int:
        self.__maxlen = value
        return self.__maxlen

    @property
    def DuLie(self) -> deque:
        return self.__dulie

    def __init__(self, max: int = 15) -> None:
        '''
        max 设置maxlen = 15
        '''
        self.maxlen = max
        self.__dulie = deque([], maxlen=self.maxlen)

    def addNote(self, n: Note) -> int:
        if self.maxlen >= self.DuLie.__len__() >= 0:
            self.DuLie.append(n)
        return self.DuLie.__len__()


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

    @property
    def getlast(self) -> List[int]:
        return self.R[:6]

    @property
    def getabc(self) -> dict:
        '''get {I...II...III}'''
        counter = Counter(self.R)
        counter_list = list(counter.items())
        # 按频率对列表进行排序
        counter_list.sort(key=lambda x: x[1])
        # 计算每个等级的元素数量
        level_size = len(counter_list) // 3
        # 将列表分成三个等级
        level1 = counter_list[:level_size]
        level2 = counter_list[level_size:level_size * 2]
        level3 = counter_list[level_size * 2:]
        return {'I': level1, 'II': level2, 'III': level3}

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
