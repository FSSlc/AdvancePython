#!/usr/bin/env python
# coding: utf-8

s = set('abcdds')
s.add('e')

print(s)
s = set(['a', 'b', 'c', 'd'])
print(s)

s = {'a', 'b'}
print(type(s))

# frozenset 可以作为 dict 的 key
s = frozenset("abdddfk")

# 向 set 添加数据
another_set = set('def')
ss = set("dkfwe")
ss.update(another_set)

# 集合的差集
sss = ss.difference(another_set)
ssss = ss - another_set
# 集合的交集
sss = ss & another_set
# 集合的并集
ssss = ss | another_set
