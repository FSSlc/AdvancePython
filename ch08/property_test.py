#!/usr/bin/env python
# coding: utf-8

from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    # 对动态属性的设值
    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User("user", date(year=2000, month=1, day=1))
    user.age = 30
    print(user._age)
    print(user.age)
