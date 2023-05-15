# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-15 20:22:04
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-15 22:21:32
from operator import ge
import re, json
from datetime import datetime as dtime
from time import sleep
from typing import List
from Codex import gethtml, pathliab

class assetx:
    def getnetdate(self):
        try:
            asset_json = pathliab.ospath.file_path('./asset.json')
            if asset_json == '':
                return
            nat_dev = 'https://m.cjcp.cn/zoushitu/cjwssq/hqfgzglclrw.html'
            html_content = gethtml.get_html(nat_dev).neirong
            if html_content != '':
                Rx = re.findall(r'>([0-9,]{17})<', html_content)
                Bx = re.findall(r'c_bule\">([0-9]{2})<', html_content)
                self.Lix = {
                    'R': [int(x) for r in Rx for x in r.split(',')],
                    'B': [int(x) for x in Bx],
                    'date': dtime.now().__str__()
                }
                
                json_str = json.dumps(self.Lix, indent=0)
                with open(asset_json, 'w') as datajson:
                    datajson.write(json_str)
                    hszie = json_str.__sizeof__()
                    print(f'updata network data sizeof {hszie}')
            else:
                print(f'updata network error')
        except Exception as e:
            print(f'error: {e}')
    
    @staticmethod      
    def listTostr(lis:list) -> str:
        prompt = '▆'
        if lis.__len__() ==0:
            return 'No Numbers'
        temp_lis = [[i, lis.count(i)] for i in set(lis)]
        temp_sort = sorted(temp_lis, key=lambda x: x[1], reverse=True)
        temp:str = '\n'.join([f' - {n:>02} Count {c:>2} {prompt * c}' for n, c in temp_sort])
        return temp
    
    def shownumber(self) -> str:
        r =self.Lix['R'][-6::]
        b =self.Lix['B'][-1]
        r_str = ' '.join([f'{x:02}' for x in r])
        return f'*{r_str} / {b:02}*'
            
    def tomd(self):
        try:
            markdown = []
            readme_md = pathliab.ospath.file_path('./README.md')
            if readme_md == '':
                return
            markdown.append('## Auto update asasset.json')
            markdown.append(f' - update {self.Lix.get("date", "None")}')
            markdown.append(f'### Black box number {self.shownumber()}')
            markdown.append('#### Red ball list')
            markdown.append(f'{self.listTostr(self.Lix.get("R", []))}')
            markdown.append('#### Blue ball list')
            markdown.append(f'{self.listTostr(self.Lix.get("B", []))}')
            readme_path = pathliab.Path(readme_md)
            with readme_path.open(mode='w') as wMd:
                for line in markdown:
                    wMd.write(f'{line}\n')
        except:
            print(f'An exception occurred while writing readme.md')

def main():
    assx = assetx()
    assx.getnetdate()
    assx.tomd()


if __name__ == "__main__":
    main()
