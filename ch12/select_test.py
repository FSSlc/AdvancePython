#!/usr/bin/env python
# coding: utf-8

import socket
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
    # 使用 非阻塞 IO 完成 http 请求
    client.setblocking(False)
    try:
        client.connect((host, 80))  # 阻塞不会消耗 CPU
    except BlockingIOError as e:
        pass

    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf8'))
            break
        except OSError as e:
            pass

    data = b''
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode('utf8')
    print(data)
    client.close()


if __name__ == '__main__':
    get_url_data('http://www.baidu.com')
