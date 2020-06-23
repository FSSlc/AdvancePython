#!/usr/bin/env python
# coding: utf-8

def gen_func():
    try:
        yield "user"
    except GeneratorExit:
        raise StopIteration

    yield 2
    yield 3
    return 'user'

# GeneratorExit 继承自 BaseException，并没有继承 Exception

if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    next(gen)

    # GeneratorExit 是继承 BaseException