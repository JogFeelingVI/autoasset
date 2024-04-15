# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2024-01-06 21:09:15
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-04-15 13:02:56
from aiohttp import web
from app_routes import setup_routes, setup_static_routes
from app_midd import setup_middleware
from app_setting import BASE_DIR
import aiohttp_jinja2, jinja2, asyncio
from codex import pipsub

async def on_shutdown(app):
    """Do not forget to correctly close ThreadPool"""
    app["workers_pool"].shutdown()
    
async def shell(cmd='', sleep=0):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')
    await asyncio.sleep(sleep)
    return sleep


def main():
    def callb(r):
        print(f'web app http://{r}:8080')
        
    pipsub.runscript('./script/ip.sh', callback=callb)
    
    try:
        app = web.Application()
        #print(f'BASE_DIR {BASE_DIR}')
        aiohttp_jinja2.setup(app=app,
                            loader=jinja2.FileSystemLoader(str(BASE_DIR /
                                                                'templates')))
        setup_static_routes(app=app)
        setup_routes(app=app)
        setup_middleware(app=app)
        web.run_app(app=app, host='0.0.0.0', port=8080)
    except :
        print(f'web run app ERROR, use `kill -9 $(lsof -ti tcp:8080)`')
        pipsub.runscript('./script/kill9.sh')
        #asyncio.gather(shell('kill -9 $(lsof -ti tcp:8080)', 3 ))
    

if __name__ == '__main__':
    main()
