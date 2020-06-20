#!/usr/bin/env python
# coding: utf-8

"""
Python 中函数的工作原理:
    Python 解释器会使用一个叫做 PyEvalFramEx 的 C 函数去执行函数
    首先会创建一个栈帧(stack frame),栈帧也是一个对象,
    然后在栈帧对象的上下文中运行字节码
    所有的栈帧都是分配在堆内存上,这就决定了栈帧可以独立于调用者存在
"""
import dis
import inspect

frame = None


def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()


def gen_func():
    yield 1
    name = "user"
    yield 2
    age = 20
    return "GenFunc"


if __name__ == '__main__':
    foo()
    print(dis.dis(foo))
    print(frame.f_code.co_name)
    caller_frame = frame.f_back
    print(caller_frame.f_code.co_name)
    gen = gen_func()
    print(dis.dis(gen))
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
    next(gen)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)
