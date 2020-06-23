#!/usr/bin/env python
# coding: utf-8


def gen_func():
    try:
        yield "user"
    except Exception as e:
        pass

    yield 2
    yield 3
    return 'user'


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")
    print(next(gen))
    gen.throw(Exception, "download error")
