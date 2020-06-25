#!/usr/bin/env python
# coding: utf-8
"""
示例 asyncio 的 call_soon call_later call_at call_soon_threadsafe
"""
import asyncio


def callback(sleep_time):
    print('sleep {} success'.format(sleep_time))


def stop_loop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    now = loop.time()

    loop.call_at(now + 2, callback, 2)
    loop.call_later(now + 1, callback, 1)
    loop.call_later(now + 3, callback, 3)

    # loop.call_later(2, callback, 2)
    # loop.call_later(1, callback, 1)
    # loop.call_later(3, callback, 3)

    # loop.call_soon(callback, 2)
    # loop.call_soon(stop_loop, loop)  # 停止对普通函数的调用
    loop.call_soon(callback, 4)
    loop.run_forever()
