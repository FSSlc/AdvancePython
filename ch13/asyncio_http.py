#!/usr/bin/env python
# coding: utf-8
"""
当前 asyncio 没有提供 http 协议的接口，可以借助 aiohttp
"""
import asyncio
import time
from urllib.parse import urlparse


async def get_url_data(url):
    # 通过 socket 请求 html 数据
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立 socket 连接
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode('utf8')
        all_lines.append(data)
    html = "\n".join(all_lines)
    return html


async def main():
    tasks = []
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        tasks.append(asyncio.ensure_future(get_url_data(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('last time: {}'.format(time.time() - start_time))
