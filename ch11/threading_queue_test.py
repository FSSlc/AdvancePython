#!/usr/bin/env python
# coding: utf-8

"""
线程间通信方式：
1. 共享变量
2. 通过 queue
"""
import threading
import time
from queue import Queue


def get_detail_html(queue):
    # 爬取文章详情页
    while True:
        url = queue.get()
        print('get detail html  {} started'.format(url))
        time.sleep(2)
        print('get detail  html end')


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print('get detail  url started')
        time.sleep(4)
        for i in range(20):
            queue.put("http://project.com/{id}".format(id=i))
        print('get detail  url end')


if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)

    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()

    detail_url_queue.task_done()
    detail_url_queue.join()