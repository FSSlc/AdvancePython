#!/usr/bin/env python
# coding: utf-8

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 8000))
server.listen()
sock, addr = server.accept()
# 获取从客户端获取的数据,一次获取 1K 的数据
data = sock.recv(1024)
print(data.decode('utf8'))
sock.send('hello {}'.format(data.decode('utf8')).encode('utf8'))
sock.close()
server.close()
