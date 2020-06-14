#!/usr/bin/env python
# coding: utf-8

import abc
from collections.abc import Sized


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


company = Company(["c1", "c2"])
# 判断一个类是否有某个方法
print(hasattr(company, "__len__"))

# 我们在某些情况之下希望判定某个对象的类型

isinstance(company, Sized)


# 我们需要强制某个子类必须实现某些方法
# eg. 实现了一个 WEB 框架，集成 cache(redis cache memorycache)
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 如何模拟一个抽象基类
class CacheBase(object):
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


# 弊端：只有调用 set 方法时才会报异常
class RedisCache(CacheBase):
    def set(self, key, value):
        pass


redis_cache = RedisCache()
redis_cache.set("k", "v")


# 使用 abc 来实现
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    pass


redis_cache = RedisCache()
