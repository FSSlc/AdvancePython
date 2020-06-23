#!/usr/bin/env python
# coding: utf-8

# def get_url(url):
#     # do something 1
#     html = get_html(url)  # 此处暂停，切换到另一个函数去执行
#     # parse html
#     urls = parse_url(html)

# 传统函数调用过程 A -> B -> C
# 需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行
# 协程 -> 有多个入口的函数， 可以暂停的函数，可以向暂停的地方传入值

def gen_func():
    # 可以产出值，可以接收值（调用方传递进来的值）
    html = yield "http://projectsedu.com"
    print(html)
    yield 2
    yield 3
    return 'user'


# 1. 生成器不只可以产出值，还可以接收值

# 启动生成器方式： 1. next() 2. send
if __name__ == '__main__':
    gen = gen_func()
    # 在调用 send 发送非 None 值之前，必须启动一次生成器，方法 1. next(gen) 2. gen.send(None)
    url = gen.send(None)  # 最开始没有执行过生成器的话，就没法运行到 send 要发送的代码
    url = next(gen)
    html = 'user'
    print(gen.send(html))  # send 方法可以传递值进入生成器内部，同时还可以重启生成器执行下一步
