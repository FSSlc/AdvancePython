#!/usr/bin/env python
# coding: utf-8

"""
条件变量：用于复杂的线程间同步，内部使用 Lock 或者 RLock 来实现
"""
import threading


# 通过锁来完成对话，但顺序可能不对
class XiaoAi(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="小爱同学")
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("{}: 在".format(self.name))
        self.lock.release()

        self.lock.acquire()
        print("{}: 好呀".format(self.name))
        self.lock.release()


class TianMao(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="天猫精灵")
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("{}: 小爱同学".format(self.name))
        self.lock.release()

        self.lock.acquire()
        print("{}: 让我们来对古诗吧".format(self.name))
        self.lock.release()


# 通过 condition 来完成协同对话

class XiaoAi(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="小爱同学")
        self.condition = condition

    def run(self):
        with self.condition:
            self.condition.wait()
            print("{}: 在".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 好呀".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 君住长江尾".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 共饮长江水".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 此恨何时已".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 定不负相思意".format(self.name))
            self.condition.notify()


class TianMao(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="天猫精灵")
        self.condition = condition

    def run(self):
        with self.condition:
            print("{}: 小爱同学".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 我们来对古诗吧".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 我住长江头".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 日夜思君不见君".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 此水几时休".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 只是君心似我心".format(self.name))
            self.condition.notify()
            self.condition.wait()


if __name__ == '__main__':
    condition = threading.Condition()

    tian_mao = TianMao(condition)
    xiao_ai = XiaoAi(condition)

    # 注意：
    # 1. 启动顺序非常重要
    # 2. 只有调用 with condition 之后才能调用 notify 或 wait语句
    # condition 有两层锁，一把底层锁会在调用了 wait 方法的时候释放
    # 上面的锁会在每次调用 wait 的时候分配一把锁并放入到 condition 的等待队列中，并等到 notify 的唤醒
    xiao_ai.start()
    tian_mao.start()
