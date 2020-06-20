#!/usr/bin/env python
# coding: utf-8

"""
1. 迭代器是访问集合内元素的一种方式,一般用来遍历数据
2. 迭代器是不能返回的,提供了一种惰性方式数据的方法
3. Iterable 为可迭代对象,实现 __iter__ 即可, Iterator 还需要实现 __next__
"""

from collections.abc import Iterable, Iterator

a = [1, 2]
iterator = iter(a)
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(iterator, Iterator))
