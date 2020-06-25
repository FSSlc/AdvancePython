#!/usr/bin/env python
# coding: utf-8
"""
事件循环 + 回调（驱动生成器） + IO 多路复用
asyncio 是 Python 用于解决异步 io 编程的一整套解决方案
tornado gevent twisted（scrapy django channels）
tornado（实现了 web 服务器）
django flask （uwsgi gunicorn nginx）
tornado 可以直接部署 nginx + tornado
使用 asyncio
"""

import asyncio
import time


async def get_html(url):
    print("start get url")
    # 下面 sleep 这句不能使用 time.sleep(2) 替代, 阻塞函数不要写在协程里面！
    # await 后面跟一个 awaitable 的对象
    await asyncio.sleep(2)
    # time.sleep(2)
    print("end get url")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print('time elapse {} s'.format(time.time() - start_time))
