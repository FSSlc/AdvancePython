#!/usr/bin/env python
# coding: utf-8
"""
asyncio 获取协程的返回值，添加 callback
wait 和 gather 的区别
"""

import asyncio
import time
from functools import partial


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


def callback(url, future):
    # 一个函数回调
    print('url = '.format(url))
    print('send mail to lc')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 本质上下面这句也会创建 task，与它下面的那句作用一致
    # get_future = asyncio.ensure_future(get_html("http://www.imooc.com"))
    task = loop.create_task(get_html("http://www.imooc.com"))
    # 有额外参数的话，使用 partial 包裹函数，参数在前
    task.add_done_callback(partial(callback, "http://www.imooc.com"))
    loop.run_until_complete(task)
    print('time elapse {} s'.format(time.time() - start_time))

    # gather 演示
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html('http://www.baidu.com') for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    # loop.run_until_complete(asyncio.gather(*tasks))
    print('time elapse {} s'.format(time.time() - start_time))

    # gather 和 wait 的区别
    # gather 更加 high-level 可以将 task 分组
    group01 = [get_html('http://www.baidu.com') for i in range(2)]
    group02 = [get_html('http://www.google.com') for i in range(2)]

    start_time = time.time()
    loop.run_until_complete(asyncio.gather(*group01, *group02))
    group01 = asyncio.gather(*group01)
    group02 = asyncio.gather(*group02)
    # 分组取消任务
    group01.cancel()
    loop.run_until_complete(asyncio.gather(group01, group02))
    print('time elapse {} s'.format(time.time() - start_time))
