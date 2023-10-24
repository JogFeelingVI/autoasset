# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-22 21:46:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-24 22:55:00
import pathlib
from Codex import datav, glns_v2, rego
from Codex.md import markdown


def Test_main():
    N = glns_v2.Note([4, 15, 18, 20, 24, 25], T=7)
    _rego = rego.rego()
    _rego.parse()
    _rego.debug = True
    _rego.filtration(N)


def main():
    print("Hello, World!")
    cdic = datav.LoadJson().toLix
    glns = glns_v2.glnsMpls(cdic=cdic)
    duLie = glns_v2.formation(max=25)
    filters = glns_v2.filterN_v2()
    filters.Lever = glns.getabc
    filters.Last = glns.getlast

    count = 0

    while True:
        n = glns.creativity()
        rxfil = [f(n) for _, f in filters.filters.items()]
        if False not in rxfil:
            duLie.addNote(n=n)
            count += 1
            print(f'N {count:>3}: {n}')
        if count >= duLie.maxlen:
            break
    # to md file
    _mdf = markdown()
    md = []
    for x in glns_v2.splitqueue.queuestr(n=5):
        if x == '-':
            md.append(_mdf.Dividing_line())
        elif x == '+':
            md.append(_mdf.plan(f'{duLie.DuLie.pop()}', 'x'))
            readme_path = pathlib.Path('./TEST.md')
            with readme_path.open(mode='w') as wMd:
                for line in md:
                    wMd.write(f'{line}\n')


if __name__ == "__main__":
    Test_main()
