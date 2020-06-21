#!/usr/bin/env python
# coding: utf-8
"""
使用 select 完成 http 请求

通过非阻塞 IO 实现 http 请求
select + 回调 + 事件循环：
并发性高
使用单线程
"""

import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from urllib.parse import urlparse

selector = DefaultSelector()
urls = []
stop = False


# 使用类可以方便地访问回调前的数据
class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode('utf8'))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode('utf8')
            html_data = data.split("\r\n\r\n")[1]
            print(data, html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        # 通过 socket 请求 html 数据
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b''
        if self.path == "":
            self.path = "/"

        # 建立 socket 连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 使用 非阻塞 IO 完成 http 请求
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗 CPU
        except BlockingIOError as e:
            pass

        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # 事件循环，不停地请求 socket 的状态并调用调用对应的回调函数
    # 回调 + 事件循环 + select(pool eppol)
    # 1. select 本身不支持 register 模式
    # 2. socket 状态变化以后的回调是由程序员完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)


if __name__ == '__main__':
    fetcher = Fetcher()
    import time

    started_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print(time.time() - started_time)
