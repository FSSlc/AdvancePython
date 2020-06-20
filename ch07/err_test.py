#!/usr/bin/env python
# coding: utf-8


def add(a, b):
    a += b
    return a


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == '__main__':
    a = 1
    b = 2
    c = add(a, b)
    print(c)
    print(a, b)

    a = [1, 2]
    b = [3, 4]
    c = add(a, b)
    print(c)
    print(a, b)  # 注意：这里的 a 被改变了！

    a = (1, 2)
    b = (3, 4)
    c = add(a, b)
    print(c)
    print(a, b)

    com1 = Company("com1", ["s1", "s2"])
    com1.add("s3")
    com1.remove("s1")
    print(com1.staffs)

    com2 = Company("com2")
    com2.add("s4")
    print(com2.staffs)

    print(Company.__init__.__defaults__)

    com3 = Company("com3")
    com3.add("s5")
    print(com2.staffs)
    print(com3.staffs)
    print(com2.staffs is com3.staffs) # 为 True，因为 1. staffs 是 list 可变 2. 使用来同样的默认对象


