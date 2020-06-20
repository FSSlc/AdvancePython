#!/usr/bin/env python
# coding: utf-8

# cpython 中的垃圾回收的算法采用的事 引用计数
a = 1
b = a
del a

a = object()
b = a
del a
print(b, a)
