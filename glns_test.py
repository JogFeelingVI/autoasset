# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-22 21:46:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-21 21:49:11
import pathlib
from Codex import datav, glns_v2
from Codex.md import markdown


def Test_main():
    cdic = datav.LoadJson().toLix
    rb = glns_v2.random_rb(cdic['R'], 6)
    for x in range(1000):
        rb.get_number()
        print(f'dep {rb.dep}')


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
    main()
