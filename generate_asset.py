# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-15 20:22:04
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-20 22:08:46
from operator import ge
from pickletools import markobject
import re, json
from datetime import datetime as dtime
from typing import List
from Codex import gethtml, pathliab, glns


class assetx:
    error:bool = False
    
    @staticmethod
    def anyishtml(text:str) -> list:
        if text in ['', None]:
            return []
        pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL)
        match = pattern.findall(text)
        Rx =[]
        Bx =[]
        if match:
            for _match in match:
                td = re.compile(r'<td>[\d]{7}</td>')
                if td.findall(_match):
                    num_r = re.compile(r'ball_5\'>([\d]{2})</span')
                    numsr  = num_r.findall(_match)
                    num_b = re.compile(r'ball_1\'>([\d]{2})<span')
                    numob = num_b.findall(_match)
                    Rx.extend(numsr)
                    Bx.extend(numob)
        return [Rx, Bx]
    
    def getnetdate(self):
        try:
            asset_json = pathliab.ospath.file_path('./asset.json')
            if asset_json == '':
                return
            nat_dev = 'https://chart.cp.360.cn/kaijiang/ssq'
            html_content = gethtml.get_html(nat_dev).neirong
            
            
            if html_content != '':
                # Rx = re.findall(r'>([0-9,]{17})<', html_content)
                # Bx = re.findall(r'c_bule\">([0-9]{2})<', html_content)
                Rx, Bx = self.anyishtml(html_content)
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
            self.error = True
    
    @staticmethod      
    def listTostr(lis:list) -> str:
        prompt = '█'
        if lis.__len__() ==0:
            return 'No Numbers'
        temp_lis = [[i, lis.count(i)] for i in set(lis)]
        temp_sort = sorted(temp_lis, key=lambda x: x[1], reverse=True)
        temp:str = '\n'.join([f' - {n:>02} Count {c:>2} {prompt * c}' for n, c in temp_sort])
        return temp
    
    def shownumber(self) -> str:
        r = self.Lix['R'][:6]
        b = self.Lix['B'][0]
        r_str = ' '.join([f'{x:02}' for x in r])
        return f'*{r_str} / {b:02}*'
    
    def groupBysix(self) ->List[str]:
        data = self.Lix.get('R', [])
        groups = [data[i:i + 6] for i in range(0, len(data), 6)]
        matrix = []
        
        for i in range(1, 34):
            row = ''
            for g in groups:
                if i in g:
                    row += '█'
                else:
                    row += '-'
            matrix.append(row)

        # for group in groups:
        #     row = ''
        #     for i in range(1, 34):
        #         if i in group:
        #             row += '█'
        #         else:
        #             row += '░'
        #     matrix.append(row)
        return matrix
        # for i, row in enumerate(matrix):
        #     print(f"Row {i + 1:>2}: {row}")

            
    def tomd(self):
        try:
            if self.error:
                return
            markdown = []
            readme_md = pathliab.ospath.file_path('./README.md')
            if readme_md == '':
                return
            markdown.append('## Auto update asasset.json')
            markdown.append(f' - update {self.Lix.get("date", "None")}')
            markdown.append(f'### Black box number {self.shownumber()}')
            matrix = self.groupBysix()
            markdown.append('#### Sequence graphics')
            for i, row in enumerate(matrix):
                markdown.append(f' - Row {i+1:02} {row}')
            # markdown.append('#### Red ball list')
            # markdown.append(f'{self.listTostr(self.Lix.get("R", []))}')
            # markdown.append('#### Blue ball list')
            # markdown.append(f'{self.listTostr(self.Lix.get("B", []))}')
            markdown.append('## creativity list')
            for x in (0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ,0,1,0,0,0,0,0,1,0,0,0,0,0):
                if x == 1:
                    markdown.append('---')
                else:
                    markdown.append(f'- [x] {glns.glnsMpls(self.Lix).creativity()}')
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
    assx.groupBysix()


if __name__ == "__main__":
    main()
