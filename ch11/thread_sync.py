#!/usr/bin/env python
# coding: utf-8

"""
线程同步机制：
1. 使用锁(Lock, RLock)：用锁会影响性能，锁会引起死锁（1. 获取后再获取 2.互相等待）
2. 使用 Condition 条件变量
3. 使用 Semaphore 信号量
RLock: 在同一个线程里面，可以连续调用多次 acquire，但 acquire 和 release 的次数必须相等
"""
import threading
from threading import Lock, RLock

total = 0
lock = Lock()
lock = RLock()


def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


if __name__ == '__main__':
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(total)
