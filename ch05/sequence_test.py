#!/usr/bin/env python
# coding: utf-8

from collections import abc

a = [1, 2]
c = a + [3, 4]

# 就地加，+= 对应 __iadd__ 魔法函数
a += (3, 4)
# extend，具体实现是直接 for 循环再 append，而 append 则使用 insert 实现
a.extend(range(3))
# 直接添加数据，不会迭代
a.append([1, 2])
print(a)
