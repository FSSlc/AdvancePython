#!/usr/bin/env python
# coding: utf-8

a = 1
print(type(1))
print(type(int))
print(int.__base__)
b = "abc"
print(type(b))
print(type(str))
print(str.__base__)

class Student:
    pass

stu = Student()
print(type(stu))
print(type(Student))
print(Student.__base__)

class MyStudent(Student):
    pass
print(MyStudent.__base__)

print(type.__base__)
print(type(object))
print(object.__base__)
