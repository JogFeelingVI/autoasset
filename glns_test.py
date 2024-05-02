# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2023-09-22 21:46:48
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-05-02 21:57:33
import time, asyncio
from codex import postcall, tools


def main():
    # TODO 主程序入口
    print('postcall test')
    js = '{"rego":true,"range":1000,"dzx":true,"acvalue":true,"linma":true,"duplicates":true,"sixlan":true,"mod2":true,"mod3":true,"dx16":true,"zhihe":true,"jmsht":true}'
    p = postcall
    p.initPostCall()
    p.instal_json(js=js)
    p.tasks_progress_rate_new()
    for k, v in p.toDict().items():
        n, t = v
        print(f'[{k:>3}] {n} + {t}')
        

if __name__ == "__main__":
    main()
