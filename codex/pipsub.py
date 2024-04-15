# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-04-15 08:48:00
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-04-15 12:52:49

import subprocess, pathlib
from typing import List, Callable

            
def runscript(scriptname:str, callback:Callable=lambda x:x):
    _script = pathlib.Path(scriptname)
    if _script.exists():
        result = subprocess.run(["sh", _script], capture_output=True, text=True)
        # 打印脚本输出
        std = [result.stderr.strip(), result.stdout.strip(), result.returncode]
        # print(f'{std = }')
        # std = ['kill: usage: kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]', 'ok', 0]
        # std = ['', 'ok', 0]
        match std:
            case ['', out, 0]:
                print(f'The execution of `{_script}` is completed as expected.')
                try:
                    callback(out)
                except:
                    print(f'callblack execution failed.')
            case [err, out, 0] :
                print(f'`{_script}` error: {err}')
    else:
        print(f'{_script} does not exist, please check the directory...')
        



def main():
    #runscript('kill9.sh')
    runscript('./script/netaddress.sh')
    # port = 8080
    # pids = get_pid_by_port(port)
    # for pid in pids:
    #     print(f"端口 {port} 被进程 {pid} 占用")


if __name__ == "__main__":
    main()
