#!/usr/bin/env python
# coding: utf-8

def get_url(url):
    # do something 1
    html = get_html(url)  # 此处暂停，切换到另一个函数去执行
    # parse html
    urls = parse_url(html)

# 传统函数调用过程 A -> B -> C
# 需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行
# 协程 -> 有多个入口的函数， 可以暂停的函数，可以向暂停的地方传入值