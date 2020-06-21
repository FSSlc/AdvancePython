#!/usr/bin/env python
# coding: utf-8
"""
线程池：
主线程可以获取某一个线程的状态或者某一个任务的状态以及返回值
当一个线程完成的时候我们的主线程能立即知道
futures 可以让多线程和多进程的编码接口一致
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=1)

# 通过 submit 函数提交执行的函数到线程池中，submit 是立即返回的
task1 = executor.submit(get_html, 3)
task2 = executor.submit(get_html, 2)

# done 方法用于判定任务是否完成
print(task1.done())
time.sleep(3)
print(task1.done())

# result 方法可以获取 task 的执行结果，是一个阻塞的方法
print(task1.result())
# cancel 方法
print(task2.cancel())

# 获取已经成功的 task 的返回
urls = [2, 3, 4]
all_task = [executor.submit(get_html, url) for url in urls]

wait(all_task, return_when=FIRST_COMPLETED)
print('main')

for future in as_completed(all_task):
    data = future.result()
    print("get {} page success".format(data))

# 通过 executor 的 map 来获取已经完成的 task 的值
for data in executor.map(get_html, urls):
    print("get {} page success".format(data))
