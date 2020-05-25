#!/usr/bin/env python
# coding: utf-8

# 函数和类为一等公民

# -- 函数示例
def ask(name="fsslc"):
    print(name)


my_func = ask
ask("fsslc")


# -- 类示例
class Person:
    def __init__(self):
        print("fsslc")


my_class = Person
my_class()

object_list = [ask, Person]
for item in object_list:
    print(item())
