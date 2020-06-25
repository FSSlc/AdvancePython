#!/usr/bin/env python
# coding: utf-8
"""
使用多线程：在协程中集成阻塞 io
"""
import asyncio
import socket
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse


def get_url_data(url):
    # 通过 socket 请求 html 数据
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # 建立 socket 连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))

    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    print(data)
    client.close()


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    tasks = []
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        task = loop.run_in_executor(executor, get_url_data, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print('last time: {}'.format(time.time() - start_time))
