#!/usr/bin/env python3
# -*- coding: utf-8 -*-


L = ['li', 'zhi', 'tao', 'is', 'my', 'name']
print(L)
print(L[0:3])
print(L[-2:])

L = list(range(100))
# 前十个
print(L[:10])
# 后十个
print(L[-10:])
# 前十个数每两个取一个
print(L[:10:2])
# 所有数每五个取一个
print(L[::5])

# string slice
print('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:5])
