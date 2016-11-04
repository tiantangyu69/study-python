#!/usr/bin/env python3
# -*- coding: utf-8 -*-


L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

g = [x * x for x in range(1, 11)]
g1 = [x * x for x in range(1, 11) if x % 2 == 0]
g2 = [m + n for m in 'ABC' for n in 'XYZ']
g3 = [k + '=' + v for k, v in {'a': 'a', 'b': 'b'}.items()]

print('g:', g)
print('g1:', g1)
print('g2:', g2)
print('g3:', g3)
