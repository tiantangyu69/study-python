#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def fn(x, y):
    return x + y


print(reduce(fn, [1, 2, 3, 4, 5]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 2, 3, 4, 5]))


def str2int(s):
    def fn1(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn1, map(char2num, s))


print(str2int('11111'))
