#!/usr/bin/env python
# coding: utf-8

import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 8000))
server.listen()


def handle_sock(sock, addr):
    # 获取从客户端获取的数据,一次获取 1K 的数据
    while True:
        data = sock.recv(1024)
        print("addr = ", addr, "data = ", data.decode('utf8'))
        re_data = input()
        sock.send(re_data.encode('utf8'))
    sock.close()


# 获取从客户端获取的数据,一次获取 1K 的数据
while True:
    sock, addr = server.accept()
    # 用线程来处理新接收的连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

server.close()
