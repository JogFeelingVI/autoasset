# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-22 21:46:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-10-10 10:20:20
from Codex import datav, glns_v2


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
            return


if __name__ == "__main__":
    main()
