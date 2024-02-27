# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-22 21:46:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-02-27 22:42:50
import time, asyncio
from codex import postcall, tools


def main():
    # TODO 主程序入口
    print('postcall test')
    js = '{"rego":true,"acvalue":true,"dx16":true,"mod2":true,"mod3":true,"mod4":true,"mod5":true,"mod6":true,"mod7":true,"sixlan":true,"zhihe":true,"lianhao":true}'
    p = postcall
    p.initPostCall()
    p.instal_json(js=js)
    p.manufacturingQueue()
    for k, v in p.todict().items():
        n, t = v
        print(f'[{k:>3}] {n} + {t}')
        
def async_main():
    # TODO 主程序入口
    print('tasks multiprocessing test')
    js = '{"rego":true,"acvalue":true,"dx16":true,"mod2":true,"mod3":true,"mod4":true,"mod5":true,"mod6":true,"mod7":true,"sixlan":true,"zhihe":true,"lianhao":true}'
    p = postcall
    p.initPostCall()
    p.instal_json(js=js)
    p.setting_length(1000)
    p.tasks_multiprocessing()
    for k, v in p.todict().items():
        n, t = v
        print(f'[{k:>3}] {n} + {t}')


if __name__ == "__main__":
    async_main()
