#!/usr/bin/env python
# coding: utf-8

import bisect  # 用来处理已排序的序列，用来维持已排序的序列为升序

# 二分查找
alist = []
bisect.insort(alist, 3)
bisect.insort(alist, 2)
bisect.insort(alist, 5)
bisect.insort(alist, 1)
bisect.insort(alist, 6)

print(bisect.bisect(alist, 3))
print(bisect.bisect_left(alist, 3))
print(alist)
