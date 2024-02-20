# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-22 21:46:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-02-20 22:24:23
import time
from codex import postcall


def main():
    # TODO 主程序入口
    print('glns test')
    js = '{"rego":true,"acvalue":true,"dx16":true,"mod2":true,"mod3":true,"mod4":true,"mod5":true,"mod6":true,"mod7":true,"sixlan":true,"zhihe":true,"lianhao":true}'
    p = postcall.postcallforjson()
    p.instal_json(js=js)
    rejs = p.todict()
    f = lambda x: ' '.join([f"{n:02}" for n in x])
    for k, v in rejs.items():
        n, t = v
        print(f'[{k:>3}] {f(n)} + {f(t)}')


if __name__ == "__main__":
    main()
