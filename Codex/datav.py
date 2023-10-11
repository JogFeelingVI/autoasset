# @Author: JogFeelingVi
# @Date: 2023-05-26 18:16:42
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-28 08:28:20
import pathlib, json
from typing import List
from collections import Counter


class data_visualization:
    '''
    data visualization
    '''

    def __init__(self, Lix: dict) -> None:
        if LoadJson.verify(Lix=Lix):
            self.Lix = Lix
            self.Three_categories()

    def Three_categories(self) -> dict:
        counter = Counter(self.Lix.get('R', []))
        counter_list = list(counter.items())
        # 按频率对列表进行排序
        counter_list.sort(key=lambda x: x[1])
        # 计算每个等级的元素数量
        level_size = len(counter_list) // 3
        # 将列表分成三个等级
        level1 = counter_list[:level_size]
        level2 = counter_list[level_size:level_size * 2]
        level3 = counter_list[level_size * 2:]
        return {'lv1': level1, 'lv2': level2, 'lv3': level3}

    def frequency(self, key: str) -> List[str]:
        matrix = []
        if key in 'RB':
            prompt = '■'
            lis = self.Lix.get(key, [])
            if lis.__len__() == 0:
                matrix.append('No Numbers')
            temp_lis = Counter(lis)
            temp_sort = temp_lis.most_common()
            for n, c in temp_sort:
                matrix.append(f'{n:>02} Count {c:>2} {prompt * c}')
        else:
            matrix.append('No Numbers')
        return matrix

    def showlastnumber(self) -> str:
        r = self.Lix['R'][-6:]
        b = self.Lix['B'][0 - 1]
        r_str = ' '.join([f'{x:02}' for x in r])
        return f'{r_str} / {b:02}'

    def Comprehensive_chart(self, key: str) -> List[str]:
        matrix = []
        if key in 'RB':
            data = self.Lix.get(key, [])
            if key == 'R':
                columes = [x for x in range(1, 34)]
                groups = [data[i:i + 6] for i in range(0, len(data), 6)]
            else:
                columes = [x for x in range(1, 17)]
                groups = [data[i:i + 1] for i in range(0, len(data), 1)]

            header = "|"
            separator = "|"
            for i in columes:
                header += f" {i} |"
                separator += ":-:|"
            matrix.append(header)
            matrix.append(separator)

            groups = groups[::-1]
            for row in groups:
                s_row = '|'
                for colume in columes:
                    if colume in row:
                        s_row += f'{colume:>02}|'
                    else:
                        s_row += '--|'
                matrix.append(s_row)
                s_row = '|'
        return matrix

    def groupBysix(self) -> List[str]:
        data = self.Lix.get('R', [])
        groups = [data[i:i + 6] for i in range(0, len(data), 6)]
        #groups = groups[::-1]
        matrix = []

        for i in range(1, 34):
            row = ''
            for g in groups:
                if i in g:
                    row += '■'
                else:
                    row += '□'
            matrix.append(row)

        return matrix


class LoadJson:
    '''Load JSON'''
    __Lix = {}

    @property
    def toLix(self) -> dict:
        return self.__Lix

    @toLix.setter
    def toLix(self, value: dict) -> dict:
        if self.verify(value):
            self.__Lix = value
        return self.toLix

    def __init__(self) -> None:
        asset_json = pathlib.Path('asset.json')
        if asset_json.exists():
            with asset_json.open(mode='r', encoding='utf-8') as jsfile:
                Lix = json.load(jsfile)
                if self.verify(Lix=Lix):
                    self.toLix = Lix

    @staticmethod
    def verify(Lix: dict) -> bool:
        isrex = set([1, 0][x in 'RBdate'] for x in Lix.keys())
        return [False, True][sum(isrex) == 0]


if __name__ == '__main__':
    ljson = LoadJson()
    datav = data_visualization(ljson.toLix)
    print(datav.Comprehensive_chart('R'))