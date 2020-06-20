#!/usr/bin/env python
# coding: utf-8

from collections.abc import Iterator


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.employee_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.employee_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    company = Company(["a", "b", "c"])
    for item in company:
        print(item)
