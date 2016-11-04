#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# default parameters
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 4))


# variable parameters
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


print(calc(1, 2, 3, 4, 5, 65))


# keyword parameters
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('lizhitao', 27)
person('lizhitao', 27, city='beijing', gender='M')

extra = {'city': 'beijing', 'gender': 'M'}
person('lizhitao', 27, **extra)


def person(name, age, *, city, gender):
    print('name:', name, 'age:', age, 'city:', city, 'gender:', gender)


extra = {'city': 'beijing', 'gender': 'M'}
person('lizhitao', 27, **extra)


# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
