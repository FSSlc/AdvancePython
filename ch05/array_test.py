#!/usr/bin/env python
# coding: utf-8

import array  # array 只能存放指定数据类型的数据

my_array = array.array('i')
my_array.append(1)
my_array.fromlist([3, 4, 5])
print(my_array)
