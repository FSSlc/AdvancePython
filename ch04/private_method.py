#!/usr/bin/env python
# coding: utf-8

from class_method import Date


class User:
    def __init__(self, birthday):
        # 私有属性
        self.__birthday = birthday

    def get_age(self):
        return 2020 - self.__birthday.year


class Student(User):
    def __init__(self, birthday):
        self.__birthday = birthday


if __name__ == '__main__':
    user = User(Date(1999, 2, 1))
    # 仍然能够通过下面的方法来访问私有属性
    print(user._User__birthday)
    print(user.get_age())
    student = Student(Date(1999, 2, 1))
    print(student._Student__birthday)
