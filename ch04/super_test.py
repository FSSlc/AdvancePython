#!/usr/bin/env python
# coding: utf-8

class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()  # Python 2 的用法
        super().__init__()   # Python 3 的简化

# 1. 既然重写了 B 的构造函数，为什么还有去调用 super？
    # 可以重用代码
# 2. super 的执行顺序是什么样的？
    # 依赖 mro 算法


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()


if __name__ == '__main__':
    b = B()
    print(D.__mro__)
    d = D()
    