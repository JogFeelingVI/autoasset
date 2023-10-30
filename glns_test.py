# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-22 21:46:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-31 05:59:17
import pathlib
import time
from Codex import datav, glns_v2, rego, md


def Test_main():
    N = glns_v2.Note([4, 15, 18, 20, 24, 28], T=7)
    print(f'Note {N}')
    # _rego = rego.rego()
    # _rego.debug = True
    # _rego.parse()
    # _rego.filtration(N)


def main():
    print('glns test')
    cdic = datav.LoadJson().toLix
    glns = glns_v2.glnsMpls(cdic=cdic)
    duLie = glns_v2.formation(max=25)
    filters = glns_v2.filterN_v2()
    reeego = rego.rego()
    reeego.parse_v2()
    filters.Lever = glns.getabc
    filters.Last = glns.getlast

    count = 0
    while True:
        n = glns.creativity()
        rxfil = [f(n) for _, f in filters.filters.items()]
        if False not in rxfil:
            if reeego.filtration(n):
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
            readme_path = pathlib.Path('./test.md')
            with readme_path.open(mode='w') as wMd:
                for line in mdx:
                    wMd.write(f'{line}\n')


if __name__ == "__main__":
    main()
