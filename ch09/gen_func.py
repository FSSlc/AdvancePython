#!/usr/bin/env python
# coding: utf-8

"""
函数中只要哟 yield 关键字就可以称为 生成器函数
生成器对象在 pythn 编译字节码的时候就产生了
"""


def func():
    return 1


def gen_func():
    yield 1


def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


def fib2(index):
    res = []
    n, a, b = 0, 0, 1
    while n < index:
        res.append(b)
        a, b = b, a + b
        n += 1
    return res


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


if __name__ == '__main__':
    gen = gen_func()
    for var in gen:
        print(var)
    res = func()
    print(fib(10))
    for data in gen_fib(10):
        print(data)
