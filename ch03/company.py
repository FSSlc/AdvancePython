#!/usr/bin/env python
# coding: utf-8

class Company(object):
    """示例一个简单的类"""

    def __init__(self, employee_list):
        self.employee = employee_list


company = Company(["a", "b", "c"])
for em in company.employee:
    print(em)


# 下面示例定义魔法函数 __getitem__ 方法
class ACompany(object):
    """示例一个简单的类"""

    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]


company = ACompany(["a", "b", "c"])
for em in company:
    print(em)
