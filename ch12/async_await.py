#!/usr/bin/env python
# coding: utf-8
"""
Python 为了将语义变得更加明确，就引入了 async 和 await 关键字用来定义原生的协程
"""
import types


async def downloader(url):
    return url + "donw"


@types.coroutine
def Adownloader(url):
    return url + "donw"


async def download_url(url):
    html = await downloader(url)
    html = await Adownloader(url)
    return html


if __name__ == '__main__':
    coro = downloader("http://www.imooc.com")
    coro.send(None)
