#!/usr/bin/env python
# coding: utf-8

import multiprocessing
import os
import time


# print('user') # 放到这里 就只打印一次 user
# pid = os.fork()
# print('user')
# if pid == 0:
#     print('子进程 {},  父进程 {}'.format(os.getpid(), os.getppid()))
# else:
#     print('我是父进程 {}'.format(os.getppid()))
#
# time.sleep(2) # 这里需要有，否则主进程先退出


# 多进程编程
def get_html(n):
    time.sleep(n)
    print('sub_process success')
    return n


class MyProcess(multiprocessing.Process):
    def __init__(self, n):
        super(MyProcess, self).__init__()
        self.n = n

    def run(self) -> None:
        time.sleep(self.n)
        print('sub_process success')


def calc_times(a, b):
    time.sleep(1)
    return a * b


if __name__ == '__main__':
    # 直接使用 Process 实例
    progress = multiprocessing.Process(target=get_html, args=(2,))
    print(progress.pid)
    progress.start()
    print(progress.pid)
    progress.join()
    print('main progress end using Process instance')
    # 继承类
    my_process = MyProcess(2)
    my_process.start()
    print('main progress end using custom class')

    # 线程池
    with multiprocessing.Pool(os.cpu_count()) as pool:
        result = pool.apply_async(get_html, args=(3,))
    # 等待所有任务完成
    pool.join()
    print(result.get())

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        # imap
        for result in pool.imap(get_html, [1, 5, 3]):
            print('{} sleep success'.format(result))

        # imap_unordered
        for result in pool.imap_unordered(get_html, [1, 5, 3]):
            print('{} sleep success'.format(result))

        # starmap 可以用于执行函数参数为多个的时候
        for result in pool.starmap(calc_times, list(zip([1, 2, 3], [3, 4, 5]))):
            print('calc result = {}'.format(result))
