# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-22 21:46:48
# @Last Modified by:   Your name
# @Last Modified time: 2024-01-03 23:29:10
import time
from codex import datav, glns_v2, rego_v3, md, note, ospath


def main():
    # TODO 主程序入口
    print('glns test')
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
    # to md file
    _mdf = md.markdown()
    mdx = []
    for x in duLie.queuestr():
        if x == '-':
            mdx.append(_mdf.Dividing_line())
        elif x == '+':
            mdx.append(_mdf.plan(f'{duLie.DuLie.pop()}', 'x'))
            readme_path = ospath.findAbsp.file_path('./glns_test.md')
            with open(readme_path, mode='w') as wMd:
                for line in mdx:
                    wMd.write(f'{line}\n')


if __name__ == "__main__":
    main()
