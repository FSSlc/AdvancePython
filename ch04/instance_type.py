#!/usr/bin/env python
# coding: utf-8

class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))

# is 是判断是否为同一个对象， == 判断值是否相等
print(type(b) is B)
print(type(b) is A)
