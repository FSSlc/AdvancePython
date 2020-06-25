#!/usr/bin/env python
# coding: utf-8
"""
示例 asyncio 任务的取消和任务的嵌套
"""
import asyncio


# loop 会被放到 future 中
# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()

# 取消 future(task)

async def get_html(sleep_times):
    print('waitting')
    await asyncio.sleep(sleep_times)
    print('done after {}s'.format(sleep_times))


# 子协程嵌套 chaining coroutines
async def compute(x, y):
    print('Compute {x} + {y}'.format(x=x, y=y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print('Compute {x} + {y} = {result}'.format(x=x, y=y, result=result))


if __name__ == '__main__':
    # task01 = get_html(1)
    # task02 = get_html(2)
    # task03 = get_html(3)
    #
    # tasks = [task01, task02, task03]
    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(asyncio.wait(tasks))
    # except KeyboardInterrupt as e:
    #     # 取消所有任务
    #     all_tasks = asyncio.all_tasks()
    #     for task in all_tasks:
    #         print('cancel task')
    #         print(task.cancel())
    #     loop.stop()
    #     loop.run_forever()  # 一定要有这一句
    # finally:
    #     loop.close()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()
