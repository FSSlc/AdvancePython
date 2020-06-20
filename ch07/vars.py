#!/usr/bin/env python
# coding: utf-8

# python 和 java 中的变量本质不一样， Python 的变量实质上是一个指针

a = 1
a = "abc"
# 1. a 贴在 1 上面 2. 先生成对象，然后贴便利贴

a = [1, 2, 3]
b = a
print(id(a), id(b))
print(a is b)
b.append(4)
print(a)

b = [1, 2, 3]
print(a == b) # 实现 __equal__ 判断值相等
print(id(a), id(b))
# 优化机制，小整数 str
a = 1
b = 1
print(id(a), id(b))
