#!/usr/bin/env python
# coding: utf-8

final_result = {}


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + " 销量：", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


def middle(key):
    while True:
        # 子生成器计算完成后的值赋值到这里
        final_result[key] = yield from sales_sum(key)
        print(key + " 销量统计完成！！")


def main():
    data_sets = {
        "goods01": [1200, 1203, 1800],
        "goods02": [28, 10, 61],
        "goods03": [209, 290, 801],
    }
    for key, data_sets in data_sets.items():
        print("start key:", key)
        m = middle(key)
        m.send(None)  # 预激 middle 协程
        for value in data_sets:
            m.send(value)  # 给协程传递一组值
        m.send(None)  # 结束子生成器，对应 break 那句
    print("final_result: ", final_result)


if __name__ == '__main__':
    main()
    # ----- 另一个示例，展示 yield from 的必要性
    my_gen = sales_sum("goods01")
    my_gen.send(None)
    my_gen.send(1200)
    my_gen.send(1203)
    my_gen.send(1800)
    try:
        my_gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)
