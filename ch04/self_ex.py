#!/usr/bin/env python
# coding: utf-8

class Person:
    """A person"""
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student('imooc')

    # 通过 __dict__ 查询属性
    print(user.__dict__)
    # 尝试直接修改示例的 __dict__
    user.__dict__['school_addr'] = '北京市'
    print(user.school_addr)
    print(user.name)

    print(Person.__dict__)

    # dir 列出对象的所有属性
    dir(user)
