# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2024-01-06 21:09:15
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-04-17 09:48:06
from aiohttp import web
from app_routes import setup_routes, setup_static_routes
from app_midd import setup_middleware
from app_setting import BASE_DIR
import aiohttp_jinja2, jinja2, asyncio
from codex import pipsub


async def on_shutdown(app):
    """Do not forget to correctly close ThreadPool"""
    app["workers_pool"].shutdown()


def main():

    retule = pipsub.callBackHandle()

    pipsub.runscript('./script/ip.sh', callback=retule)
    print(f'ipaddress: {retule.retule()}')
    pipsub.runscript('./script/lsof.sh', callback=retule)
    print(f'Find PID: {retule.retule()}')
    if retule.retule() != '':
        pipsub.runscript('./script/kill9.sh')

    try:
        app = web.Application()
        #print(f'BASE_DIR {BASE_DIR}')
        aiohttp_jinja2.setup(app=app,
                             loader=jinja2.FileSystemLoader(
                                 str(BASE_DIR / 'templates')))
        setup_static_routes(app=app)
        setup_routes(app=app)
        setup_middleware(app=app)
        web.run_app(app=app, host='0.0.0.0', port=8080)
    except Exception as e:
        print(f'web run app ERROR, use `kill -9 $(lsof -ti tcp:8080)`')
        pipsub.runscript('./script/kill9.sh')
        #asyncio.gather(shell('kill -9 $(lsof -ti tcp:8080)', 3 ))
        main()


if __name__ == '__main__':
    main()
