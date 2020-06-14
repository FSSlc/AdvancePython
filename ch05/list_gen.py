#!/usr/bin/env python
# coding: utf-8

# 列表生成式的性能高于列表操作
# 1. 提取 1-20 之间的奇数
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)
print(type(odd_list))

# 2. 逻辑复杂的情况


def handle_item(i): return i*i  # noqa


a_list = [handle_item(i) for i in range(21) if i % 2 == 1]  # noqa
print(a_list)

# 生成器表达式
odd_list = (i for i in range(21) if i % 2 == 1)
type(odd_list)
for item in odd_list:
    print(item)

# 字典推导式
my_dict = {'user1': 1, 'user2': 2, 'user3': 3, 'user4': 4}
revised_dict = {v: k for k, v in my_dict.items()}


# 集合推导式
my_set = {key for key, _ in my_dict.items()}
