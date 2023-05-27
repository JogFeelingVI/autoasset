# @Author: JogFeelingVi
# @Date: 2023-05-26 18:16:42
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-26 22:40:24
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
        r = self.Lix['R'][:6]
        b = self.Lix['B'][0]
        r_str = ' '.join([f'{x:02}' for x in r])
        return f'{r_str} / {b:02}'

    def groupBysix(self) -> List[str]:
        data = self.Lix.get('R', [])
        groups = [data[i:i + 6] for i in range(0, len(data), 6)]
        groups = groups[::-1]
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
    print(datav.frequency('R'))