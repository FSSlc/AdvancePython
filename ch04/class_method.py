#!/usr/bin/env python
# coding: utf-8


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year, month=self.month, day=self.day)

    # 实例方法
    def tomorrow(self):
        self.day += 1

    # 静态方法
    @staticmethod
    def parse_from_str(data_str):
        year, month, day = tuple(data_str.split('-'))
        return Date(int(year), int(month), int(day))

    @staticmethod
    def valid_str(data_str):
        year, month, day = tuple(data_str.split('-'))
        if int(year) > 0 and (int(month) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) <= 31):
            return True
        else:
            return False

    # 类方法
    @classmethod
    def from_str(cls, data_str):
        year, month, day = tuple(data_str.split('-'))
        return cls(int(year), int(month), int(day))


if __name__ == '__main__':
    new_day = Date(2020, 6, 14)
    new_day.tomorrow()
    print(new_day)

    data_str = "2020-06-14"
    year, month, day = tuple(data_str.split('-'))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # 用静态方法来完成初始化
    new_day = Date.parse_from_str(data_str)
    print(new_day)

    # 用类方法来完成初始化
    new_day = Date.from_str(data_str)
    print(new_day)

    # 用静态方法来检验日期字符串是否合法
    print(Date.valid_str("2020-12-32"))
