#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((x * x for x in range(10)), Iterator))
