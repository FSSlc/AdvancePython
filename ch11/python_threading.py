#!/usr/bin/env python
# coding: utf-8

"""
对于 io 操作来说，多线程和多进程性能差别不大
使用方法：
1. 通过 Thread 类实例化来实现多线程
2. 通过继承 Thread 来实现多线程
"""
import threading
import time


def get_detail_html(url):
    print('get detail  html started')
    time.sleep(2)
    print('get detail  html end')


def get_detail_url(url):
    print('get detail  url started')
    time.sleep(4)
    print('get detail  url end')


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail  html started')
        time.sleep(2)
        print('get detail  html end')


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get detail  url started')
        time.sleep(4)
        print('get detail  url end')


if __name__ == '__main__':
    print(" 通过 Thread 类实例化实现多线程 ".center(100, '#'))
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    started_time = time.time()

    thread1.setDaemon(True)
    thread2.setDaemon(True)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("last time: {}".format(time.time() - started_time))

    print(" 通过继承 Thread 类实现多线程 ".center(100, '#'))
    thread1 = GetDetailHtml('get detail html')
    thread2 = GetDetailUrl('get detail url')
    thread1.start()
    thread2.start()
