#!/usr/bin/env python
# coding: utf-8
"""
通过 Queue 来进行进程间通信
共享全局变量不能适用于多进程编程，可以适用于多线程编程
multiprocessing 中的 Queue 不能用于 pool 线程池
pool 中的进程间通信需要使用 manager 中的 Queue
还可以使用管道 pipe 来进行进程间通信
"""

import multiprocessing
import time
from multiprocessing import Process, Queue, Manager, Pipe


def producer(queue):
    queue.put('a')
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


def producer_pipe(pipe):
    pipe.send('user')


def consumer_pipe(pipe):
    print(pipe.recv())


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == '__main__':
    queue = Queue(10)
    my_producer = Process(target=producer, args=(queue,))
    my_consumer = Process(target=consumer, args=(queue,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

    # 使用线程池
    # 使用 Manager 实例化的 Queue 来通信
    queue = Manager().Queue(10)
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        pool.apply_async(producer, args=(queue,))
        pool.apply_async(consumer, args=(queue,))
    pool.join()

    # 使用 Pipe 来通信
    # Pipe 只能适合于 2 个进程
    # Pipe 的性能比较高
    receive_pipe, send_pipe = Pipe()
    my_producer = Process(target=producer_pipe, args=(send_pipe,))
    my_consumer = Process(target=consumer_pipe, args=(receive_pipe,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

    # Manager 中包含了常见的通信方式和数据结构例如 dict Array Condition 等
    process_dict = Manager().dict()
    first_progress = Process(target=add_data, args=(process_dict, 'user1', 22))
    second_progress = Process(target=add_data, args=(process_dict, 'user2', 23))
    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()

    print(process_dict)
