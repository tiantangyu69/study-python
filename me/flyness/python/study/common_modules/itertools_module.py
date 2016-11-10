#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

natuals = itertools.count(1)
for n in natuals:
    if n > 1000:
        break
    print(n)

cs = itertools.cycle('ABC')
stop = 100
for c in cs:
    if stop == 0:
        break
    print(c)
    stop = stop - 1

ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))
