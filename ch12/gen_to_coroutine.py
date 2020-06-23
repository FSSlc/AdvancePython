#!/usr/bin/env python
# coding: utf-8

import inspect
import socket


def gen_func():
    value = yield 1
    # 第一返回值给调用方，第二调用值通过 send 方式返回值给 gen
    return "user"

# 用同步的方式编写异步的代码，在适当的时候暂停函数并在适当的时候启动函数
def get_socket_data():
    yield 'user'


def downloader(url):
    # 协程的调度依然是 事件循环 + 协程模式
    # 协程是单线程模式
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    host = '1.1.1.1'
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass

    source = yield from get_socket_data()

    data = source.decode('utf8')
    print(data.split('\r\n\r\n')[1])


def download_html(html):
    html = yield from downloader()


if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))
