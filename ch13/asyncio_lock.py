#!/usr/bin/env python
# coding: utf-8
"""
如果函数中没有需要同步，asyncio 可以不用锁
"""
import asyncio

total = 0


async def add():
    global total
    for i in range(1000000):
        total += 1


async def desc():
    global total
    for i in range(1000000):
        total -= 1


if __name__ == '__main__':
    tasks = [add(), desc()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(total)
