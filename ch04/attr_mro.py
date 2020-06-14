#!/usr/bin/env python
# coding: utf-8


class A:
    name = 'A'

    def __init__(self):
        self.name = 'obj'


a = A()
print(a.name)


# 菱形继承
class E:
    pass


class D(E):
    pass


class C(E):
    pass


class B(C, D):
    pass


print(B.__mro__)


# 分叉的情形
class D1:
    pass


class B1(D1):
    pass


class E1():
    pass


class C1:
    pass


class A1(B1, C1):
    pass


print(A1.__mro__)
