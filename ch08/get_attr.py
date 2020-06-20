#!/usr/bin/env python
# coding: utf-8

from datetime import date

class User:
    def __init__(self, name, birthday, info=None):
        if info is None:
            info = {}
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        # __getattr__ 在查找不到属性的时候调用
        return self.info[item]

    def __getattribute__(self, item):
        # 调用属性时，无条件调用该函数
        return "user2"


if __name__ == '__main__':
    user = User("user", date(year=2000, month=1, day=1), info={"company_name": "abc"})
    print(user.company_name)
