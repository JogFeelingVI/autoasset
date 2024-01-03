# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-15 20:22:04
# @Last Modified by:   Your name
# @Last Modified time: 2024-01-03 23:29:48

import re, json
from datetime import datetime as dtime
from typing import List
from codex import gethtml, ospath, glns_v2, md, datav, rego_v3, note


class assetx:
    error: bool = False

    @staticmethod
    def anyishtml_N(text: str) -> list:
        if text != '':
            Rx = re.findall(r'>([0-9,]{17})<', text)
            Bx = re.findall(r'c_bule\">([0-9]{2})<', text)

            return [Rx, Bx]
        return []

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
            asset_json = ospath.findAbsp.file_path('./DataFrame.json')
            if asset_json == '':
                print(f'Asset is not Finder')
                return
            #nat_dev = 'https://chart.cp.360.cn/kaijiang/ssq'
            nat_dev = 'https://www.cjcp.cn/zoushitu/cjwssq/hqaczhi.html'
            html_content = gethtml.get_html(nat_dev).neirong

            if html_content != '':
                Rx, Bx = self.anyishtml_N(html_content)
                self.Lix = {
                    'R': [int(x, base=10) for r in Rx for x in r.split(',')],
                    'B': [int(x, base=10) for x in Bx],
                    'date': dtime.now().__str__()
                }

                json_str = json.dumps(self.Lix)
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
            readme_md = ospath.findAbsp.file_path('./README.md')
            if readme_md == '':
                return
            markdown.append(_mdf.title('Auto update DataFrame.json', 2))
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
            cdic = datav.LoadJson().toLix
            glns = glns_v2.glnsMpls(cdic, 6, 1, 'c')
            duLie = glns_v2.formation(max=25)
            filters = glns_v2.filterN_v2()
            reeego = rego_v3.Lexer().pares(rego_v3.load_rego_v2())
            filters.Lever = glns.getabc
            filters.Last = glns.getlast
            count = 0
            while True:
                _n = glns.producer['r']()
                _t = glns.producer['b']()
                n = note.Note(_n, _t)

                rxfil = True
                for k, func in filters.filters.items():
                    if func(n) == False:
                        rxfil = False
                        #print(f'key {k} is False')
                        break

                for k, f in reeego.items():
                    if f(n) == False:
                        rxfil = False
                        break
                if rxfil:
                    duLie.addNote(n=n)
                    count += 1
                    print(f'[{count:^4}]: {n}')

                if count >= duLie.maxlen:
                    break
            # glnsN = glns.glnsMpls(self.Lix)
            for x in duLie.queuestr():
                if x == '-':
                    markdown.append(_mdf.Dividing_line())
                elif x == '+':
                    markdown.append(_mdf.plan(f'{duLie.DuLie.pop()}', 'x'))
            readme_path = ospath.findAbsp.file_path(readme_md)
            with open(readme_path, mode='w') as wMd:
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
