#!/usr/bin/env python
# coding: utf-8

import numbers


class IntField:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value needed")
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    age = IntField()


if __name__ == '__main__':
    user = User()
    user.age = 30
    print(user.age)


"""
如果 user 是某个类的实例，那么 user.age（以及等价的 getattr(user, 'age') ）的查找过程：
首先调用 __getattribute__
如果类定义了 __getattr__ 方法，
那么在 __getattribute__ 抛出 AttributeError 的时候就会调用到 __getattr__
面对描述符 __get__ 的调用，则是发生在 __getattribute__ 内部的。

user = User()，那么 user.age 的顺序如下：
1. 如果 age 是出现在 User 或者其基类的 __dict__ 中，且 age 时 data descriptor，
    那么调用其 __get__ 方法，否则
2. 如果 age 出现在 obj 的 __dict__ 中，那么直接返回 obj.__dict__['age']，否则
3. 如果 age 出现在 User 或者基类的 __dict__ 中
3.1 如果 age 是 non-data descriptor 那么调用其 __get__ 方法，否则
3.2 返回 __dict__['age']
4. 如果 User 有 __getattr__ 方法，调用 __getattr__ 方法，否则
5. 抛出 AttributeError
"""