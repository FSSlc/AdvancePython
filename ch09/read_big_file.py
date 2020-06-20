#!/usr/bin/env python
# coding: utf-8

def my_readlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            # 消除一次读取多行
            buf = buf[pos + len(newline):]
        chunk = f.read(4096)

        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk


with open("input.txt") as f:
    for line in my_readlines(f, "|"):
        print(line)
