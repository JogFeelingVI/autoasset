# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-05-15 20:22:04
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-02-17 12:11:43

import re, json
from datetime import datetime as dtime
from typing import List
from codex import gethtml, ospath, datav, md, postcall


class assetx:
    error: bool = False
    
    def getnetdate(self):
        try:
            asset_json = ospath.findAbsp.file_path('./DataFrame.json')
            if asset_json == '':
                print(f'DataFrame is not Finder')
                return
            #nat_dev = 'https://chart.cp.360.cn/kaijiang/ssq'
            url = 'https://www.cjcp.cn/zoushitu/cjwssq/hqaczhi.html'
            self.Lix = gethtml.toDict(gethtml.get_html(url).neirong)
            json_str = json.dumps(self.Lix)
            with open(asset_json, 'w') as datajson:
                datajson.write(json_str)
                hszie = json_str.__sizeof__()
                print(f'updata network data sizeof {hszie}')
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
            js = '{"rego":true,"acvalue":true,"dx16":true,"mod2":true,"mod3":true,"mod4":true,"mod5":true,"mod6":true,"mod7":true,"sixlan":true,"zhihe":true}'
            p = postcall.postcallforjson()
            p.instal_json(js=js)
            rejs = p.todict()
            f = lambda x: ' '.join([f"{n:02}" for n in x])
            # glnsN = glns.glnsMpls(self.Lix)
            for k, v in rejs.items():
                n, t = v
                kn = k+1
                items = f'{f(n)} + {f(t)}'
                print(f'[{kn:>3}] {items}')
                markdown.append(_mdf.plan(f'{items}', 'x'))
                if (kn) % 5 == 0 and kn != p.length:
                    print('')
                    markdown.append(_mdf.Dividing_line())
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
