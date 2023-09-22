# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-22 21:46:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2023-09-22 21:49:52
from Codex import datav, glns_v2


def main():
    print("Hello, World!")
    cdic = datav.LoadJson().toLix
    glns = glns_v2.glnsMpls(cdic=cdic)
    print(f'glns {glns.creativity()}')


if __name__ == "__main__":
    main()
