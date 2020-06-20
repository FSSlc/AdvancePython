#!/usr/bin/env python
# coding: utf-8

# __new__ 用来控制对象的生成过程，在对象生成之前
# __init__ 用来完善对象
# 如果 new 方法不返回对象,则不会调用 init 方法


class User:
    def __new__(cls, *args, **kwargs):
        # 对类的生成过程做操作
        print("in new")
        return super().__new__(cls)

    def __init__(self, name):
        # 对对象做操作
        print("int init")
        self.name = name


if __name__ == '__main__':
    user = User()
