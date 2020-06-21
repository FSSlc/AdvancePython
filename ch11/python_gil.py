#!/usr/bin/env python
# coding: utf-8

"""
GIL global interpreter lock (CPython)
Python 中一个线程对应于 C 语言中的一个线程
GIL 使得同一时刻只有一个线程在一个 cpu 上执行字节码
无法将多个线程映射到多个 cpu 上

GIL 会根据执行的字节码行数以及时间片释放 GIL，还会在 io 操作时释放 GIL
"""
import dis
import threading


def add(a):
    a = a + 1
    return a


print(dis.dis(add))

total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)
