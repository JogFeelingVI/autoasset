# @Author: JogFeelingVi 
# @Date: 2023-05-26 18:16:42 
# @Last Modified by:   By JogFeelingVi 
# @Last Modified time: 2023-05-26 18:16:42
import pathlib, json
from typing import List

class data_visualization:
    '''
    data visualization
    '''
    def __init__(self, Lix:dict) -> None:
        if LoadJson.verify(Lix=Lix):
            self.Lix = Lix
    
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
    def __init__(self) -> None:
        asset_json = pathlib.Path('asset.json')
        if asset_json.exists():
            with asset_json.open(mode='r', encoding='utf-8') as jsfile:
                Lix = json.load(jsfile)
                if self.verify(Lix=Lix):
                    self.Lix = Lix
    
    @staticmethod
    def verify(Lix:dict) -> bool:
        isrex = set([1, 0][x in 'RBdate'] for x in Lix.keys())
        return [False, True][sum(isrex)!=0]
                
            
if __name__ == '__main__':
    ljson = LoadJson()