#!/usr/bin/env python
# coding: utf-8


def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"

        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


def say(self):
    return "I'm user"
    # return self.name


class BaseClass:
    def answer(self):
        return "I'm base class"


"""
元类是创建类的类, 对象 <- class(对象) <- type

python 中类的实例化过程,会首先寻找 metaclass,通过 metaclass 去创建类
type 去创建类对象,实例
"""


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user"


if __name__ == '__main__':
    my_class = create_class("user")
    my_obj = my_class
    print(my_obj)

    # type 动态创建类,类也是对象, type 创建类的类
    User = type("User", (), {})
    my_obj = User()
    print(my_obj)

    # 添加一个属性
    User = type("User", (), {"name": "user"})
    my_obj = User()
    print(my_obj.name)

    # 添加属性和方法
    User = type("User", (), {"name": "user", "say": say})
    my_obj = User()
    print(my_obj.say())

    # 添加属性和方法以及基类
    User = type("User", (BaseClass,), {"name": "user", "say": say})
    my_obj = User()
    print(my_obj.answer())

    my_obj = User(name="newUser")
