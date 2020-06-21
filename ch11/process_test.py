#!/usr/bin/env python
# coding: utf-8
"""
多进程编程：
耗 cpu 的操作用多进程的操作
对于 io 操作来说使用多线程编程
进程切换代价高于线程切换
"""

import functools
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


# 1. 耗费 cpu 的操作，多进程优于多线程，
# 但如果使用了 lru 缓存后，多线程会快一点
@functools.lru_cache(None)
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def calc(e):
    # 具体的计算逻辑
    start_time = time.time()

    print('结果乱序')
    all_task = [e.submit(fib, num) for num in range(25, 40)]
    for future in as_completed(all_task):
        data = future.result()
        print('exe result: {}'.format(data))
    print('结果顺序')
    for data in e.map(fib, range(90, 100)):
        print('exe result: {}'.format(data))

    print("last time is: {}".format(time.time() - start_time))


# 2. 对于 io 操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n


def sleep_test(e):
    # 具体的计算逻辑
    start_time = time.time()
    for data in e.map(random_sleep, [2] * 30):
        print('sleep result: {}'.format(data))
    print("last time is: {}".format(time.time() - start_time))


if __name__ == '__main__':
    with ThreadPoolExecutor(8) as e:
        calc(e)
        print('=' * 100)
        sleep_test(e)

    print('=' * 100)

    with ProcessPoolExecutor(8) as e:
        calc(e)
        print('=' * 100)
        sleep_test(e)
