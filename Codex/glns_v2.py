# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-21 21:14:47
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-12-06 11:56:55

from collections import Counter, deque
import itertools, random, math
from typing import Any, List

def mod_old(n: List, m: int):
    ''' mod ? m = 2 3 4 5 6'''
    f = lambda x: x % m
    s = sorted(n, key=f)
    gby = itertools.groupby(s, key=f)
    
    # sorted([len(list(g[1])) for g in gby])
    return [list(v).__len__() for g, v in gby]


def mod(n: List, m: int):
    ''' mod ? m = 2 3 4 5 6  group (1, [1,2,3])'''
    f = [x % m for x in n]
    s = sorted(f)
    gby = itertools.groupby(s)
    return [list(v).__len__() for g, v in gby]


def Range_M(M: int = 16) -> List:
    '''
    M is 33 or 16
    修复 R B 中缺失的数字
    '''
    max_set = [x for x in range(1, M + 1)]
    return max_set


class Note:
    __set_r = None
    __set_b = None

    def __init__(self, n: List[int], T: List[int] | int) -> None:
        """Note
        Args:
            n (List[int]): 1-33 红色号码球
            T (List[int] | int): 1-16 蓝色号码球
        """
        _T = [T, [T]][isinstance(T, int)]
        self.number = sorted(n)
        self.tiebie = sorted(_T)

    def index(self, i: int) -> int:
        return self.number[i - 1]

    @property
    def setnumber_R(self):
        if self.__set_r == None:
            self.__set_r = set(self.number)
        return self.__set_r

    @property
    def setnumber_B(self):
        if self.__set_b == None:
            self.__set_b = set(self.tiebie)
        return self.__set_b

    def __str__(self) -> str:
        n = ' '.join([f'{num:02d}' for num in self.number])
        t = ' '.join([f'{num:02d}' for num in self.tiebie])
        return f'{n} + {t}'


