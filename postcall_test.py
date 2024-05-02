# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-05-02 20:32:56
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-05-02 21:49:28

import time
from codex import postcall

def main():
    jsonx = '{"rego":true,"range":1000,"dzx":true,"acvalue":true,"linma":true,"duplicates":true,"sixlan":true,"mod2":true,"mod3":true,"dx16":true,"zhihe":true,"jmsht":true}'
    print("Hello, World!")
    start = time.time()
    p = postcall
    p.initPostCall()
    p.instal_json(js=jsonx)
    # p.tasks_futures()
    # rejs = p.toJson()
    # loop.run_in_executor(executor=request.app["workers_pool"], func=p.tasks_progress_rate)
    # tracemalloc.stop()
    p.tasks_progress_rate_new()
    #! todo 这是新的方法
    # asyncio.gather(p.tasks_progress_rate())
    rejs = p.toJson()
    end = time.time() - start
    print(f"postcall is done! {p.interimStorage.keys().__len__()} {end:.2f}")


if __name__ == "__main__":
    main()
