#!/usr/bin/env python
# coding: utf-8

class A:
    # 类变量
    aa = 1

    def __init__(self, x, y):
        # 这里赋值后是实例的变量
        self.x = x
        self.y = y


a = A(2, 3)
A.aa = 11  # 修改类属性
a.aa = 100  # 这里会新建属性 aa 到实例中
print(a.x, a.y, a.aa)
print(A.aa)

b = A(3, 5)
print(b.aa)
