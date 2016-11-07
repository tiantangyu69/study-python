#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


print(calc_sum(1, 2, 3, 4, 5, 6, 7, 8))
sum = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8)
print(sum())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# def count():
#     f = lambda j: j * j
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs
#
#
# f1, f2, f3 = count()
# print(f1(), f2(), f3())
