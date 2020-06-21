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
    get_url_data('http://www.baidu.com')