class filterN_v2:
    ''' 对Note进行过滤 '''
    filters = {}

    __Lever = {}
    __Last = [0, 0, 0, 0, 0, 0]
    __debug = False

    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, value: bool) -> None:
        self.__debug = value
        self.__init__filters()

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

    def __init__filters(self) -> None:
        self.filters = {
            'sixlan': self.sixlan,  #
            'dx16': self.dx16,
            'zhihe': self.zhihe,
            'duplicates': self.duplicates,  #
            'linma': self.linma,  #
            'dzx': self.dzx,
            'lianhao': self.lianhao,
            'ac': self.acvalue,
            'mod2': self.mod2,
            'mod3': self.mod3,
            'mod4': self.mod4,
            'mod5': self.mod5,
            'mod6': self.mod6,
            'mod7': self.mod7,
            'denji': self.denji,  #
        }

        if self.__debug == False:
            #diskey = ['sixlan', 'denji']
            diskey = [
                #'sixlan',
                #'duplicates',
                'denji',
            ]
            for k in diskey:
                self.filters.pop(k)

    def __init__(self) -> None:
        self.__init__filters()

    def dzx(self, N: Note) -> bool:
        '''xiao zhong da'''
        g = [range(i, i + 11) for i in range(0, 33, 11)]
        countofg = map(lambda x: N.setnumber_R.intersection(x).__len__(), g)
        return [False, True][5 not in countofg or 6 in countofg]

    def acvalue(self, N: Note) -> bool:
        '''计算数字复杂程度 默认 P len = 6 这里操造成效率低下'''
        p = itertools.product(N.number[1::], N.number[0:5])
        ac = [1 for a, b in p if a - b > 0.1].__len__() - 1 - len(N.number)
        return [False, True][ac >= 4]

    def linma(self, N: Note) -> bool:
        '''计算临码'''
        # plus_minus = []

        # for n in N.setnumber_R:
        #     if n + 1 in self.Last or n - 1 in self.Last:
        #         plus_minus.append(n)
        # return [False, True][plus_minus.__len__() in (0, 1, 2, 3)]
        plus_minus = 0
        for n in N.setnumber_R:
            if n + 1 in self.Last or n - 1 in self.Last:
                plus_minus += 1
                if plus_minus > 3.5:
                    return False
        return True

    def duplicates(self, N: Note) -> bool:
        '''计算数组是否有重复项目'''
        duplic = N.setnumber_R & set(self.Last)
        return [False, True][duplic.__len__() in (0, 1, 2)]

    def sixlan(self, N: Note) -> bool:
        '''判断红色区域是否等于 1, 2, 3, 4, 5, 6, 7'''
        rb = [False, True][max(N.setnumber_R) != 6]
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

    def mod3(self, n: Note) -> bool:
        '''mod 3 not in [[6], [5,1],[3,3]]'''
        cts = [[6], [5, 1]]
        counts = sorted(mod(n.number, 3))
        if counts in cts:
            return False
        return True
    
    def mod4(self, n:Note) ->bool:
        counts = mod(n.number, 4)
        if max(counts) > 4.01:
            return False
        return True

    def mod2(self, n: Note) -> bool:
        '''mod 2 not in [[6], [5,1],[3,3]]'''
        cts = [[6], [5, 1]]
        counts = sorted(mod(n.number, 2))
        if counts in cts:
            return False
        return True

    def mod5(self, n: Note) -> bool:
        '''mod 5 not in [[6], [5,1],[3,3]]'''
        cts = [4, 5, 6]
        counts = max(mod(n.number, 5))
        if counts in cts:
            return False
        return True

    def mod6(self, n: Note) -> bool:
        '''mod 5 not in [[6], [5,1],[3,3]]'''
        cts = [4, 5, 3]
        counts = len(mod(n.number, 6))
        if counts not in cts:
            return False
        return True

    def mod7(self, n: Note) -> bool:
        '''mod 5 not in [[6], [5,1],[3,3]]'''
        cts = [4, 5, 3, 6]
        counts = len(mod(n.number, 7))
        if counts not in cts:
            return False
        return True

    def dx16(self, n: Note) -> bool:
        '''
        da:xiao 1:5 n > 16.02 is da
        '''
        f = lambda x: x > 16.02
        cts = [[6], [0]]
        s = sorted(n.number, key=f)
        modg = itertools.groupby(s, key=f)
        counts = sorted([len(list(g[1])) for g in modg])
        if counts in cts:
            return False
        return True

    def zhihe(self, n: Note) -> bool:
        '''
        da:xiao 1:5 n > 16.02 is da
        '''
        f = lambda x: x in (1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
        cts = [[6], [0]]
        s = sorted(n.number, key=f)
        modg = itertools.groupby(s, key=f)
        counts = sorted([len(list(g[1])) for g in modg])
        if counts in cts:
            return False
        return True

    def denji(self, N: Note) -> bool:
        '''
        这个方法会造成命中率降低弃用
        [(4, 1), (20, 3), (7, 3), (23, 3), (21, 3), (2, 4), (29, 4), (28, 4), (5, 4), (12, 4), (17, 4)]
        '''
        if self.Lever.keys().__len__() == 0:
            return True
        Levers = map(lambda x: [i[0] for i in x], self.Lever.values())
        Rexts = map(lambda x: N.setnumber_R.intersection(x).__len__(), Levers)
        if 0 in Rexts:
            return False
        return True


class formation:
    __dulie: deque
    __maxlen = 15

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

    def queuestr(self) -> str:
        '''
            gsize group size = 5 
            n gsize * n
            +++++-+++++-+++++-+++++-+++
        '''
        temps = ['+'] * self.maxlen
        temps_group = [
            ''.join(temps[i:i + 5]) for i in range(0, self.maxlen, 5)
        ]
        return '-'.join(temps_group)

    def __init__(self, max: int = 15) -> None:
        '''
        max 设置maxlen = 15
        '''
        self.maxlen = max
        self.__dulie = deque([], maxlen=self.maxlen)

    def addNote(self, n: Note) -> int:
        try:
            self.DuLie.append(n)
            return self.DuLie.__len__()
        except:
            return -1


class random_rb:
    '''random R & B'''

    def __init__(self, rb: List, L: int) -> None:
        self.len = L
        self.nPool = rb

    def get_number_v2(self):
        dep = sorted(random.sample(self.nPool, k=self.len))
        return dep


class glnsMpls:
    '''glns mpls'''

    _rlen = 6
    _blen = 1

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
        return self.R[-6:]

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
            self.R = cdic.get('R', [])
            self.B = cdic.get('B', [])
            if self.R != None and self.B != None:
                self.groupby = [
                    self.R[i:i + 6] for i in range(0, len(self.R), 6)
                ]
                self.random_r = random_rb(Range_M(M=33), self.rLen)
                self.random_b = random_rb(Range_M(M=16), self.bLen)
            # print(f'glns init done')

    def creativity(self) -> tuple[list[int], list[int]]:
        '''产生号码'''
        #get_r = random_rb(self.FixR, self.rLen)
        # N = Note()
        while 1:
            r = self.random_r.get_number_v2()
            if self.cosv(N=r) > 0.9:
                return (r, self.random_b.get_number_v2())
        return ([0] * 6, [0])

    def cosv(self, N: List) -> float:
        dot = sum(a * b for a, b in zip(N, self.getlast))
        normx = math.sqrt(sum([a * a for a in N]))
        normy = math.sqrt(sum([a * a for a in self.getlast]))
        cos = dot / (normx * normy)
        return cos
