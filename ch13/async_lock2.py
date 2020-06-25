#!/usr/bin/env python
# coding: utf-8
"""
如果函数中没有需要同步，asyncio 可以不用锁
"""
from asyncio import Lock

import aiohttp

lock = Lock()
cache = {}


async def get_stuff(url):
    # 下面这句实现了 __aenter__ __await__
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff


async def parse_stuff():
    stuff = await get_stuff()
    # do some parsing


async def use_stuff():
    stuff = await get_stuff()
    # use stuff to do someing interesting
