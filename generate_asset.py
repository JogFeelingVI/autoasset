# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-15 20:22:04
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-05-26 21:48:25
from operator import ge
from pickletools import markobject
import re, json
from datetime import datetime as dtime
from typing import List
from Codex import gethtml, pathliab, glns, md, datav


class assetx:
    error: bool = False

    @staticmethod
    def anyishtml(text: str) -> list:
        if text in ['', None]:
            return []
        pattern = re.compile(r'<tr[^>]*>(.*?)</tr>', re.DOTALL)
        match = pattern.findall(text)
        Rx = []
        Bx = []
        if match:
            for _match in match:
                td = re.compile(r'<td>[\d]{7}</td>')
                if td.findall(_match):
                    num_r = re.compile(r'ball_5\'>([\d]{2})</span')
                    numsr = num_r.findall(_match)
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

    def tomd(self):
        try:
            if self.error:
                return
            _mdf = md.markdown()
            _datav = datav.data_visualization(self.Lix)
            markdown = []
            readme_md = pathliab.ospath.file_path('./README.md')
            if readme_md == '':
                return
            markdown.append(_mdf.title('Auto update asasset.json', 2))
            markdown.append(
                _mdf.unordered_list(f'update {self.Lix.get("date", "None")}'))
            markdown.append(
                _mdf.unordered_list(
                    f'Black box number {_mdf.ltalic(_datav.showlastnumber())}')
            )
            matrix = _datav.groupBysix()
            markdown.append(_mdf.title('Sequence graphics', 4))
            for i, row in enumerate(matrix):
                markdown.append(_mdf.unordered_list(f'{i+1:02}: {row}'))
            markdown.append(_mdf.title('Creativity list', 2))
            glnsN = glns.glnsMpls(self.Lix)
            for x in glns.splitqueue.queuestr():
                if x == '□':
                    markdown.append(_mdf.Dividing_line())
                elif x == '■':
                    markdown.append(_mdf.plan(f'{glnsN.creativity()}', 'x'))
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
