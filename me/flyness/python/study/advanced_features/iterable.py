#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print('i:', i, 'value:', value)
