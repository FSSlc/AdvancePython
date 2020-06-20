#!/usr/bin/env python
# coding: utf-8

from collections import UserDict, defaultdict


# 不建议继承 list 和 dict，是 c 语言实现方法，不会调用自定义的方法

class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)  # 这里 one 的值还是 1
my_dict["one"] = 1  # 这里 one 的值才是 2
print(my_dict)


class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)  # 这里 one 的值还是 1

my_dict = defaultdict(dict)
my_value = my_dict["user"]  # 没有 key 时调用 __missing__
