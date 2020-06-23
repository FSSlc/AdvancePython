#!/usr/bin/env python
# coding: utf-8
"""
yield from 是 Python 3.3 新加的语法

yield from iterable
"""

my_list = [1, 2, 3]
my_dict = {
    'user1': 'http://abc1.com',
    'user2': 'http://abc2.com',
}


# for value in chain(my_list, my_dict, range(5, 10)):
#     print(value)


def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value


for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)


# ---------
def g1(iterable):
    yield range(10)


def g2(iterable):
    yield from range(10)


for value in g1(range(10)):
    print(value)
for value in g2(range(10)):
    print(value)


# ---------
def g3(gen):
    yield from gen


def g4():
    g = g3()
    g.send(None)
# g4 调用方， g3（委托生成器） gen 子生成器
# yield from 会在调用方和子生成器之间建立一个双向通道
