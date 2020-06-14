#!/usr/bin/env python
# coding: utf-8

def exe_try():
    try:
        print('code started')
        raise KeyError
        return 1
    except KeyError as e:
        print(e, 'key error')
        return 2
    else:
        print('other error')
        return 3
    finally:
        print('finally')
        return 4


class Sample:
    # 上下文管理器示例
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def do(self):
        print('do something')


if __name__ == "__main__":
    result = exe_try()
    print(result)

    with Sample() as sample:
        sample.do()
