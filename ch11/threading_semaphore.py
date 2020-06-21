#!/usr/bin/env python
# coding: utf-8

"""
Semaphore：用于控制进入数量的锁
场景：文件的读写一般只是一个线程写，可以运行多个线程来读
     做爬虫时控制并发数
"""
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, semaphore):
        super().__init__()
        self.url = url
        self.semaphore = semaphore

    def run(self) -> None:
        time.sleep(2)
        print('get html text success')
        self.semaphore.release()


class UrlProducer(threading.Thread):
    def __init__(self, semaphore):
        super().__init__()
        self.semaphore = semaphore

    def run(self) -> None:
        for i in range(20):
            self.semaphore.acquire()
            html_thread = HtmlSpider("https://www.baidu.com/{}".format(i), self.semaphore)
            html_thread.start()


if __name__ == '__main__':
    semaphore = threading.Semaphore(3)
    url_producer = UrlProducer(semaphore)
    url_producer.start()
