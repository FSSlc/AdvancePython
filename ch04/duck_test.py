#!/usr/bin/env python
# coding: utf-8

class Cat(object):
    def say(self):
        print("I'm a cat")


class Dog(object):
    def say(self):
        print("I'm a dog")


class Duck(object):
    def say(self):
        print("I'm a duck")


animal = Cat
animal().say()

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()

a = ["name01", "name02"]
b = ["name03", "name04"]
name_tuple = ("name05", "name06")
name_set = set()
name_set.add("name07")
name_set.add("name08")
a.extend(name_set)
print(a)
